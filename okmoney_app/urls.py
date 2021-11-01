from django.urls import path

from . import views

urlpatterns = [
    # inclua aqui as rotas
    path('', views.Index.as_view(), name='index'),
    path('money_status.html', views.MoneyReleases.as_view(), name='releases'),
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
