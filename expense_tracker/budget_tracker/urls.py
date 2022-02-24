import imp
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),
    # path('new-transaction/', TransactionCreate.as_view(), name='create'),
    path('create/', TransactionCreateView.as_view(), name='create'),
    path('', TransactionsView.as_view(), name='transactions'),
    path('update/<int:pk>', TransactionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TransactionDeleteView.as_view(), name='delete')
]