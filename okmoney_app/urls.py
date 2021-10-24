from django.urls import path

from . import views

urlpatterns = [
    # inclua aqui as rotas
    path('', views.index, name='index'),  # index é o template html
    path('money_in/', views.money_in, name='Entradas'),
    # path('money_out/', views.money_out, name='Saidas'),
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
