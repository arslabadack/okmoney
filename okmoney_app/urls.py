from django.urls import path

from . import views

urlpatterns = [
    # inclua aqui as rotas
    path('index.html', views.index, name='index'),  # index é o template html
    path('money_in.html', views.MoneyIn.as_view(), name='Entradas'),
    path('money_out.html', views.money_out, name='Saidas'),
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
