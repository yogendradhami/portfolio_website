from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    number=models.CharField(max_length=50)
    description= models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title= models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=50)
    img=models.ImageField(upload_to='static/img/blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title