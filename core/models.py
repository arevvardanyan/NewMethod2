from django.db import models

class MainCategory(models.Model):
    name = models.CharField('Category name',max_length=255)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'