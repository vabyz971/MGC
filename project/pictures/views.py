# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:22:33-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   vabyz971
# @Last modified time: 2020-09-02T22:28:45-04:00
# @License: GPLv3

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Picture


class PicturesListView(ListView):

    model = Picture
    title = _('Liste des images')
    template_name = 'pictures/pictures.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx


# class PicturesCreateView(CreateView):
#     pass
