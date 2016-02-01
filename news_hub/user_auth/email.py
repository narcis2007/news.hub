__author__ = 'narcis'
from django.core.mail import send_mail


def send_initial_email(instance):
    #send_mail('Initial Email','Hello '+instance.last_name +' '+ instance.first_name+'! \nYou\'ve just been registered! ','booking.internship@gmail.com',[str(instance.email)])
    print 'bn'

def send_confirmation_email(instance):

    #send_mail('Confirmation Email','Hello again '+instance.first_name+ ' '+instance.last_name+', we\'ve just confirmed your booking! Your appointment date and time is: '+str(instance.final_date.year) +'-'+str(instance.final_date.month)+'-'+str(instance.final_date.day)+' '+str(instance.final_date.hour)+':'+str(instance.final_date.minute),'booking.internship@gmail.com',[str(instance.email)])
    print 'sent'