from django.shortcuts import render

from apps.about.models import About
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    return render(request, 'about/about.html', locals())