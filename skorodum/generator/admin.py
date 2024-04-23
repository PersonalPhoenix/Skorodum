from django.contrib import admin

from .models import *


admin.site.register(Game)
admin.site.register(Round)
admin.site.register(Question)
admin.site.register(Category)