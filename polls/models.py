from django.db import models

class Course(models.Model):
    name= models.CharField(max_length=64)
    description= models.CharField(max_length=254)
    logo= models.ImageField(upload_to='media/jpg/')
    def __str__(self):
        return self.name

class Branch(models.Model):
    laitude = models.CharField(max_length=64)
    longitude= models.CharField(max_length=64)
    address= models.CharField(max_length=64)
    branchs= models.ForeignKey('Course', related_name='branchs',on_delete=models.CASCADE,null=True)    
    def __str__(self):
        return self.address

class Contact(models.Model):
    CONTACTS=[
        (1,'PHONE'),
        (2,'FACEBOOK'),
        (3,'EMAIL')
    ]
    Type= models.IntegerField(choices=CONTACTS,default=1)
    Value= models.CharField(max_length=64)
    contacts= models.ForeignKey('Course',related_name='contacts', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Value

class Category(models.Model):
    name= models.CharField(max_length=64)
    imgpath= models.CharField(max_length=64)
    category= models.ForeignKey('Course',related_name='category', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
