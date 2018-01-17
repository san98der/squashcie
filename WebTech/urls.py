"""WebTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^$', views.main_page, name='main_page'),
    url(r'^matches/$', views.matches_page, name='matches_page'),
    url(r'^ranking/$', views.ranking_page, name='ranking_page'),
    url(r'^results/$', views.results_page, name='results_page'),
    url(r'^thank_you/$', views.thank_you_page, name='thank_you_page'),
]
