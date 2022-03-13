# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'CBV_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Company_list_view.as_view(), name='home'),
    path('<int:pk>/', views.Company_Details_view.as_view(), name='detail'),
    path('create/', views.Company_create_view.as_view(), name='create'),
    path('update/<int:pk>/', views.Company_update_view.as_view(), name='update'),
    path('delete/<int:pk>/', views.Company_delete_view.as_view(), name='delete'),
]
