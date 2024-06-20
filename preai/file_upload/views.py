# file_upload/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import os
import uuid
import sys

# ------------------------------------------------------------------
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            sys.stderr.write("*** file_upload *** aaa ***\n")
            handle_uploaded_file(request.FILES['file'])
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/frontpage.html', {'form': form})
#
#
# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    file_path = 'media/documents/' + file_obj.name 
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
#
# ------------------------------------------------------------------
def success(request):
    str_out = "Success!<p />"
    str_out += "成功<p />"
    return HttpResponse(str_out)
# ------------------------------------------------------------------
def processing(request):
    filename = request.GET.get('filename')
    # 解析処理を行うためのフィードバックアプリにリダイレクト
    return redirect(reverse('feedback:result') + f'?filename={filename}')
