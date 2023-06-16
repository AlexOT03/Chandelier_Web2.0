from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexHome.as_view(), name='indexHome'),
    path('cotizacion_rapida/', views.fastQuoteHome.as_view(), name='fastQuoteHome'),
    path('ubicaciones/<str:reference>/<id>/', views.locationHome.as_view(), name='locationHome'),
    path('ubicacion/informacion/<int:id>/', views.locationInfoHome.as_view(), name='locationInfoHome'),
    path('cotizar/<id>', views.quoteHome.as_view(), name='quoteHome'),
    path('acerca_de/', views.aboutUsHome.as_view(), name='aboutHome'),
    path('contactanos/', views.contactHome.as_view(), name='contactHome'),
]