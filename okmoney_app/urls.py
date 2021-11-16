from django.urls import path


from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('money_in/', views.MoneyIn.as_view(), name='moneyin'),
    path('money_in/<int:pk>', views.MoneyInEdit.as_view(), name='money_in_edit'),
    path('money_out/', views.MoneyOut.as_view(), name='moneyout'),
    path('money_out/<int:pk>', views.MoneyOutEdit.as_view(), name='money_out_edit'),
    path('money_list/', views.MoneyList.as_view(), name='list'),
    path('future/', views.Future.as_view(), name='future'),
    path('future/<int:pk>', views.FutureEdit.as_view(), name='future_edit'),
]
