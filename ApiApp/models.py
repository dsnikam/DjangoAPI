from email.policy import default
from bson import ObjectId
from djongo import models

# Create your models here.

class RawData(models.Model):
    _id = models.ObjectIdField(db_column="_id",primary_key=True)
    dd = models.CharField(max_length=150)
    vn = models.CharField(max_length=150)
    ep = models.BigIntegerField()
    dt = models.JSONField()
    
    def __str__(self):
        return str(self.ep)

