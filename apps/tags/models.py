from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applies to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # how to identify any object to tag (product, pic, article):
    # Type and ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()