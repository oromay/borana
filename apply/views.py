import datetime
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Apply, Attachment, Term
from .forms import ApplyForm
from borana.settings import DROPBOX_CLIENT


def days_left(deadline):
    today = datetime.date.today()
    days_left = str(deadline - today).split(' ')[0]
    if int(days_left[-1])>4 or int(days_left[-1])==0 or 10< int(days_left) <15:
        word = "дней"
        verb = 'Осталось'
    elif 1<int(days_left[-1])<5:
        word = "дня"
        verb = 'Осталось'
    else:
        word = "день"
        verb = 'Остался'
    return (verb + ' ' + days_left + ' ' + word)

def done_view(request):
    context = {
        "name": 'Грант "Африка"',
        "title": 'Спасибо!',
    }
    return render(request, "complete.html", context)

def add_to_dropbox(path):
    with open(('media_cdn/'+path), 'rb') as f:
        response = DROPBOX_CLIENT.put_file(path, f)


# def apply_view(request):
#     form = ApplyForm(request.POST or None, request.FILES or None)
#     terms = Term.objects.all()
#     if form.is_valid():
#         Apply.objects.create(first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
#         for each in (form.cleaned_data['attachments']):
#             Attachment.objects.create(document=each, applicant = Apply.objects.last())
#         return HttpResponseRedirect('/done')
#     context = {
#         "title": 'Спасибо!',
#         'terms':terms,
#         'form': form,
#         }
#     return render(request, "home.html", context)



class UploadView(FormView):
    template_name = 'index.html'
    form_class = ApplyForm
    success_url = '/done/'
    def get_context_data(self, ** kwargs):
        context = super(UploadView, self).get_context_data( ** kwargs)
        context['f'] = open('main_text.txt', 'r')
        context['advice'] = open('advice.txt', 'r')
        context['name'] = 'ГРАНТ "АФРИКА"'
        context['terms'] = Term.objects.all()
        deadline = datetime.date(2017,3,31)
        context['deadline'] = deadline
        context['days_left'] = days_left(deadline)
        return context

    def form_valid(self, form):
        Apply.objects.create(first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
        for each in (form.cleaned_data['attachments']):
            Attachment.objects.create(document=each, applicant = Apply.objects.last())
            add_to_dropbox(str(Attachment.objects.last().document))
        return super(UploadView, self).form_valid(form)
