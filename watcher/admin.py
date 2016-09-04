
from django.contrib import admin

from .models import Data, Document, Resource, Tag, Type, DataLink, ResourceLink, DocumentLink

admin.site.register(Data)
admin.site.register(Document)
admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(DataLink)
admin.site.register(ResourceLink)
admin.site.register(DocumentLink)
