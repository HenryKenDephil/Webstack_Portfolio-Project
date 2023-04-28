from django.urls import path, include
from rest_framework import routers
from . import views
from . views import CreateUser, LoginView


app_name = 'courses'


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)


urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
     path("users/", CreateUser.as_view(),
          name="create_user"),
     path("login/", LoginView.as_view(),
          name = "login"),
     path('', include(router.urls)),
]
