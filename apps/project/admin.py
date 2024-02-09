from django.contrib import admin

from apps.project.models import BigBanner,LongBanner,SmallBanner,SquareBanner
# Register your models here.
admin.site.register(BigBanner)
admin.site.register(LongBanner)
admin.site.register(SmallBanner)
admin.site.register(SquareBanner)