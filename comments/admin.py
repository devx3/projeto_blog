from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_name', 'comment_email', 'comment_post', 'comment_published')
    list_editable = ('comment_published',)
    list_display_links = ('id', 'comment_name', 'comment_email',)
