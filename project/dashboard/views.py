from django.utils.translation import ugettext_lazy as _
from nierInterface.generic import TemplateView

# Create your views here.


class DashboardHomeView(TemplateView):
    title = _('Dashboard')
    template_name = 'dashboard/dashboard.html'
