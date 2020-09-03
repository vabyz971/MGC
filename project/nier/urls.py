# @Author: Jahleel Lacascade <vabyz971>
# @Date:   2020-09-02T19:47:18-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   vabyz971
# @Last modified time: 2020-09-02T19:48:09-04:00
# @License: GPLv3

from django.urls import path, include
from . import views

app_name = 'nier'
urlpatterns = [
    path('', views.NierHomeView.as_view(), name="home"),
]
