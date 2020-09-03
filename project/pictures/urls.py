# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T16:30:45-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   vabyz971
# @Last modified time: 2020-09-02T20:06:05-04:00
# @License: GPLv3

from django.urls import path
from . import views

app_name = 'pictures'
urlpatterns = [
    path('', views.PicturesListView.as_view(), name="list"),
    # path('add/', views.PicturesCreateView.as_view(), name="add"),
]
