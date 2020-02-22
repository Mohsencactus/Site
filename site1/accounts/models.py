from django.db import models

class uploader(models.Model):
    title = models.CharField(max_length=200,default='')
    document = models.FileField(upload_to='./accounts',default='')

    def __str__(self): 
        return self.title