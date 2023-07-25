from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.render_grapejs, name='render_grapejs'),
    path('grapejs/<int:page_id>/', views.grapejs, name='grapejs'),
    path('save-page/<int:page_id>/', views.save_page, name='save_page'),
    path('save-exported-content/<int:page_id>/', views.save_exported_content, name='save_exported_content'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
