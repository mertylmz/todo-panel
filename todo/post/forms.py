from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'pname',
            'name',
            # 'title',
            # 'date',
            'description',
            # 'title2',
            # 'date2',
            # 'description2'
        ]