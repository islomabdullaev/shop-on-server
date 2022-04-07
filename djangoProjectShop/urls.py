from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = i18n_patterns(
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
    path("products/", include("products.urls", namespace="products")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("users/", include("users.urls", namespace="users")),
    path("", include("pages.urls", namespace="pages")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
