from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.welcome_page,name='index'),
    path('subjects',views.get_subjects,name='subjects'),
    path('subject/<int:pk>', views.get_subject, name='subject'),
    path('subject',views.add_subject, name='add_subject'),
    path('subject/<int:pk>/update',views.update_subject, name='update'),
    path('subject/<int:pk>/delete',views.delete_subject, name='delete'),
    ]
