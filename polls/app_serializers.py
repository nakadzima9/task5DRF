from rest_framework import serializers
from .models import Course, Category, Branch, Contact

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=['laitude','longitude','address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name','imgpath']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields=['Type','Value']


class CourseSerializer(serializers.ModelSerializer):
    course=BranchSerializer(many=True)
    contacts=ContactSerializer(many=True)
    
    class Meta:
        model=Course
        fields=['name','description','category','contacts','logo','course']
    
    def create(self, validated_data):
        branchs_data = validated_data.pop('branchs')
        contacts_data = validated_data.pop('contacts')
        categorys_data = validated_data.pop('category')
        course = Course.objects.create(**validated_data)
        
        for branch_data in branchs_data:
            Branch.objects.create(course=course, **branch_data)
        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)
        for category_data in categorys_data:
            Category.objects.create(course=course, ** category_data)
        return course





