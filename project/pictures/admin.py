# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:22:33-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   vabyz971
# @Last modified time: 2020-09-02T22:16:35-04:00
# @License: GPLv3
from django.contrib import admin

from .models import Picture


@admin.register(Picture)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'date')
    date_hierarchy = 'date'
