from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from django.contrib.auth import authenticate, login,logout
from django.core.context_processors import csrf
from forms import MyRegistrationForm,LoginForm
from django.contrib import messages
from django.conf import settings
# from notification.models import Notification

def index(request):

    '''template=loader.get_template('user_auth/index.html')
    return HttpResponse(template.render(RequestContext(request)))
    '''
    args={}
    '''
    n=Notification.objects.filter(viewed=False)
    if request.user.id:
        n=n.filter(user=request.user)
    args['unread_notifications']=n.count() #inlocuiesc cu cookies si il mut in login
    '''
    return render(request,'user_auth/index.html',args)

def login_view(request):
    context={}
    context.update(csrf(request))
    context['form']=LoginForm()
    template=loader.get_template('user_auth/login.html')
    return HttpResponse(template.render(RequestContext(request,context)))

def register_user(request):
    if request.method=='POST':
        form=MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registered')
        else:
            args={}
            args.update(csrf(request))
            args['form']=form
            return render(request,'user_auth/sign_up.html',args)

    args={}
    args.update(csrf(request))
    args['form']=MyRegistrationForm()
    return render(request,'user_auth/sign_up.html',args)

def registered(request):
    return render(request,'user_auth/registered.html')

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        # request.session['unread_notifications']=str(Notification.objects.filter(user=request.user).exclude(viewed=request.user).count())
        response = render(request,'user_auth/index.html')

        return response
    else:
        args={}
        args['form']=LoginForm(request.POST or None)
        if username!='' and password!='':
            args['invalid_details']='invalid user or password'
        return render(request,'user_auth/login.html',args)

def invalid(request):
    template=loader.get_template('user_auth/invalid.html')
    return HttpResponse(template.render(RequestContext(request)))

def logged_out(request):
    template=loader.get_template('user_auth/logged_out.html')
    logout(request)
    return HttpResponse(template.render(RequestContext(request)))

def logged(request):
    template=loader.get_template('user_auth/logged.html')
    return HttpResponse(template.render(RequestContext(request)))

def sign_up(request):
    template=loader.get_template('user_auth/sign_up.html')
    return HttpResponse(template.render(RequestContext(request)))

def forgot_pass(request):
    template=loader.get_template('user_auth/forgot_pass.html')
    return HttpResponse(template.render(RequestContext(request)))

def send_reset_pass_link(request):
    if request.method=='POST':
        #send_reset_pass_email(request.POST.get('email',''))
        print(request.POST.get('email',''))
        return HttpResponseRedirect('/registered')