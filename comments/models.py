from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    comment_name = models.CharField(max_length=250, verbose_name='Name')
    comment_email = models.EmailField(verbose_name='Email')
    comment_content = models.TextField(verbose_name='Content')
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    comment_user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                     verbose_name='User', blank=True, null=True)
    comment_date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    comment_published = models.BooleanField(verbose_name='Published', default=False)

    def __str__(self):
        return self.comment_name
