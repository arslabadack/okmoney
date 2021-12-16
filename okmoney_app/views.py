import logging
import datetime
from . import forms
from . import models
from . import serializers
from django.db.models import Sum
from django.template import loader
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.http.response import HttpResponse
from rest_framework.response import Response
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render, redirect, get_object_or_404

logger = logging.getLogger(__name__)


class RemindersViewSet(viewsets.ModelViewSet):
    queryset = models.Reminders.objects.all()
    serializer_class = serializers.RemindersSerializer


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        initial_date = self.request.GET.get('initial_date')
        final_date = self.request.GET.get('final_date')
        
        try:
            token, created = Token.objects.get_or_create(user=self.request.user)
        except:
            return redirect('login')


        if not initial_date:
            initial_date = datetime.date.today()-datetime.timedelta(days=365)
        if not final_date:
            final_date = datetime.date.today()

        total_in = models.MoneyIn.objects.filter(date__range=[initial_date, final_date]).aggregate(Sum('value'))[
            'value__sum']
        total_out = models.MoneyOut.objects.filter(date__range=[initial_date, final_date]).aggregate(Sum('value'))[
            'value__sum']

        total_in_future = models.Future.objects.filter(
            category='entrada').aggregate(total=Sum('value')).get('total')
        total_out_future = models.Future.objects.filter(
            category='saida').aggregate(total=Sum('value')).get('total')

        if total_in == None and total_out == None:
            total_in = 0
            total_out = 0
        elif total_in == None:
            total_in = 0
        elif total_out == None:
            total_out = 0

        if total_in_future == None and total_out_future == None:
            total_in_future = 0
            total_out_future = 0
        elif total_in_future == None:
            total_in_future = 0
        elif total_out_future == None:
            total_out_future = 0

        current_in = models.MoneyIn.objects.all().aggregate(Sum('value'))[
            'value__sum']
        current_out = models.MoneyOut.objects.all().aggregate(Sum('value'))[
            'value__sum']

        if current_in == None and current_out == None:
            current_in = 0
            current_out = 0
        elif current_in == None:
            current_in = 0
        elif current_out == None:
            current_out = 0

        current_balance = current_in - current_out

        total_expenses = [
            {'category': 'total_health', 'amount': float(models.MoneyOut.objects.filter(
                category='saude', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_food', 'amount': float(models.MoneyOut.objects.filter(
                category='alimentacao', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_lazer', 'amount': float(models.MoneyOut.objects.filter(
                category='lazer', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_entertainment', 'amount': float(models.MoneyOut.objects.filter(
                category='entretenimento', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_energywater', 'amount': float(models.MoneyOut.objects.filter(
                category='energiasaneamento', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_taxes', 'amount': float(models.MoneyOut.objects.filter(
                category='impostos', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_fuel', 'amount': float(models.MoneyOut.objects.filter(
                category='combustivel', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)},
            {'category': 'total_other', 'amount': float(models.MoneyOut.objects.filter(
                category='outros', date__range=[initial_date, final_date]).aggregate(total=Sum('value')).get('total') or 0.0)}
        ]

        context = {
            'total_in': total_in,
            'total_out': total_out,
            'current_balance': current_balance,

            'token': token.key,

            'initial_date': initial_date,
            'final_date': final_date,

            'total_in_future': total_in_future,
            'total_out_future': total_out_future,

            'future_releases': models.Future.objects.all(),

            'total_expenses': total_expenses,

            'reminders_form': forms.RemindersModelForm(self.request.POST or None),
            'all_reminders': models.Reminders.objects.all(),
        }

        self.reminders_form = context['reminders_form']
        self.render = render(
            self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.reminders_form.is_valid:
            return self.render

        new_reminder = models.Reminders(
            author=self.request.user,
            content=self.reminders_form.cleaned_data.get('content'),
        )
        new_reminder.save()

        return redirect('index')


class MoneyIn(LoginRequiredMixin, TemplateView):
    template_name = 'money_in.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'money_in_form': forms.MoneyInModelForm(
                data=self.request.POST or None
            ),
        }

        self.money_in_form = context['money_in_form']

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.money_in_form.is_valid():
            return self.render

        new_money_in = models.MoneyIn(
            author=self.request.user,
            date=self.money_in_form.cleaned_data.get('date'),
            category=self.money_in_form.cleaned_data.get('category'),
            value=self.money_in_form.cleaned_data.get('value'),
            observation=self.money_in_form.cleaned_data.get('observation'),
        )

        new_money_in.save()

        messages.success(
            self.request,
            'Entrada Financeira Registrada com Sucesso!'
        )

        logger.info(
            f'Entrada financeira registrada por {(self.request.user.username)}')
        return redirect('index')


class MoneyInEdit(LoginRequiredMixin, TemplateView):
    template_name = 'money_in.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.release = get_object_or_404(
            models.MoneyIn, pk=self.kwargs.get('pk'))

        context = {
            'relese': self.release,
            'money_in_form': forms.MoneyInModelForm(
                data=self.request.POST or None,
                instance=self.release,
            ),
        }

        self.money_in_form = context['money_in_form']
        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.money_in_form.is_valid():
            return self.render

        self.release.save()
        messages.info(self.request, 'Entrada Financeira Editada com Sucesso!')

        logger.warning('Uma alteração foi realizada no lançamento financeiro')
        return redirect('list')


class MoneyInDelete(LoginRequiredMixin, TemplateView):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.money_in_object = get_object_or_404(
            models.MoneyIn, pk=self.kwargs.get('pk'))

        self.money_in_object.delete()
        messages.warning(
            self.request, 'Entrada Financeira Excluída com Sucesso!')

    def get(self, *args, **kwargs):
        logger.warning(
            'Um lançamento financeiro foi deletado do banco de dados')
        return redirect('list')


class MoneyOut(LoginRequiredMixin, TemplateView):
    template_name = 'money_out.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'money_out_form': forms.MoneyOutModelForm(
                data=self.request.POST or None
            ),
        }

        self.money_out_form = context['money_out_form']

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.money_out_form.is_valid():
            return self.render

        new_money_out = models.MoneyOut(
            author=self.request.user,
            date=self.money_out_form.cleaned_data.get('date'),
            category=self.money_out_form.cleaned_data.get('category'),
            reason=self.money_out_form.cleaned_data.get('reason'),
            place=self.money_out_form.cleaned_data.get('place'),
            value=self.money_out_form.cleaned_data.get('value'),
            payment_method=self.money_out_form.cleaned_data.get(
                'payment_method'),
            observation=self.money_out_form.cleaned_data.get('observation'),
        )
        new_money_out.save()

        messages.success(
            self.request,
            'Saída Financeira Registrada com Sucesso!',
        )
        logger.info(
            f'Saída financeira registrada por {(self.request.user.username)}')
        return redirect('index')


class MoneyOutEdit(LoginRequiredMixin, TemplateView):
    template_name = 'money_out.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.release = get_object_or_404(
            models.MoneyOut, pk=self.kwargs.get('pk'))

        context = {
            'relese': self.release,
            'money_out_form': forms.MoneyOutModelForm(
                data=self.request.POST or None,
                instance=self.release,
            ),
        }

        self.money_out_form = context['money_out_form']
        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.money_out_form.is_valid():
            return self.render

        self.release.save()
        messages.info(self.request, 'Saída Financeira Editada com Sucesso!')
        logger.warning('Uma alteração foi realizada no lançamento financeiro')
        return redirect('list')


class MoneyOutDelete(LoginRequiredMixin, TemplateView):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.money_out_object = get_object_or_404(
            models.MoneyOut, pk=self.kwargs.get('pk'))

        self.money_out_object.delete()
        messages.warning(
            self.request, 'Saída Financeira Excluída com Sucesso!')

    def get(self, *args, **kwargs):
        logger.warning(
            'Um lançamento financeiro foi deletado do banco de dados')
        return redirect('list')


class MoneyList(LoginRequiredMixin, ListView):
    template_name = 'money_list.html'
    context_object_name = 'money_in_list'
    paginate_by = 10
    model = models.MoneyIn

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['money_out_list'] = models.MoneyOut.objects.all()
        return context


class Future(LoginRequiredMixin, TemplateView):
    template_name = 'future.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'future_form': forms.FutureModelForm(
                data=self.request.POST or None
            ),
            'future_releases': models.Future.objects.all(),
        }

        self.future_form = context['future_form']

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.future_form.is_valid():
            return self.render

        new_release = models.Future(
            author=self.request.user,
            release_date=self.future_form.cleaned_data.get('release_date'),
            receiving_date=self.future_form.cleaned_data.get(
                'receiving_date'),
            category=self.future_form.cleaned_data.get('category'),
            reason=self.future_form.cleaned_data.get('reason'),
            value=self.future_form.cleaned_data.get('value'),
        )
        new_release.save()
        messages.success(
            self.request,
            'Lançamento Futuro Registrado com Sucesso!',
        )
        logger.info(
            f'Lançamento futuro registrado por {(self.request.user.username)}')
        return redirect('future')


class FutureEdit(LoginRequiredMixin, TemplateView):
    template_name = 'future_edit.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.release = get_object_or_404(
            models.Future, pk=self.kwargs.get('pk'))

        context = {
            'release': self.release,
            'future_form': forms.FutureModelForm(
                data=self.request.POST or None,
                instance=self.release,
            ),
        }

        self.future_form = context['future_form']
        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.future_form.is_valid():
            return self.render

        self.release.save()
        messages.success(
            self.request, 'Lançamento Futuro Editado com Sucesso!')
        logger.warning('Uma alteração foi realizada no lançamento financeiro')
        return redirect('future')


class FutureDelete(LoginRequiredMixin, TemplateView):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.future_object = get_object_or_404(
            models.Future, pk=self.kwargs.get('pk'))

        self.future_object.delete()
        messages.warning(
            self.request, 'Lançamento Futuro Excluído com Sucesso!')

    def get(self, *args, **kwargs):
        logger.warning(
            'Um lançamento financeiro foi deletado do banco de dados')
        return redirect('future')


class RemindersDelete(LoginRequiredMixin, TemplateView):
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.reminder_object = get_object_or_404(
            models.Reminders, pk=self.kwargs.get('pk'))

        self.reminder_object.delete()

    def get(self, *args, **kwargs):
        return redirect('index')


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)
