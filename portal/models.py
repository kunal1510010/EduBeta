from django.db import models


# Create your models here.


class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    user_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_name)


class Document(models.Model):
    doc_id = models.AutoField(primary_key=True, null=False)
    user_id = models.IntegerField()
    doc_file = models.FileField(upload_to='documents/', default='none')

    def __str__(self):
        return str(self.doc_file)
