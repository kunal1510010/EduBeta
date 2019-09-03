from django.db import models

# Create your models here.


class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.first_name)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


