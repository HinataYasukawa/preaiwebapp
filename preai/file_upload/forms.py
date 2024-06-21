from django import forms
from file_upload.models import Post

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('file', )
