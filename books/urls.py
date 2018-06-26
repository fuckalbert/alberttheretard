"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from mybooks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.CustomLoginView.as_view(), name='login'),
    url(r'^$', views.main_page, name='main_page'),
    url(r'^add-book/$', views.add_book_page, name='add_book'),
    url(r'^book/(?P<book_id>\d+)/$', views.book_page, name='single_book'),
    url(r'^logout/$', views.CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

