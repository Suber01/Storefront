from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    #To determine what tag is applied to which Item
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    #identifying the object this tag is applied to
    #Type(product, video, article)--using type we can find the table
    #ID()--using ID we can find the record    
    content_type=models.ForeignKey(ContentType, on_delete= models.CASCADE)
    object_id= models.PositiveIntegerField()
    content_object= GenericForeignKey()