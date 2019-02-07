from django.contrib import admin

# Register your models here.
from catalog.models import Mentee
admin.site.register(Mentee)
from catalog.models import Mentor
admin.site.register(Mentor)
from catalog.models import Mentorgroup
admin.site.register(Mentorgroup)
