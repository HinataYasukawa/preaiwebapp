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
    print("GGG")
    if request.method == 'POST':
        print("FFF")
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("AAA")
            file_obj = request.FILES['file']
            if file_obj:
                print("BBB")
                handle_uploaded_file(file_obj)
                return render(request, 'file_upload/frontpage.html', {
                    'form': form, 'show_success_message': True
                })
            else:
                return render(request, 'file_upload/frontpage.html', {
                    'form': form, 'error_message': 'ファイルを選択していません。'
                })
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/frontpage.html', {'form': form})
#
# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    print("CCC")
    # mediaフォルダにファイルを保存する
    file_path = os.path.join('./media', file_obj.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
# ------------------------------------------------------------------
def processing(request):
    filename = request.GET.get('filename')
    # 解析処理を行うためのフィードバックアプリにリダイレクト
    return redirect(reverse('feedback:result') + f'?filename={filename}')
