from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog # 어떤 모델쓸래?
        fields = ("title", "body")
        # 그 모델에서 어떤 필드 쓸래?