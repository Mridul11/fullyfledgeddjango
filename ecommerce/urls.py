
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.urls import urlpatterns as products_urls
from .views import ( home_page, about_page, contact_page , 
                     login_page, register_page, logout_page 
                    )
from carts.urls import urlpatterns as carts_urls 
from Tags.views import tag_view

urlpatterns = [
    path('', home_page, name="home-route"),
    path('about/', about_page, name="about-route"),
    path('contact/', contact_page, name="contact-route"),
    path('login/', login_page, name="login-route"),
    path('register/', register_page, name="register-route"),
    path('logout', logout_page, name="logout-route"),
    path('tags/', tag_view, name="tag-view"),
    path('admin/', admin.site.urls),
    path('', include(products_urls)),
    path('carts/', include(carts_urls)),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






