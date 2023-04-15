from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.ManageCourseListView.as_view(),
        name= 'manage_course_list'),
    path('create/', views.CourseCreateView.as_view(),
         name= 'create_course'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(),
         name= 'edit_course'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(),
         name= 'delete_course'),
     path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
          name = 'course_module_update'),
]