from django.contrib import admin
from .models import Blog , Author ,Tags ,Comments

class BlogAdmin(admin.ModelAdmin):
    list_display =  ("title", "date_d", "author" ,)  #this must be a tuple that's why extra comma is necessary 
    list_filter = ("author","tags", "date_d", )
    prepopulated_fields = {"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment" , "user_name","post",)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Author)
admin.site.register(Tags)

# Register your models here.
