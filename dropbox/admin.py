from django.contrib import admin
from dropbox.models import File
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
# Register your models here.

admin.site.register(File, DraggableMPTTAdmin)