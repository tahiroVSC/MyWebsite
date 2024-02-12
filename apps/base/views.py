from django.shortcuts import render

from apps.base.models import Index,Slide,ServicesOffering
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    slide = Slide.objects.all()
    servicesoffering = ServicesOffering.objects.all()
    return render (request, 'base/index.html', locals())