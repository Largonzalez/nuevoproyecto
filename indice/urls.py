

# from django.urls import admin

from django.urls import path, include


urlpatterns = [
    path ('', include("indice.urls")),
    # path('admin/', admin.site.urls),
]
