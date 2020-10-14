from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
