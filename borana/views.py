from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from .forms import ContactUsForm

def contact_us(request):
    form = ContactUsForm(request.POST or None)
    context = {'form': form, 'name':'Contact us'}
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        name = form.cleaned_data['first_name']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['moreplavatel@gmail.com',]
        message = 'Сообщение от %s \n %s \n via %s' %(name, message, sender)
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipients, fail_silently=False)
        context = {
        'sent': True,
        'Text':'Спасибо!'}
    return render(request, "contact.html", context)


# Create your views here.
