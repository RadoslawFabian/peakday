from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls', namespace='mainpage')),  # główna strona z namespace
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', include('tasks.urls')),
    path('shopping/', include('shopping.urls')),
    path('dietplanner/', include('dietplanner.urls')),
    path('trainingplanner/', include('trainingplanner.urls')),  # tu poprawione include
    path('budget/', include('budget.urls')),
    path('profiles/', include('profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
