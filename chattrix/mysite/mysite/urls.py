from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('', lambda request: redirect('chat/', permanent=False)),  # This redirects '/'
]
