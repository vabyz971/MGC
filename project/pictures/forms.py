# @Author: Jahleel Lacascade <jahleel>
# @Date:   2020-09-03T09:38:46-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   jahleel
# @Last modified time: 2020-09-03T09:46:17-04:00
# @License: GPLv3

from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Picture


class PictureAddForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('__all__')
