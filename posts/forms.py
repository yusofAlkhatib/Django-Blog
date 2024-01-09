from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'content': SummernoteWidget(),
                  }