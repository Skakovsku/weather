from django.views.generic.base import TemplateView

class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'about': True}
        return context
