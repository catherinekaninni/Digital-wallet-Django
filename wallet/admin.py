from django.contrib import admin
from .models import Customer,Currency, Receipt,Wallet,Account,Transaction,Card,Thirdparty,Notification,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_Fields=("first_name","last_name")
admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("amount", "symbol", "country_of_origin")
    search_fields = ("country_of_origin", "symbol")
admin.site.register(Currency, CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("customer", "balance", "currency")
    search_fields = ("customer", "status")
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_name", "account_type", "wallet")
    search_fields = ("account_name", "account_type")
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction)

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_type", "card_name")
    search_fields = (" card_type","card_name")
admin.site.register(Card, CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("name","phone_number",)
    search_fields = ("name","phone_number")
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("name","receipt")
    search_fields = ("name","receipt")
admin.site.register(Notification,NotificationAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("guarantor","loan_type")
    search_fields = ("guarantor","loan_type")
admin.site.register(Loan,LoanAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_file","receipt_type")
    search_fields = ("receipt_file","receipt_type")
admin.site.register(Receipt,ReceiptAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("gender","date_and_time")
    search_fields = ("gender","date_and_time")
admin.site.register(Reward,RewardAdmin)
