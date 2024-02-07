from django.shortcuts import render

from apps.about.models import About,Skills,Path
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    skills = Skills.objects.all()
    path = Path.objects.all()
    return render(request, 'about/about.html', locals())