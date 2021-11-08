from django.urls import path

from . import views

urlpatterns = [
    # inclua aqui as rotas
    path('', views.Index.as_view(), name='index'),
    path('money_in.html', views.MoneyIn.as_view(), name='moneyin'),
    path('money_out.html', views.MoneyOut.as_view(), name='moneyout'),
    path('money_list.html', views.MoneyInList.as_view(), name='list'),
    # path('money_details.html', views.MoneyDetails.as_view(), name='details'),
    path('login/', views.Login.as_view(), name='login'),
    # path('register/', register, name='register'),
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
