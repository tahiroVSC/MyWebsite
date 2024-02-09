from django.shortcuts import render

from apps.project.models import LongBanner,SmallBanner,BigBanner,SquareBanner
# Create your views here.
def project(request):
    long = LongBanner.objects.all()
    small = SmallBanner.objects.all()
    big = BigBanner.objects.all()
    square = SquareBanner.objects.all()
    return render(request, 'project/project.html', locals())