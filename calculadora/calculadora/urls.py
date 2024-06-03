<<<<<<< HEAD

=======
>>>>>>> ded7fc8b56ed4d9ca623f4d6bd1656e084ad7498
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mac.urls')),
]
