# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:22:33-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   jahleel
# @Last modified time: 2020-10-17T10:42:42-04:00
# @License: GPLv3

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from nierInterface.generic import ListView, CreateView

from .forms import PictureAddForm
from .models import Picture


class PicturesListView(ListView):

    model = Picture
    title = _('Liste des images')
    template_name = 'pictures/pictures.html'
    paginate_by = 10


class PicturesCreateView(CreateView):
    model = Picture
    title = _('Ajouter votre Images')
    form_class = PictureAddForm
