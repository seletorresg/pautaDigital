"""pautaDigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, ListView

urlpatterns = [
   path('admin/',admin.site.urls),
   path('hoy/',views.current_datetime,name='datetime_now'),
   path('home/',views.home_page,name='home'),
   path('',views.home_page,name='home'),
   path('today/',views.home_with_time,name='home_with_time'),
   path('clientes/',views.show_clients.as_view(),name='listado_clientes'),
   path('clientes/<slug:pk>/marcas',views.show_brands.as_view(),name='listado_marcas'),
   path('facturas/',views.show_invoices,name='listado_facturas'),
   path('download/<str:fileName>',views.download_pdf_file, name='download_file'),
   path('info/', TemplateView.as_view(template_name='informativo.html'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
