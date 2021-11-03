from . import forms
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum


class Index(View):
    template_name = 'index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'total_in': models.MoneyReleases.objects.filter(operation='entrada').aggregate(total=Sum('value')).get('total'),
            'total_out': models.MoneyReleases.objects.filter(operation='saida').aggregate(total=Sum('value')).get('total'),
            'total_difference': models.MoneyReleases.objects.filter(operation='entrada').aggregate(total=Sum('value')).get('total') - models.MoneyReleases.objects.filter(operation='saida').aggregate(total=Sum('value')).get('total'),
        }

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        pass


class MoneyReleases(View):
    template_name = 'money_releases.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'money_form': forms.MoneyForm(
                data=self.request.POST or None
            ),
        }

        self.money_form = context['money_form']

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        if not self.money_form.is_valid():
            return self.render

        new_money = models.MoneyReleases(
            date=self.money_form.cleaned_data.get('date'),
            operation=self.money_form.cleaned_data.get('operation'),
            reason=self.money_form.cleaned_data.get('reason'),
            place=self.money_form.cleaned_data.get('place'),
            value=self.money_form.cleaned_data.get('value'),
            payment_method=self.money_form.cleaned_data.get(
                'payment_method'),
            observation=self.money_form.cleaned_data.get('observation'),
            # registered_by=self.request.user
        )
        new_money.save()

        messages.success(
            self.request,
            'Lançamento financeiro registrado',
        )

        return redirect('index')


class MoneyList(ListView):
    template_name = 'money_releases.html'
    context_object_name = 'money_list'
    paginate_by = 20
    model = models.MoneyReleases

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MoneyDetails(View):
    template_name = 'money_releases.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
# TODO: duvida se é realmente self.money_status
        self.money_releases = get_object_or_404(
            models.MoneyReleases, pk=self.kwargs.get('pk'))

        context = {
            'money_releases': self.money_releases,
        }

        self.render = render(self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        pass


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


# class Login(View):
#     def get(self, *args, **kwargs):
#         return render(self.request, 'login.html')

#     def post(self, *args, **kwargs):
#         '''
#         username = self.request.POST.get('username')
#         password = self.request.POST.get('password')
#         user = authenticate(self.request, username=username, password=password)
#         if not user:

#             messages.error(
#                 self.request,
#                 'CPF ou senha incorretos!',
#             )

#             return redirect('donations:login')
#         else:
#             login(self.request, user)
#         next = self.request.GET.get('next')
#         if next is None or next == '/':
#             if tecnico.is_gestor:
#                 return redirect('tecnicos:index_gestor')
#             return redirect('tecnicos:index')

#         return redirect(self.request.GET.get('next'))
#         '''


# class Logout(View):
#     def get(self, *args, **kwargs):
#         logout(self.request)
#         return redirect(self.request.META.get('HTTP_REFERER'))
