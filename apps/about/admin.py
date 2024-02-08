from django.contrib import admin

from apps.about.models import About,Skills,Path,Education
# Register your models here.
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Path)
admin.site.register(Education)