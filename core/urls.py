from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/<slug>/', views.ItemDetailView.as_view(), name='product')
]
