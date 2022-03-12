
from django.urls import path
from.views import nuevo_curso1


urlpatterns = [
    path('nuevo/', nuevo_curso1, name='nuevo_curso1'),

]



