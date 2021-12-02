from django.urls import path
# from django.conf import settings 
# from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.main, name='main'),
    path('result',views.pdf_result,name='pdf_result'),
    path('pdf_upload_single',views.model_form_upload,name='pdf_upload_single'),
    path('pdf_upload_multiple',views.model_form_upload,name='pdf_upload_multiple'),
]