from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),   
     # Admin
    path('admin/staff/', views.manage_staff, name='manage_staff'),
    path('admin/students/', views.manage_students, name='manage_students'),
    path('admin/fees/', views.manage_fees, name='manage_fees'),
    path('admin/library/', views.manage_library, name='manage_library'),

    # Office Staff
    path('office/students/', views.view_students, name='office_students'),
    path('office/fees/add/', views.add_fee, name='add_fee'),
    path('office/fees/edit/<int:fee_id>/', views.edit_fee, name='edit_fee'),
]