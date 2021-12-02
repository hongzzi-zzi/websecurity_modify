from django import forms
from django.db import models
from .models import PDFdocuments

class PDFUploadForm(forms.ModelForm):
  class Meta:
    model=PDFdocuments
    fields = ( 'document', )