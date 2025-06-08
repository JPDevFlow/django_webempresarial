"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #paths del core
    # Aquí se incluyen las URLs de la aplicación principal del proyecto
    path('', include('core.urls')),
    #paths del servicios
    # Aquí se incluyen las URLs de la aplicación de servicios
    path('services/', include('services.urls')),
    # Aquí se incluyen las URLs de la aplicación de blog
    path('blog/', include('blog.urls')),
    # Aquí se incluyen las URLs de la aplicación de páginas
    path('page/', include('pages.urls')),
      #paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    