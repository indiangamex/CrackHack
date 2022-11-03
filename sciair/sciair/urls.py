from django.contrib import admin
from django.urls import include, path
admin.site.site_header = "Crack-Hack Admin"
admin.site.site_title = "Crack-Hack Admin Portal"
admin.site.index_title = "Welcome to Crack-Hack Researcher Portal"
urlpatterns = [
    path('', include('cityair.urls')),
    path('admin/', admin.site.urls),
]