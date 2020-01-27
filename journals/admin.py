from django.contrib import admin
from journals.models import Profile, Journal, Entry, Todo


admin.site.register(Profile)

admin.site.register(Journal)

admin.site.register(Entry)

admin.site.register(Todo)
