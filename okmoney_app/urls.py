from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('reminders', views.RemindersViewSet)

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('money_in/', views.MoneyIn.as_view(), name='moneyin'),
    path('money_in/<int:pk>', views.MoneyInEdit.as_view(), name='money_in_edit'),
    path('money_out/', views.MoneyOut.as_view(), name='moneyout'),
    path('money_out/<int:pk>', views.MoneyOutEdit.as_view(), name='money_out_edit'),
    path('money_list/', views.MoneyList.as_view(), name='list'),
    path('money_list_del_in/<int:pk>',
         views.MoneyInDelete.as_view(), name='money_in_delete'),
    path('money_list_del_out/<int:pk>',
         views.MoneyOutDelete.as_view(), name='money_out_delete'),
    path('future/', views.Future.as_view(), name='future'),
    path('future_edit/<int:pk>', views.FutureEdit.as_view(), name='future_edit'),
    path('future/<int:pk>', views.FutureDelete.as_view(), name='future_delete'),
    path('reminders/<int:pk>', views.RemindersDelete.as_view(),
         name='reminders_delete'),

]
