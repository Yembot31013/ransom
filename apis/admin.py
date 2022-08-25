from django.contrib import admin
from .models import Profile, How_To_Pay

class RansomAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'token', "token_id", 'sender_id', 'registered_owner', "time_Zone", "registered_organization", "is_verified", "decrypted"
            ),
        }),
        ('OS Info', {
            "classes": ('collapse',),
            "fields": (
                'os_name', 'os_version', 'os_manufacturer', "os_configuration", "os_build_type", "product_iD", "original_Install_Date", "windows_Directory"
            ),
        }),
        ('System Info', {
            "classes": ('collapse',),
            "fields": (
                 "system_Boot_Time", "system_Manufacturer", "system_Model", "system_Type","system_Directory"
            ),
        }),
        ('others', {
            "classes": ('collapse',),
            "fields": (
                'host_name', "processor", "bios_Version", "system_Locale", "input_Locale", "total_Physical_Memory", "available_Physical_Memory"
            ),
        }),
    )

admin.site.register(Profile, RansomAdmin)
admin.site.register(How_To_Pay)
