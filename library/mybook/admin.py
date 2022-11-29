from django.contrib import admin

# Register your models here.
from mybook.models import Author, Branches, District, Book

admin.site.register(District)
admin.site.register(Branches)
admin.site.register(Author)
admin.site.register(Book)