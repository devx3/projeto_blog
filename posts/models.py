from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Title')
    post_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Author')
    post_date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    post_content = models.TextField(verbose_name='Content')
    post_excerpt = models.TextField(verbose_name='Excerpt')
    post_category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Category')
    post_image = models.ImageField(upload_to='post_img/%Y/%m/%d',
                                   blank=True, null=True, verbose_name='Image')
    post_published = models.BooleanField(default=False, verbose_name='Published')

    def __str__(self):
        return self.post_title
