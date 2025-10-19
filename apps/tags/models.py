from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects.filter(content_type=content_type, 
                                         object_id=obj_id)
    

class Tag(models.Model):
    name = models.CharField(max_length=255)


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    # What tag applies to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # how to identify any object to tag (product, pic, article):
    # Type and ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()