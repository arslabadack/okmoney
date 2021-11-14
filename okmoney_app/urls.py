from django.urls import path


from . import views


urlpatterns = [
    # inclua aqui as rotas
    path('', views.Index.as_view(), name='index'),
    path('money_in/', views.MoneyIn.as_view(), name='moneyin'),
    path('money_in/', views.MoneyInEdit.as_view(), name='money_in_edit'),
    path('money_out/', views.MoneyOut.as_view(), name='moneyout'),
    path('money_list/', views.MoneyList.as_view(), name='list'),
    path('future/', views.Future.as_view(), name='future'),
    path('future_edit/', views.FutureEdit.as_view(), name='future_edit'),
    path('login/', views.Login.as_view(), name='login'),
    # path('register/', views.Register.as_view, name='register'),
    # path(nome do caminho da pag html ex:'pedidos/', pedido,  name='pedido'),
]
