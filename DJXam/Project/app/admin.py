from django.contrib import admin
from .models import author , publisher , book , post , category , comment
# Register your models here.
admin.site.register(author)

admin.site.register(publisher)

admin.site.register(book)

admin.site.register(post)

admin.site.register(category)

admin.site.register(comment)