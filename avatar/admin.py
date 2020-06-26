from django.contrib import admin
from avatar.models import Avatar


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('avatar',)


admin.site.register(Avatar, AvatarAdmin)
