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


def index(request):
 #   form = ContatoForm(request.POST or None)

    # if str(request.method) == 'POST':
    #     if form.is_valid():
    #         nome = form.cleaned_data['nome']
    #         email = form.cleaned_data['email']
    #         mensagem = form.cleaned_data['mensagem']

    #         print('Mensagem enviada')
    #         print(f'Nome: {nome}')

    #         messages.success(request, 'Mensagem enviada com sucesso!')
    #         form = ContatoForm()
    #     else:
    #         messages.error(request, 'Formulário inválido')

    # context = {
    #     'form': form,
    # }
    #    produtos = Produto.objects.all()
    #
    #    context = {
    #        'produtos': produtos
    #    }
    return render(request, 'index.html')  # , context)


class MoneyIn(View):
    template_name = 'money_in.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        context = {
            'money_in_form': forms.MoneyInForm(
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
            data=self.money_in_form.cleaned_data.get('data'),
            categoria=self.money_in_form.cleaned_data.get('categoria'),
            valor=self.money_in_form.cleaned_data.get('valor'),
            observacao=self.money_in_form.cleaned_data.get('observacao'),
            # registered_by=self.request.user
        )

        new_money_in.save()

        messages.success(
            self.request,
            'Entrada financeira registrada',
        )

        return redirect('okmoney_app:index')


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


def money_out(request):
    return render(request, 'money_out.html')

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
