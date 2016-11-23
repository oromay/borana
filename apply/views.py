from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from .forms import ApplyForm


def apply_view(request):
    context = {
        "title": 'Спасибо!',
    }
    return render(request, "done.html", context)

class UploadView(FormView):
    template_name = 'home.html'
    form_class = ApplyForm
    success_url = '/done/'

    def form_valid(self, form):
        b = list(form.cleaned_data['attachments'])
        if len(b) == 3:
            Apply.objects.create(attachments=b[0], attachment_02=b[1], attachment_03=b[2], first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
        elif len(b) == 2:
            Apply.objects.create(attachments=b[0], attachment_02=b[1], first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
        else:
            Apply.objects.create(attachments=b[0], first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
        return super(UploadView, self).form_valid(form)
