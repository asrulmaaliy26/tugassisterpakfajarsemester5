
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
]
