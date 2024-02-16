from django.shortcuts import render

# Create your views here.
def error(request, exception):
    return render(request, 'error/error.html', status=404)