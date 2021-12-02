from django.shortcuts import render,redirect
from .forms import PDFUploadForm
import pickle
import pandas as pd
import numpy as np
from util import libsvm_to_csv, parser
# Create your views here.

def main(request):
  return render(request,'main.html')

def model_form_upload_single(request):
  if request.method == 'POST':
      form = PDFUploadForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('main:pdf_result')
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
  return render(request, 'pdf_upload_single.html', {
      'form': form
  })

def pdf_result(request):
  libsvm_to_csv.libsvm_to_csv('/home/anhong-eun/study_Web-Secuity/util/data.libsvm')
  dataset = pd.read_csv('/home/anhong-eun/study_Web-Secuity/util/testresult.csv',header=None)
  df =pd.DataFrame(dataset)
  test=df.iloc[:,:]
  
  loaded_model = pickle.load(open('/home/anhong-eun/study_Web-Secuity/util/pdf_detection_ml.pkl', 'rb'))
  result = loaded_model.predict(test)
  return render(request,'pdf_result.html',{'result':result})

def one_pdf_result(request):
  parser()
  libsvm_to_csv.libsvm_to_csv('/home/anhong-eun/study_Web-Secuity/util/data.libsvm')
  dataset = pd.read_csv('/home/anhong-eun/study_Web-Secuity/util/testresult.csv',header=None)
  df =pd.DataFrame(dataset)
  test=df.iloc[0,:]
  test=test.values.reshape(1,-1)
  loaded_model = pickle.load(open('/home/anhong-eun/study_Web-Secuity/util/pdf_detection_ml.pkl', 'rb'))
  result = loaded_model.predict(test)
  return render(request,'pdf_result.html',{'result':result[0]})
