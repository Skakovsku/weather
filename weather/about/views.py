from django.views.generic.base import TemplateView

from weathers_content.get_user_info import get_user_info

class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        get_user_info(self.request, 'об_авторе', kwargs['town'])
        context = super().get_context_data(**kwargs)
        context = {
            'about': True,
            'name': kwargs['town'],
        }
        return context
