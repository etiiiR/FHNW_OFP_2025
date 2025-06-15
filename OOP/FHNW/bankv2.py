from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Callable, Dict


@dataclass(frozen=True)
class Transaction:
    """Repräsentiert eine vollständige Buchung in der Bank (Journal)."""
    timestamp: int
    from_account: Optional[str]  # None bei Bareinzahlungen
    to_account: Optional[str]
    amount: float              # immer positiv
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
# NEU: Das Strategie-Muster (Strategy Pattern)
# -------------------------------

class WithdrawalPolicy(ABC):
    """Abstrakte Strategie, die definiert, ob eine Abbuchung erlaubt ist."""
    @abstractmethod
    def can_withdraw(self, balance: float, amount: float) -> bool:
        ...

class FeePolicy(ABC):
    """Abstrakte Strategie, die definiert, wie Gebühren berechnet werden."""
    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        ...

# --- Konkrete Strategie-Implementierungen ---

class NoOverdraftPolicy(WithdrawalPolicy):
    """Strategie: Abbuchung nur bei ausreichendem Guthaben."""
    def can_withdraw(self, balance: float, amount: float) -> bool:
        return balance >= amount

class OverdraftPolicy(WithdrawalPolicy):
    """Strategie: Abbuchung erlaubt, solange das Dispolimit nicht überschritten wird."""
    def __init__(self, overdraft_limit: float):
        self._overdraft_limit = overdraft_limit

    def can_withdraw(self, balance: float, amount: float) -> bool:
        return (balance - amount) >= -self._overdraft_limit
        
class NoWithdrawalPolicy(WithdrawalPolicy):
    """Strategie: Abbuchungen sind niemals erlaubt."""
    def can_withdraw(self, balance: float, amount: float) -> bool:
        return False

class NoFeePolicy(FeePolicy):
    """Strategie: Es fallen keine Gebühren an."""
    def calculate_fee(self, amount: float) -> float:
        return 0.0

class PercentageFeePolicy(FeePolicy):
    """Strategie: Eine prozentuale Gebühr auf den Abbuchungsbetrag."""
    def __init__(self, fee_rate: float):
        self._fee_rate = fee_rate

    def calculate_fee(self, amount: float) -> float:
        return amount * self._fee_rate


class Account:
    """
    Eine generische Konto-Klasse.
    Die spezifischen Verhaltensweisen (Dispo, Gebühren) werden durch
    injizierte Strategie-Objekte gesteuert.
    """
    def __init__(self, account_id: str, withdrawal_policy: WithdrawalPolicy, fee_policy: FeePolicy) -> None:
        self._account_id: str = account_id
        self._withdrawal_policy = withdrawal_policy
        self._fee_policy = fee_policy
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

    def can_withdraw(self, amount: float) -> bool:
        # Delegation an das Strategie-Objekt
        return self._withdrawal_policy.can_withdraw(self._balance, amount)

    def calculate_fee(self, amount: float) -> float:
        # Delegation an das Strategie-Objekt
        return self._fee_policy.calculate_fee(amount)

    def __str__(self) -> str:
        status = "aktiv" if self._active else "geschlossen"
        policy_info = f"{type(self._withdrawal_policy).__name__}, {type(self._fee_policy).__name__}"
        return f"<Konto {self._account_id}: Saldo={self._balance:.2f} ({status}) - Policies: {policy_info}>"


class SavingsAccount(Account):
    """
    Spezialfall: Sparkonto. Erbt von der generischen Klasse und fügt
    zusätzliche Funktionalität hinzu (Verzinsung).
    Die Basis-Policys werden an den Konstruktor der Elternklasse übergeben.
    """
    def __init__(self, account_id: str, interest_rate: float = 0.01) -> None:
        # Initialisiere die Elternklasse mit den passenden Strategien
        super().__init__(account_id, NoOverdraftPolicy(), NoFeePolicy())
        self.interest_rate: float = interest_rate

    def apply_interest(self) -> None:
        """Zinsgutschrift – hier als Beispiel: Das Guthaben wird verzinst."""
        interest = self._balance * self.interest_rate
        self.deposit_amount(interest)
        # Eine Buchung im Konto-Journal könnte hier ebenfalls erfolgen.


# -------------------------------
# Die Bank (mit angepasster Konto-Factory)
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

        # Konto-Factory: Hier werden die Konten mit den passenden Strategien konfiguriert
        self._account_factories: Dict[str, Callable[[str], Account]] = {}
        self.register_account_type(
            "youth",
            lambda aid: Account(aid, NoOverdraftPolicy(), NoFeePolicy())
        )
        self.register_account_type(
            "savings",
            lambda aid: SavingsAccount(aid, interest_rate=0.01) # Nutzt die spezielle Subklasse
        )
        self.register_account_type(
            "private",
            lambda aid: Account(aid, OverdraftPolicy(500.0), PercentageFeePolicy(0.01))
        )
        
        # Das Gebührenkonto der Bank wird ebenfalls mit Strategien konfiguriert
        self._fee_account = Account("FEE-0001", NoWithdrawalPolicy(), NoFeePolicy())
        self._accounts[self._fee_account.id] = self._fee_account

    def _get_timestamp(self) -> int:
        self._current_timestamp += 1
        return self._current_timestamp

    def register_account_type(self, type_name: str, factory: Callable[[str], Account]) -> None:
        self._account_factories[type_name.lower()] = factory

    def _generate_account_id(self) -> str:
        aid = f"A{self._account_id_counter:06d}"
        self._account_id_counter += 1
        return aid

    def open_account(self, account_type: str, account_id: Optional[str] = None) -> Account:
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
        debit = self._accounts.get(debit_account_id)
        credit = self._accounts.get(credit_account_id)
        if debit is None or credit is None:
            print("Eines der angegebenen Konten existiert nicht.")
            return False
        if not (debit.is_active and credit.is_active):
            print("Eines der Konten ist nicht aktiv.")
            return False
        fee = debit.calculate_fee(amount)
        total = amount + fee
        if not debit.can_withdraw(total):
            print(f"Nicht genügend Deckung: {debit.balance:.2f} (erforderlich: {total:.2f})")
            return False

        try:
            self._execute_transaction(debit, credit, amount, usage)
            if fee > 0:
                fee_usage = f"Gebühr: {usage}" if usage else "Gebühr"
                self._execute_transaction(debit, self._fee_account, fee, fee_usage)
            return True
        except Exception as e:
            print(f"Fehler bei der Überweisung: {e}")
            return False

    def get_balance(self, account_id: str) -> Optional[float]:
        account = self._accounts.get(account_id)
        return account.balance if account else None

    def get_account_transactions(self, account_id: str, count: Optional[int] = None) -> Optional[List[TransactionEntry]]:
        account = self._accounts.get(account_id)
        return account.get_transactions(count) if account else None

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
        return list(self._accounts.values())

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
        # Kleiner Schönheitsfehler: das Fee-Account wird hier auch gelistet.
        if acct.id != "FEE-0001":
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