from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import AdminIndex, AdminMessages
from chandelier_web.apps.admin_page_locations.views import LocationsView
from chandelier_web.apps.admin_page_services.views import ServicesView
from chandelier_web.apps.admin_page_themes.views import ThemesView
from chandelier_web.apps.admin_page_states.views import  StatesView
from chandelier_web.apps.admin_page_quotes.views import QuotesView

urlpatterns = [
    # URL para la vista de administrador
    path('admin/', AdminIndex.as_view(), name="AdminIndex"),
    path('admin/logout/', AdminIndex().logoutCrud, name="AdminLogout"),
    
    path('admin/mensajes/', AdminMessages.as_view(), name="AdminMessages"),
    
    path('admin/ubicaciones/', LocationsView.as_view(), name="AdminLocations"),
    path('admin/ubicacion/<id>/eliminar/', LocationsView().delete, name="AdminLocationsDelete"),
    path('admin/ubicacion/<id>/informacion/', LocationsView().show, name="AdminLocationsInfo"),
    path('admin/ubicacion/<id>/editar/', LocationsView().update, name="AdminLocationsEdit"),
    
    path('admin/servicios/', ServicesView.as_view(), name="AdminServices"),
    path('admin/servicios/<id>/eliminar/', ServicesView().delete, name="AdminServicesDelete"),
    path('admin/servicio/<id>/informacion/', ServicesView().show, name="AdminServicesInfo"),
    path('admin/servicio/<id>/editar/', ServicesView().update, name="AdminServicesEdit"),
    
    path('admin/tematicas/', ThemesView.as_view(), name="AdminThemes"),
    path('admin/tematica/<id>/eliminar/', ThemesView().delete, name="AdminThemesDelete"),
    path('admin/tematica/<id>/informacion/', ThemesView().show, name="AdminThemesInfo"),
    path('admin/tematica/<id>/editar/', ThemesView().update, name="AdminThemesEdit"),
    
    path('admin/estados/', StatesView.as_view(), name="AdminStates"),
    path('admin/estado/<id>/eliminar/', StatesView().delete, name="AdminStatesDelete"),
    path('admin/estado/<id>/informacion/', StatesView().show, name="AdminStatesInfo"),
    path('admin/estado/<id>/editar/', StatesView().update, name="AdminStatesEdit"),
    
    path('admin/cotizaciones/', QuotesView.as_view(), name="AdminQuotes"),
    
    # URL para la vista de login
    path('accounts/', include('django.contrib.auth.urls')),
    # URL para la vista de restablecimiento de contraseña
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'), name='password_reset_complete'),
]