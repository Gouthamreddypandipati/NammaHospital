from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Doctor)
admin.site.register(Reports)
admin.site.register(Courses)
admin.site.register(Docterpatient)
admin.site.register(Tests)