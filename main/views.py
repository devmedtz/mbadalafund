from django.shortcuts import render,get_object_or_404,redirect
from .forms import PitchForm
from .models import *

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages


def home(request):

    template_name = 'main/home.html'

    context = {
        'title':'Home',
    }

    return render(request, template_name, context)

def team(request):
    template_name = 'main/team.html'
    context = {'title':'Our Team',}
    return render(request, template_name, context)

def contact(request):
    template_name = 'main/contact.html'
    context = {'title':'Contact Us',}
    return render(request, template_name, context)

def pitch(request):
    template_name = 'main/pitch.html'
    if request.POST:
        form = PitchForm(request.POST, request.FILES)
        print(form)        
        if form.is_valid():
            pitch = form.save(commit=False)
            pitch.save()            
            subject = 'Pitch Submission'            
            html_message = render_to_string('main/mail_template.html', {'pitch':pitch})
            plain_message = strip_tags(html_message)
            recipient_list = ['info@ssc.co.tz',]
            from_email ="info@mbadala.co.tz"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)
            messages.success(request, 'Submitted Successfully')
            return redirect( to = 'main:pitch')
        else:
            messages.error(request, 'Error Occured!')
            return redirect( to = 'main:pitch')
    else:
        form = PitchForm()
    context = {
        'title':'Submit your pitch',
        'form':form
    }
    return render(request, template_name, context)
