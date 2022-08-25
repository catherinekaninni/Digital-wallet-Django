from django.contrib import admin
from .models import Customer,Currency, Receipt,Wallet,Account,Transaction,Card,Thirdparty,Notification,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_Fields=("first_name","last_name")
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Loan)
admin.site.register(Receipt)
admin.site.register(Reward)
