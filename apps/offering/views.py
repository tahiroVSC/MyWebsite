from django.shortcuts import render

# Create your views here.
def offering(request):
    return render(request, 'offering/offering.html', locals())