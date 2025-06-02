from django import forms
from .models import Transaktion, Bankaccoount, Antrag
from django.contrib.auth.models import User


class FolderForm(forms.ModelForm):
    class Meta:
       model = Transaktion
       fields = ['Money_from', 'Money_to', 'Value']
       user = ''

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(FolderForm, self).__init__(*args, **kwargs)
       self.fields['Money_from'].queryset = Bankaccoount.objects.filter(User=user)
       self.user = self.fields['Money_from'].queryset

    def sendtransaktion(self):
        pass

from django.forms import ModelForm

class AntragsForm(forms.ModelForm):
   class Meta:
      model = Antrag
      fields = ['User', 'Nachname', 'Vorname', 'Antragswunsch', 'Kontotyp']
      user = ''
      
   def __init__(self, *args, **kwargs):
      user = kwargs.pop('user')
      super(AntragsForm, self).__init__(*args, **kwargs)
      self.fields['User'].queryset = User.objects.filter(username=user)
      self.user = self.fields['User'].queryset
