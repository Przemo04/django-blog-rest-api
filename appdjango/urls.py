"""appdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
#from news.views import PostList, PostDetailApiView
#from news.views import PostDetailApiView
from slider.views import MainSliderList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/news/', include('news.urls', namespace='posts-api')),

    #url(r'^api/news/', PostList.as_view()),
    #url(r'^(?P<pk>\d+)/api/news/$', PostDetailApiView().as_view(), name='detail'),
    url(r'^api/slider/', MainSliderList.as_view()),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'', include('news.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
