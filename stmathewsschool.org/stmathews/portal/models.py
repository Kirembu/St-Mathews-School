from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null= True)
    bio = models.TextField(null=True)
    def __unicode__(self):
        return self.first_name
    
    class Meta:
        unique_together = ("first_name", "last_name")