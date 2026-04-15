from django.urls import path

from apps.plast4ce import views

app_name = 'plast4ce'

urlpatterns = [
    path('', views.home, name='plast4ce_home'),
    path('about/', views.about, name='plast4ce_about'),
    path('contact/', views.contact, name='plast4ce_contact'),
    path('faq/', views.faq, name='plast4ce_faq'),
    path('pricing/', views.pricing, name='plast4ce_pricing'),
    path('services/', views.services, name='plast4ce_services'),
    path('services/<int:pk>/', views.service_detail, name='plast4ce_service_detail'),
    path('projects/', views.projects, name='plast4ce_projects'),
    path('projects/<int:pk>/', views.project_detail, name='plast4ce_project_detail'),
    path('gallery/', views.gallery, name='plast4ce_gallery'),
    path('blog/', views.blog, name='plast4ce_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='plast4ce_blog_detail'),
    path('team/', views.team, name='plast4ce_team'),
    path('team/<int:pk>/', views.team_detail, name='plast4ce_team_detail'),
]
