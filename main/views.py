from django.shortcuts import render,redirect
from .forms import PDFUploadForm
# Create your views here.

def main(request):
  return render(request,'main.html')

def model_form_upload_single(request):
  if request.method == 'POST':
      form = PDFUploadForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('main:main')
  else:
      form = PDFUploadForm()
  return render(request, 'pdf_upload_single.html', {
      'form': form
  })

def model_form_upload_multiple(request):
  if request.method == 'POST':
      form = PDFUploadForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('main:main')
  else:
      form = PDFUploadForm()
  return render(request, 'pdf_upload_multiple.html', {
      'form': form
  })