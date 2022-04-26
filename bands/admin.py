from labels.models import Label
from django.contrib import admin

from bands.models import Album, Band
from members.models import Member

admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Label)
admin.site.register(Album)

# Register your models here.
