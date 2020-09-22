from django.urls import path
from . import views
from.views import ProjectDetailView

urlpatterns =[
    path('', views.home, name ='portfolio-home'),
    path('profile/', views.profile ,name ='portfolio-profile'),
    path('cv/', views.cv, name ='portfolio-cv'),
    path('portfolio/', views.portfolio, name='portfolio-portfolio'),
    path('portfolio/<project_title>', ProjectDetailView.as_view(), name = "portfolio-project-detail"),
    path('contact/', views.contact, name='portfolio-contact')
]