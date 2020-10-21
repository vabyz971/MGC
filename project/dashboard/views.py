from django.utils.translation import ugettext_lazy as _
from nierInterface.generic import TemplateView

from pictures.models import Picture


class DashboardHomeView(TemplateView):
    title = _('Dashboard')
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        images = Picture.objects.all()
        ctx['images_list'] = images.count()
        return ctx
