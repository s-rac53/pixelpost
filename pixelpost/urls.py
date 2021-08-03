"""pixelpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from pixelperfectpost import views
from django.contrib.sitemaps.views import sitemap
from pixelperfectpost import sitemaps


sitemaps = {
'static': sitemaps.StaticViewSitemap,

}


urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('services/',views.services, name="services"),
    path('works/',views.works, name="works"),
    path('portfolio/',views.portflio, name="portfolio"),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
