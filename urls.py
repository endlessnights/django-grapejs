from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grapejs/<int:page_id>/', views.grapejs, name='grapejs'),
    path('save-page/<int:page_id>/', views.save_page, name='save_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)