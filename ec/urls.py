from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls')),
    path('accounts/', include('authentication.urls')),
    #path('account/', include('account.urls')),
    path('payment/',include('payment.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('api-token-auth', views.ObtainAuthToken)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)