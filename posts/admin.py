from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'id',
        'post_title',
        'post_author',
        'post_date',
        'post_category',
        'post_published',
        'post_author',
    )
    list_editable = ('post_published',)
    summernote_fields = ('post_content',)
    list_display_links = ('id', 'post_title',)
