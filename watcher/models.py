
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.postgres.fields import HStoreField, JSONField, ArrayField
from django_extensions.db.models import TimeStampedModel

# TODO: Might prevent links and tags between objects with different class and/or type


class BaseModel(TimeStampedModel):
    """
    Each BaseModel has creation and modification time stamps, a name,
    one or more tags and can be linked to one link

    Tags are for lists of arbitrary relations
    Links are for direct mappings between two objects like in a hierarchy
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=1024)
    tag = models.ManyToManyField('Tag')
    link = models.OneToOneField('Link')


class Data(BaseModel):
    """
    At this moment everything else in Data is stored into JSON
    These are mostly filesystem objects and other more permanent stuff
    """
    
    class Meta:
        verbose_name_plural = "data"

    store = JSONField()


class Resource(BaseModel):
    """
        At this moment everything else in Resource is stored into JSON
        These are for bookmarks and other kind of arbitrary objects
    """
    properties = JSONField()


def document_default_array():
    return ['title', 'text']


class Document(BaseModel):
    """
    A very basic base for content stored with this app
    Using content fields to denote which fields are for display purposes
    Other types of data can be stored into content as well
    """
    content_fields = ArrayField(models.CharField(max_length=30, blank=True),
                                default=document_default_array)
    content = HStoreField()
    type = models.ForeignKey('Type')


class Link(TimeStampedModel):
    """
    Links are for one to one mapping between two objects
    e.g. for hierarchical structure
    allowing for key-value properties and a type
    """
    name = models.CharField(max_length=1024, blank=True, null=True)
    type = models.ForeignKey('Type', blank=True, null=True)
    props = HStoreField(blank=True, null=True)
    target = models.OneToOneField('Link')


class Tag(TimeStampedModel):
    """
    Tag is many to many properties for multiple objects
    to share same information properties
    """
    name = models.CharField(max_length=1024)
    type = models.ForeignKey('Type', blank=True, null=True)
    props = HStoreField(blank=True, null=True)


class Type(TimeStampedModel):
    name = models.CharField(max_length=30)
