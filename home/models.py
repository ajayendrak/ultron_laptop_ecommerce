from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    desc=models.TextField()
    date=models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table="contactinfo"