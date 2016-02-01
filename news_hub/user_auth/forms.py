__author__ = 'narcis'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from email import send_initial_email
from django.core.exceptions import MultipleObjectsReturned,ObjectDoesNotExist
from datetime import datetime
class MyRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def save(self,commit=True):


        user=super(MyRegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            send_initial_email(user)
            user.save()
        return user

    def clean(self):
        cleaned_data=super(UserCreationForm,self).clean()
        try:
            if User.objects.filter(email=self.cleaned_data['email']).exists():
                raise forms.ValidationError('Email already used!')
        except :
            pass
        return cleaned_data

def get_upload_file_name(instance,filename):
        return 'uploaded_files/' + str(datetime.now())+'_' + filename

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)
