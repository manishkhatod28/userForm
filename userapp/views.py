from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserFormForm
from .models import UserForm

def user_form(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            form.save()
            send_email_notification(form.cleaned_data['email'])
            return redirect('form_submitted')
    else:
        form = UserFormForm()
    return render(request, 'user_form.html', {'form': form})

def send_email_notification(email):
    subject = 'Form Submitted Successfully'
    message = 'Thank you for submitting the form.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

def form_submitted(request):
    forms = UserForm.objects.all()
    return render(request, 'userform/form_submitted.html', {'forms': forms})
