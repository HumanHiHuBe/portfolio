from django.shortcuts import render, redirect
from .models import *
from .forms import MessageForm

# Create your views here.

def home(request):
    error = ""
    if request.method == 'POST':
        mo = Message()
        mo.senderName = request.POST['senderName']
        mo.senderEmail = request.POST['senderEmail']
        mo.theMessage = request.POST['theMessage']
        if mo.senderName == "" or mo.theMessage == "":
            error = 'Name & Email are required fields, please correct & resend.'
        else:
            try:
                mo.save()
            except:
                error = 'Something went wrong, please resend.'
        return redirect('home')
    else:
        projects = Projects.objects.all()
        contacts = ContactInfo.objects.all()
        resume = Resume.objects.all()
        myphoto = MyPhoto.objects.all()
        about = About.objects.all()
        return render(request, 'resumeApp/home.html', {'about':about, 'projects':projects, 'contacts':contacts, 'resume':resume, 'myphoto':myphoto, 'error':error})

