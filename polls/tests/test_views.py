from django.test import TestCase
from django.urls.base import resolve
from rest_framework.reverse import reverse
from polls.views import CourseList, CourseDetail
from django.urls import reverse
from polls.models import Course, Category
import json
from polls.app_serializers import CourseSerializer


class TestViews(TestCase):
    def setUp(self):
        category = Category.objects.create(id=3, name='Jostar', imgpath='Jonathan')
        Course.objects.create(
            id=3, name='Test name', description='Test course', category=category, logo=None)
    
    def First_Test_CourseList(self):
        response = self.client.get(reverse('Course_List'))
        self.assertEquals(response.status_code, 200)
    def Test_CourseList_data(self):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = self.client.get(reverse('Course_List'))
        self.assertEquals(response.data, serializer.data)
    def Second_Test_CourseList(self):
        url = reverse('Courses_List')
        self.assertEquals(resolve(url).func.view_class, CourseList)
    def test_CourseDetail(self):
        url = reverse('Course_Detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, CourseDetail)