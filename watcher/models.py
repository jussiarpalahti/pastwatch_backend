
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.postgres.fields import HStoreField, JSONField, ArrayField
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    """
    Each BaseModel has creation and modification time stamps, a name and one or more tags

    Tags are for lists of arbitrary relations
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=1024)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return "{0}".format(self.name)


class Data(BaseModel):
    """
    At this moment everything else in Data is stored into JSON
    These are mostly filesystem objects and other more permanent stuff
    """

    class Meta:
        verbose_name_plural = "data"

    store = JSONField(blank=True, null=True)


class Resource(BaseModel):
    """
        At this moment everything else in Resource is stored into JSON
        These are for bookmarks and other kind of arbitrary objects
    """
    properties = JSONField(blank=True, null=True)


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
    content = HStoreField(blank=True, null=True)
    type = models.ForeignKey('Type', blank=True, null=True)


class Link(TimeStampedModel):
    """
    Links are for one to one mapping between two objects
    e.g. for hierarchical structure
    allowing for key-value properties and a type
    Each content model has its own Link model
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=1024, blank=True, null=True)
    type = models.ForeignKey('Type', blank=True, null=True)
    props = HStoreField(blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.name)


class DataLink(Link):
    source = models.OneToOneField(Data, related_name="linking")
    target = models.OneToOneField(Data, related_name="linked")


class ResourceLink(Link):
    source = models.OneToOneField(Resource, related_name="linking")
    target = models.OneToOneField(Resource, related_name="linked")


class DocumentLink(Link):
    source = models.OneToOneField(Document, related_name="linking")
    target = models.OneToOneField(Document, related_name="linked")


class Tag(TimeStampedModel):
    """
    Tag is many to many properties for multiple objects
    to share same information properties
    """
    name = models.CharField(max_length=1024)
    type = models.ForeignKey('Type', blank=True, null=True)
    props = HStoreField(blank=True, null=True)

    def __str__(self):
        return "{0}{1}".format(self.name,
                               " ({0})".format(self.type) if self.type else " ()")


class Type(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{0}".format(self.name)

