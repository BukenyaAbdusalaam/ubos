from .views import home
from django.urls import path

from .views import manage_gadgets, issue_gadget, return_gadget,gadget_form, access_control_form, access_log_form, user_form,list_gadgets, update_gadget, delete_gadget

urlpatterns = [
    path("", home, name="home"),
    path('manage_gadgets/', manage_gadgets, name='manage_gadgets'),
    path('issue_gadget/', issue_gadget, name='issue_gadget'),
    path('return_gadget/', return_gadget, name='return_gadget'),
     path('gadget_form/', gadget_form, name='gadget_form'),
    path('access_control_form/', access_control_form, name='access_control_form'),
    path('access_log_form/', access_log_form, name='access_log_form'),
    path('user_form/', user_form, name='user_form'),
     path('gadget_form/', gadget_form, name='gadget_form'),
    path('access_control_form/', access_control_form, name='access_control_form'),
    path('access_log_form/', access_log_form, name='access_log_form'),
    path('user_form/', user_form, name='user_form'),
    path('list_gadgets/', list_gadgets, name='list_gadgets'),
    path('update_gadget/<int:gadget_id>/', update_gadget, name='update_gadget'),
    path('delete_gadget/<int:gadget_id>/', delete_gadget, name='delete_gadget'),
    # Add other URLs as needed
]



