from django.urls import path
from puppies import views

# Define urlpatterns
urlpatterns = [
    path('puppies/', views.get_post_puppies, name='get_post_puppies'),
    path('puppies/<int:pk>/', views.get_delete_update_puppy,
         name='get_delete_update_puppy'),
]
