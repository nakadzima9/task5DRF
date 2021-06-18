from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('Course/', views.CourseList.as_view(), name='Courses_List'),
    path('Course/<int:pk>/', views.CourseDetail.as_view(),name='Course_Detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)