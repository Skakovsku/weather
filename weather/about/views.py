from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from weathers_content.get_user_info import get_user_info
from .forms import EmailForm

class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, *args, **kwargs):
        get_user_info(self.request, 'об_авторе', kwargs['town'])
        context = {
            'about': True,
            'name': kwargs['town'],
        }
        return context


def message(request, town):
    template = 'about/message.html'
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
                'Zeveze',
                form.data['message'],
                'Skakovsku@yandex.ru',
                ['Skakovsku@yandex.ru '],
                fail_silently=False,
            )
            return redirect('about:message_sended', town)
    else:
        form = EmailForm()
    context = {
        'about': True,
        'name': town,
    }
    return render(request, template, context)

def message_sended(request, town):
    template = 'about/message_sended.html'
    context = {
        'about': True,
        'name': town,
    }
    return render(request, template, context)
