# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:22:33-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   vabyz971
# @Last modified time: 2020-09-02T23:15:48-04:00
# @License: GPLv3

from PIL import ImagePalette
from django.utils.translation import ugettext_lazy as _
from django.db import models


def pictures_directory_path(instence, filename):
    return 'pictures/{}'.format(filename)


class Picture(models.Model):

    image = models.ImageField(_('image'),
                              blank=True,
                              null=False,
                              upload_to=pictures_directory_path)

    date = models.DateTimeField(_("ajouter le"), auto_now_add=True)
    updated = models.DateTimeField(_("modifier le"), auto_now=True)

    def getResolution(self):
        return '{}x{}'.format(self.image.width, self.image.height)

    def __str__(self):
        return self.image.url

    def get_add_url(self):
        return reverse('pictures:add')

    def get_absolute_url(self):
        return reverse('pictures:view', kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse('pictures:update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('pictures:delete', kwargs={"pk": self.pk})
