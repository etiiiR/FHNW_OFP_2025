from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Callable, Dict


# -------------------------------
# Transaktionsmodelle
# -------------------------------

@dataclass(frozen=True)
class Transaction:
    """Repräsentiert eine vollständige Buchung in der Bank (Journal)."""
    timestamp: int
    from_account: Optional[str]  # None bei Bareinzahlungen
    to_account: Optional[str]
    amount: float                # immer positiv
    usage: str = ""


@dataclass(frozen=True)
class TransactionEntry:
    """
    Eine einzelne Buchungseintragung in einem Konto-Journal.
    Der Betrag ist negativ, wenn es sich um eine Belastung handelt, und positiv bei Gutschrift.
    """
    timestamp: int
    counterparty: Optional[str]  # Bei Bareinzahlungen z.B. None
    amount: float
    usage: str = ""


# -------------------------------
# Abstrakte Konto-Klasse und Implementierungen
# -------------------------------

class Account(ABC):
    """
    Abstrakte Basisklasse für alle Konten.
    Jedes Konto hat eine eindeutige ID, einen Saldo, einen Status und ein eigenes Buchungsjournal.
    """

    def __init__(self, account_id: str) -> None:
        self._account_id: str = account_id
        self._balance: float = 0.0
        self._active: bool = True
        self._transactions: List[TransactionEntry] = []

    @property
    def id(self) -> str:
        return self._account_id

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def is_active(self) -> bool:
        return self._active

    @property
    def transactions(self) -> List[TransactionEntry]:
        return self._transactions.copy()

    def get_transactions(self, count: Optional[int] = None) -> List[TransactionEntry]:
        if count is None:
            return self.transactions
        return self._transactions[-count:]

    def close(self) -> bool:
        """Schliesst das Konto, falls der Saldo exakt 0 beträgt."""
        if self._balance == 0:
            self._active = False
            return True
        return False

    def _record_transaction(self, entry: TransactionEntry) -> None:
        self._transactions.append(entry)

    def deposit_amount(self, amount: float) -> None:
        self._balance += amount

    def withdraw_amount(self, amount: float) -> None:
        self._balance -= amount

    @abstractmethod
    def can_withdraw(self, amount: float) -> bool:
        """
        Prüft, ob eine Abbuchung des gegebenen Betrags zulässig ist.
        Muss in den konkreten Kontotypen implementiert werden.
        """
        ...

    def calculate_fee(self, amount: float) -> float:
        """
        Berechnet eine Gebührenaufschlag bei Abbuchungen.
        Standardmäßig keine Gebühr – in abgeleiteten Klassen (z.B. Privatkonto) zu überschreiben.
        """
        return 0.0

    def __str__(self) -> str:
        status = "aktiv" if self._active else "geschlossen"
        return f"<Konto {self._account_id}: Saldo={self._balance:.2f} ({status})>"


class YouthAccount(Account):
    """
    Jugendkonto: Darf niemals ins Negative gehen – alle Buchungen erfolgen gebührenfrei.
    """

    def can_withdraw(self, amount: float) -> bool:
        return self._balance >= amount


class SavingsAccount(Account):
    """
    Sparkonto: Darf niemals ins Negative gehen, gebührenfrei.
    Optional kann hier auch ein Zinssatz implementiert werden.
    """

    def __init__(self, account_id: str, interest_rate: float = 0.01) -> None:
        super().__init__(account_id)
        self.interest_rate: float = interest_rate

    def can_withdraw(self, amount: float) -> bool:
        return self._balance >= amount

    def apply_interest(self) -> None:
        """Zinsgutschrift – hier als Beispiel: Das Guthaben wird verzinst."""
        interest = self._balance * self.interest_rate
        self.deposit_amount(interest)
        # Eine Buchung im Konto-Journal könnte hier ebenfalls erfolgen.
        

class PrivateAccount(Account):
    """
    Privatkonto: Erlaubt ein negatives Guthaben bis zu einem festgelegten Limit.
    Für Abbuchungen wird eine Gebühr berechnet.
    """

    def __init__(self, account_id: str, overdraft_limit: float = 500.0, fee_rate: float = 0.01) -> None:
        super().__init__(account_id)
        self.overdraft_limit: float = overdraft_limit
        self.fee_rate: float = fee_rate

    def can_withdraw(self, amount: float) -> bool:
        # Es ist zulässig, wenn nach der Abbuchung der Saldo nicht unter -overdraft_limit sinkt.
        return (self._balance - amount) >= -self.overdraft_limit

    def calculate_fee(self, amount: float) -> float:
        # Beispiel: 1% des abgebuchten Betrags als Gebühr
        return amount * self.fee_rate


class FeeAccount(Account):
    """
    Ein spezielles Konto der Bank zur Erfassung von Gebühren.
    Normalerweise dürfen von diesem Konto keine Abbuchungen vorgenommen werden.
    """

    def can_withdraw(self, amount: float) -> bool:
        return False  # Rückbuchungen sind hier nicht vorgesehen.


# -------------------------------
# Die Bank
# -------------------------------

class Bank:
    """
    Repräsentiert die Bank, die Konten verwaltet, Buchungen ausführt und
    ein globales Buchungsjournal führt.
    """

    def __init__(self) -> None:
        self._accounts: Dict[str, Account] = {}
        self._journal: List[Transaction] = []
        self._current_timestamp: int = 0
        self._account_id_counter: int = 1

        # Konto-Factory: Hier können verschiedene Kontotypen registriert werden.
        self._account_factories: Dict[str, Callable[[str], Account]] = {}
        self.register_account_type("youth", lambda aid: YouthAccount(aid))
        self.register_account_type("savings", lambda aid: SavingsAccount(aid))
        self.register_account_type("private", lambda aid: PrivateAccount(aid))
        # Das Gebührenkonto der Bank (wird intern verwendet)
        self._fee_account = FeeAccount("FEE-0001")
        self._accounts[self._fee_account.id] = self._fee_account

    def _get_timestamp(self) -> int:
        self._current_timestamp += 1
        return self._current_timestamp

    def register_account_type(self, type_name: str, factory: Callable[[str], Account]) -> None:
        """
        Ermöglicht die Registrierung neuer Kontotypen, ohne den Kern der Bank zu ändern.
        """
        self._account_factories[type_name.lower()] = factory

    def _generate_account_id(self) -> str:
        aid = f"A{self._account_id_counter:06d}"
        self._account_id_counter += 1
        return aid

    def open_account(self, account_type: str, account_id: Optional[str] = None) -> Account:
        """
        Eröffnet ein neues Konto eines bestimmten Typs.
        Falls keine ID angegeben wird, generiert die Bank eine eindeutige ID.
        """
        key = account_type.lower()
        if key not in self._account_factories:
            raise ValueError(f"Unbekannter Kontotyp: {account_type}")
        if account_id is None:
            account_id = self._generate_account_id()
        account = self._account_factories[key](account_id)
        self._accounts[account_id] = account
        return account

    def _execute_transaction(
        self,
        from_account: Optional[Account],
        to_account: Optional[Account],
        amount: float,
        usage: str = ""
    ) -> None:
        """
        Führt eine einzelne Buchung aus, aktualisiert die beteiligten Kontosalden,
        trägt in die jeweiligen Journale ein und fügt den globalen Eintrag hinzu.
        """
        if amount <= 0:
            raise ValueError("Betrag muss positiv sein!")
        ts = self._get_timestamp()
        if from_account is not None:
            from_account.withdraw_amount(amount)
            from_account._record_transaction(
                TransactionEntry(ts, counterparty=to_account.id if to_account else None, amount=-amount, usage=usage)
            )
        if to_account is not None:
            to_account.deposit_amount(amount)
            to_account._record_transaction(
                TransactionEntry(ts, counterparty=from_account.id if from_account else None, amount=amount, usage=usage)
            )
        transaction = Transaction(
            timestamp=ts,
            from_account=from_account.id if from_account else None,
            to_account=to_account.id if to_account else None,
            amount=amount,
            usage=usage
        )
        self._journal.append(transaction)

    def deposit_cash(self, account_id: str, amount: float) -> bool:
        """
        Führt eine Bareinzahlung auf das angegebene Konto aus.
        """
        account = self._accounts.get(account_id)
        if account is None or not account.is_active:
            return False
        try:
            self._execute_transaction(None, account, amount, usage="Bareinzahlung")
            return True
        except Exception as e:
            print(f"Fehler bei Bareinzahlung: {e}")
            return False

    def transfer(self, debit_account_id: str, credit_account_id: str, amount: float, usage: str = "") -> bool:
        """
        Überträgt einen Betrag von einem Konto auf ein anderes.
        Falls Gebühren anfallen (z.B. bei Privatkonten), werden diese separat
        an das gebührenbezogene Bankkonto übertragen.
        """
        debit = self._accounts.get(debit_account_id)
        credit = self._accounts.get(credit_account_id)
        if debit is None or credit is None:
            print("Eines der angegebenen Konten existiert nicht.")
            return False
        if not (debit.is_active and credit.is_active):
            print("Eines der Konten ist nicht aktiv.")
            return False
        # Berechne ggf. anfallende Gebühren
        fee = debit.calculate_fee(amount)
        total = amount + fee
        if not debit.can_withdraw(total):
            print(f"Nicht genügend Deckung: {debit.balance:.2f} (erforderlich: {total:.2f})")
            return False

        try:
            # Hauptüberweisung
            self._execute_transaction(debit, credit, amount, usage)
            # Gebührenüberweisung, falls zutreffend
            if fee > 0:
                fee_usage = f"Gebühr: {usage}" if usage else "Gebühr"
                self._execute_transaction(debit, self._fee_account, fee, fee_usage)
            return True
        except Exception as e:
            print(f"Fehler bei der Überweisung: {e}")
            return False

    def get_balance(self, account_id: str) -> Optional[float]:
        account = self._accounts.get(account_id)
        if account is None:
            return None
        return account.balance

    def get_account_transactions(self, account_id: str, count: Optional[int] = None) -> Optional[List[TransactionEntry]]:
        account = self._accounts.get(account_id)
        if account is None:
            return None
        return account.get_transactions(count)

    def get_bank_transactions(self, count: Optional[int] = None) -> List[Transaction]:
        if count is None:
            return self._journal.copy()
        return self._journal[-count:]

    def close_account(self, account_id: str) -> bool:
        account = self._accounts.get(account_id)
        if account is None or not account.is_active:
            return False
        if account.balance != 0:
            print("Konto kann nur bei einem Saldo von 0 geschlossen werden.")
            return False
        return account.close()

    def list_accounts(self) -> List[Account]:
        """Liefert alle registrierten Konten zurück."""
        return list(self._accounts.values())


# -------------------------------
# Demonstration / Testprogramm
# -------------------------------

def main() -> None:
    bank = Bank()

    # Eröffne verschiedene Konten
    youth = bank.open_account("youth")
    savings = bank.open_account("savings")
    private = bank.open_account("private")

    print("Konten nach der Eröffnung:")
    for acct in bank.list_accounts():
        print(acct)

    # Bareinzahlung
    bank.deposit_cash(youth.id, 200.0)
    bank.deposit_cash(savings.id, 1000.0)
    bank.deposit_cash(private.id, 500.0)

    # Überweisung: Jugendkonto -> Sparkonto (gebührenfrei)
    bank.transfer(youth.id, savings.id, 50.0, usage="Überweisung 1")

    # Überweisung: Privatkonto -> Sparkonto (hier fallen Gebühren an)
    bank.transfer(private.id, savings.id, 100.0, usage="Überweisung 2")

    # Versuche eine Überweisung, die nicht gedeckt ist (z.B. Jugendkonto darf nicht überziehen)
    bank.transfer(youth.id, private.id, 500.0, usage="Überweisung 3")

    # Zeige aktuelle Salden
    print("\nAktuelle Salden:")
    for acct in bank.list_accounts():
        print(f"{acct.id}: {acct.balance:.2f}")

    # Zeige Transaktionsjournal eines Kontos (z.B. Sparkonto)
    print(f"\nBuchungen für Konto {savings.id}:")
    for entry in bank.get_account_transactions(savings.id):
        sign = "+" if entry.amount > 0 else ""
        print(f"  {entry.timestamp}: {sign}{entry.amount:.2f} (Gegenkonto: {entry.counterparty}) - {entry.usage}")

    # Zeige das globale Buchungsjournal (letzte 5 Buchungen)
    print("\nGlobales Buchungsjournal (letzte 5 Einträge):")
    for t in bank.get_bank_transactions(5):
        print(f"  {t.timestamp}: {t.from_account} -> {t.to_account} : {t.amount:.2f} - {t.usage}")

    # Versuche, ein Konto zu schließen
    print("\nKonto-Schliessungsversuch:")
    if bank.close_account(youth.id):
        print(f"Konto {youth.id} wurde geschlossen.")
    else:
        print(f"Konto {youth.id} konnte nicht geschlossen werden (Saldo: {youth.balance:.2f}).")


if __name__ == "__main__":
    main()
