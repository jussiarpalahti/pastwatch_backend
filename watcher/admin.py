
from django.contrib import admin

from .models import Data, Document, Resource, Link, Tag, Type

admin.site.register(Data)
admin.site.register(Document)
admin.site.register(Resource)
admin.site.register(Link)
admin.site.register(Type)

