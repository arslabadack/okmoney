from django.views import View
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


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

            return redirect('users:login')
        else:
            login(self.request, user)

        return redirect('index')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('users:login')


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
