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
    
    path('admin/servicios/', ServicesView.as_view(), name="AdminServices"),
    
    path('admin/tematicas/', ThemesView.as_view(), name="AdminThemes"),
    
    path('admin/estados/', StatesView.as_view(), name="AdminStates"),
    
    path('admin/cotizaciones/', QuotesView.as_view(), name="AdminQuotes"),
    # URL para la vista de login
    path('accounts/', include('django.contrib.auth.urls')),
    # URL para la vista de restablecimiento de contraseña
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'), name='password_reset_complete'),
]