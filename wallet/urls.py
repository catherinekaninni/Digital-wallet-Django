from urllib.request import url2pathname
from django.urls import path

from wallet.models import Card
# from .views import register_customer 
from . import views
urlpatterns=[
    path("register/", views.register_customer,name="registration"),
    path("currency/", views.register_currency,name="registration"),
    path("wallet/",views.register_wallet, name="registration"),
    path("account/",views.register_account,name="registration"),
    path("transaction/",views.register_transaction,name="registration"),
    path("card/",views.register_card,name="registration"),
    path("notification/",views.register_notification,name="registration"),
    path("receipt/",views.register_receipt,name="registration"),
    path("loan/",views.register_loan,name="registration"),
    path("reward/",views.register_reward,name="registration"),
    path("thirdparty/", views.register_thirdparty,name="registration")
    ]


