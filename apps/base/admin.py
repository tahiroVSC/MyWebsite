from django.contrib import admin
from django.contrib.auth.models import User,Group

from apps.base.models import Index,Slide
# Register your models here.

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)
    

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
  

admin.site.register(Index)
admin.site.register(Slide)

admin.site.unregister(User)
admin.site.unregister(Group)