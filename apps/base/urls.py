from django.urls import path

from apps.base.views import index
from apps.about.views import about
from apps.article.views import article
from apps.contact.views import contact
from apps.error.views import error
from apps.offering.views import offering
from apps.project.views import project

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('article/', article, name='article'),
    path('contact/', contact, name='contact'),
    path('error/', error, name='error'),
    path('offering/', offering, name='offering'),
    path('project/', project, name='project'),
]

