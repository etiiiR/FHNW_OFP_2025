from lib2to3.fixes.fix_input import context
import logging
#from fnmatch import filter
from django.core.exceptions import ValidationError
from .forms import FolderForm, AntragsForm
from .models import Bankaccoount, Transaktion
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.context_processors import request
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, \
    UpdateView
from django.views.generic.list import ListView
from django.http import Http404 
from django.contrib.auth.models import User
logger = logging.getLogger(__name__)

class abheben(ListView):
    model = Bankaccoount
    template_name = 'user_abheben.html'
    context_object_name = 'all_bancaccounts_user'

    def get_queryset(self):
        return Bankaccoount.objects.filter(User_id=self.kwargs['pk'])


    



@method_decorator(login_required, name='dispatch')
class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'bankaccount.can_see_bankaccount' 
    model = Bankaccoount
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'object_list'  # Default: object_list
    paginate_by = 10
    queryset = Bankaccoount.objects.all()
    logger.info("Log of Queryset in UserlistView %s", queryset)



@method_decorator(login_required, name='dispatch')
class UserchangeListView(PermissionRequiredMixin, ListView):
    permission_required = 'bankaccount.can_change_bankaccount' 
    model = Bankaccoount
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'object_list'  # Default: object_list
    paginate_by = 10
    queryset = Bankaccoount.objects.all()
    logger.info("Log of Queryset in UserchangeListView %s", queryset)
    
@method_decorator(login_required, name='dispatch')
class AccountCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'bankaccount.can_change_bankaccount' 
    model = Bankaccoount
    fields = ['balance', 'User']
    logger.info("Account Created", fields)

@method_decorator(login_required, name='dispatch')
class SignUp(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'bankaccount.can_bankeröffnung' 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@method_decorator(login_required, name='dispatch')
class Friendspay(CreateView):
    form_class = FolderForm
    accounts = Bankaccoount.objects.all().values('id')

    def get_form_kwargs(self):
        kwargs = super(Friendspay, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        print("ssss")
        if form.is_valid():
            data = form.cleaned_data
            my_form_obj = form.save(commit=True)
            #use dir()
            amount = my_form_obj.Value.amount
            id_money_from = my_form_obj.Money_from_id
            id_money_to = my_form_obj.Money_to_id
            account_from = Bankaccoount.objects.get(id=id_money_from)
            account_to = Bankaccoount.objects.get(id=id_money_to)

            if(id_money_from == id_money_to):
                logger.error(" Error Account %s %s", account_from, account_to)
                return HttpResponseRedirect('same_account/')
            else:
                if (account_from.balance.amount >= amount ):
                    konto_bezahlt = Bankaccoount.objects.filter(id=id_money_from).update(balance = account_from.balance.amount - amount)
                    konto_gezahlt = Bankaccoount.objects.filter(id=id_money_to).update(balance= account_to.balance.amount + amount)
                else:
                    logger.error(" Error Balance %s", account_from)
                    return HttpResponseRedirect('error_blance/')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RequestforAccount(CreateView):
    form_class = AntragsForm
    accounts = User.objects.all().values('id')

    def get_form_kwargs(self):
        kwargs = super(RequestforAccount, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs