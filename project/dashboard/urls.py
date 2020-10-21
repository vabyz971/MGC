# @Author: Jahleel Lacascade <jahleel>
# @Date:   2020-09-03T14:26:18-04:00
# @Email:  vabyz971@gmail.com
# @Last modified by:   jahleel
# @Last modified time: 2020-09-03T14:32:15-04:00
# @License: GPLv3

from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name="home"),
]
