
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ['id','name','creatrd_at']
    list_filter = ['creatrd_at']
    search_fields = ['name','content']
    summernote_fields = '__all__'

admin.site.register(Post,PostAdmin)



