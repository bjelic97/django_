from django.urls import path

from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    #path('', MyListView.as_view(), name='courses-list'),
    #path('', CourseView.as_view(template_name='about.html'), name='courses-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete', CourseDeleteView.as_view(), name='course-delete'),
 
]
