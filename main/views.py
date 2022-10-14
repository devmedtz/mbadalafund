from django.shortcuts import render

def home(request):

    template_name = 'main/home.html'

    context = {

    }

    return render(request, template_name=template_name, context=context)
