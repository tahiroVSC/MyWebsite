from django.shortcuts import render

from apps.offering.models import Offernig
# Create your views here.
def offering(request):
    offering = Offernig.objects.all()
    return render(request, 'offering/offering.html', locals())