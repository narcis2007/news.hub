__author__ = 'narcis'

from django import forms
from models import RawArticle

class ArticleForm(forms.ModelForm):

    class Meta:
        model=RawArticle
        fields=['title','content','email']

# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model=Comment
#         fields=['content']
    '''
    def clean(self):
        cleaned_data=self.cleaned_data


        return cleaned_data
    '''