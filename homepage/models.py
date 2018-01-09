from django.db import models
#from user.models import Users


class Books(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey('user.Users', on_delete=models.CASCADE, null=True)
    owner_email = models.EmailField(max_length=254,null=True)
    #image = models.FileField(upload_to='static/images/', default='static/images/no-img.png')
    image = models.FileField(upload_to='uploads/', default='static/images/no-img.png')
    owner_review = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title