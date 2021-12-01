from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.main, name='main'),
    path('pdf_upload',views.model_form_upload,name='pdf_upload')
]