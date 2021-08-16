# Core Django imports
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls', namespace='blog')),  # Urls for article app.
    path('api/v1/article/', include('blog.api.v1.routers.routers')), # Urls for API.
    path('admin/', admin.site.urls),

    # Url for password reset.
    path('account/password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='password_reset'),

    # Url for successful password reset.
    path('account/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    # Url for successful password reset confirm.
    path('account/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # Url for password reset done.
    path('account/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns


# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "Bona Admin"
admin.site.site_title = "Bona Admin Portal"
admin.site.index_title = "Welcome to Bona Blog Portal"