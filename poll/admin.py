from django.contrib import admin
from .models import Poll, Vote, Choice

# Register your models here.
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Choice)
