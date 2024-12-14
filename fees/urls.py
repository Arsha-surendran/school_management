from django.urls import path
from . import views

urlpatterns = [
    path('fees/', views.fees_history_list, name='fees_history_list'),
    path('fees/add/', views.add_fee_history, name='add_fee_history'),
    path('fees/edit/<int:fee_id>/', views.edit_fee_history, name='edit_fee_history'),
    path('fees/delete/<int:fee_id>/', views.delete_fee_history, name='delete_fee_history'),
]
