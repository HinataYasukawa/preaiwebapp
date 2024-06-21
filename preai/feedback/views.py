from django.shortcuts import render
from .models import Feedback
import subprocess

def process_file(filename):
    # feedback.pyを呼び出して解析を行う
    result = subprocess.run(['python', 'feedback.py', filename], capture_output=True, text=True)
    return result.stdout

def result(request):
    filename = request.GET.get('filename')
    feedback = Feedback.objects.filter(filename=filename).first()
    if not feedback:
        result = process_file(filename)
        feedback = Feedback.objects.create(filename=filename, result=result)
    return render(request, 'feedback/result.html', {'feedback': feedback})
