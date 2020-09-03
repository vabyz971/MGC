from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class NierHomeView(TemplateView):
    template_name = "base.html"
    title = _('Acceuil')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx
