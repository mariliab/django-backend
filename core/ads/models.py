from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.title
