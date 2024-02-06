from django.shortcuts import render

from apps.base.models import Index,Slide
# Create your views here.
def index(request):
    index = Index.objects.latest('id')
    slide = Slide.objects.all()
    return render (request, 'base/index.html', locals())