from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views
urlpatterns = [
    path('Course/', views.CourseList.as_view()),
    path('Course/<int:pk>/', views.CourseDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)