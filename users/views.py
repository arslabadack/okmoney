from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'templates/register.html'


class Login(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')

    def post(self, *args, **kwargs):

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(self.request, username=username, password=password)

        if not user:
            messages.error(
                self.request,
                'Nome de usuário ou senha incorretos!',
            )

            return redirect('templates/login')
        else:
            login(self.request, user)

        return redirect('index')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('templates/login')
