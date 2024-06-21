from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
import os

def file_upload(request):
    print("GGG")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print("アップロードされたファイル:", request.FILES)
        if form.is_valid():
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

def handle_uploaded_file(file_obj):
    print("CCC")
    # mediaフォルダにファイルを保存する
    file_path = os.path.join('./media', file_obj.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

def processing(request):
    filename = request.GET.get('filename')
    # 解析処理を行うためのフィードバックアプリにリダイレクト
    return redirect(reverse('feedback:result') + f'?filename={filename}')
