from . import forms
from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        total_in = models.MoneyIn.objects.all().aggregate(Sum('value'))[
            'value__sum']
        total_out = models.MoneyOut.objects.all().aggregate(Sum('value'))[
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

        context = {
            'total_in': total_in,
            'total_out': total_out,

            'total_in_future': total_in_future,
            'total_out_future': total_out_future,

            'future_releases': models.Future.objects.all()
        }

        self.render = render(
            self.request, self.template_name, context)

    def get(self, *args, **kwargs):
        return self.render

    def post(self, *args, **kwargs):
        pass


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
            'Entrada financeira registrada',
        )

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
        messages.success(self.request, 'Lançamento atualizado')

        return redirect('money_list', pk=self.release.pk)


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
            # registered_by=self.request.user
        )
        new_money_out.save()

        messages.success(
            self.request,
            'Saída financeira registrada',
        )

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
        messages.success(self.request, 'Lançamento atualizado')

        return redirect('money_list', pk=self.release.pk)


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
        messages.success(self.request, 'Lançamento editado')

        return redirect('future', pk=self.release.pk)


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

#         username = self.request.POST.get('username')
#         password = self.request.POST.get('password')

#         user = authenticate(self.request, username=username, password=password)

#         if not user:
#             messages.error(
#                 self.request,
#                 'Nome de usuário ou senha incorretos!',
#             )

#             return redirect('login')
#         else:
#             login(self.request, user)

#         return redirect('index')


# class Logout(View):
#     def get(self, *args, **kwargs):
#         logout(self.request)
#         return redirect('login')
