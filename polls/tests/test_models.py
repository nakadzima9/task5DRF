from django.test import TestCase
from polls.models import Course, Category


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Dart', imgpath='Veider')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field = category._meta.get_field('name').verbose_name
        self.assertEquals(field, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 64)

    def test_imagePath_label(self):
        category= Category.objects.get(id=1)
        field= category._meta.get_field('imgpath').verbose_name
        self.assertEquals(field,'imgpath')
    
    def test_imagePath_max_length(self):
        category= Category.objects.get(id=1)
        field= category._meta.get_field('imgpath').max_length
        self.assertEquals(field, 64)

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Joseph', imgpath='Jojo')
        Course.objects.create(
            name='Neobis', description='Jojo adventures', category=category, logo=None)

    def test_name_label(self):
        course = Course.objects.get(id=1)
        field = course._meta.get_field('name').verbose_name
        self.assertEquals(field, 'name')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length, 64)

    def test_description_label(self):
        course = Course.objects.get(id=1)
        field = course._meta.get_field('description').verbose_name
        self.assertEquals(field, 'description')

    def test_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('description').max_length
        self.assertEquals(max_length, 254)

    def test_ForeignKey_label(self):
        course = Course.objects.get(id=1)
        field = course._meta.get_field('category').verbose_name
        self.assertEquals(field, 'category')

    def test_imageField(self):
        course = Course.objects.get(id=1)
        field = course._meta.get_field('logo').verbose_name
        self.assertEquals(field, 'logo')