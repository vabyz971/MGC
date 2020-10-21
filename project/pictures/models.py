# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:22:33-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   jahleel
# @Last modified time: 2020-09-16T15:09:46-04:00
# @License: GPLv3
from __future__ import unicode_literals
import os

from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete
from django.db import models


def picture_directory_path(instance, filename):
    return 'images/{}'.format(filename)


class Picture(models.Model):

    image = models.ImageField(_('image'),
                              blank=True,
                              null=False,
                              upload_to=picture_directory_path)

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

    def remove_file(self, field_name=None):
        """Supprime physiquement le fichier

        Args:
            field_name: None du champs où est stocké le fichier

        Returns:
            Oui ou non si la suppression a réussi ou non
        """
        field = getattr(self, field_name, False)
        if field:
            if os.path.exists(field.path):
                os.remove(field.path)
                return True
        return False

    def save(self, *args, **kwargs):
        """Vérifie si le fichier a été supprimé ou changé pour savoir
        si on supprime physiquement
        """
        if self.pk:
            doc = self.__class__.objects.get(pk=self.pk)
            if not self.image == doc.image:
                doc.remove_file('image')

        super().save(*args, **kwargs)


def remove_file(sender, instance=None, **kwargs):
    """ Supprime le fichier après la suppression de l'objet.
    À utiliser avec un post_delete
    """
    if instance is None:
        return
    instance.remove_file('image')


post_delete.connect(remove_file, sender=Picture)
