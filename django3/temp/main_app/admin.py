from django.contrib import admin
from main_app.models import Customer, Profession, ContactInfo, Hobbies

@admin.register(ContactInfo)
class AdminContactInfo(admin.ModelAdmin):
    list_display = ('address', 'phone')

@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'profession')
    list_display_links = ('full_name',)
    #запятая ставится после 1-го элемента, чтобы видело что tuple
    search_fields = ('firstname', 'lastname')
    list_filter = ('profession',)

    def full_name(self, obj):
        return f'{obj.firstname}  {obj.lastname}'

# admin.site.register(Customer)
admin.site.register(Profession)
# admin.site.register(ContactInfo)
admin.site.register(Hobbies)

