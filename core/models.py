from django.db import models

class MainCategory(models.Model):
    name = models.CharField('Category name',max_length=255)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Company(models.Model):
    name = models.CharField('Company name',max_length=255)

class MainProduct(models.Model):
    name = models.CharField('name',max_length=255)
    description = models.TextField('Description')
    embedding = models.JSONField('Embedding', null=True)
    img_1 = models.ImageField('Image main',upload_to='media/product')
    img_2 = models.ImageField('image 2',upload_to='media/product')        
    img_3 = models.ImageField('image 3',upload_to='media/product')
    addtime = models.DateField('add data',auto_now_add=True)
    category = models.ForeignKey(MainCategory,on_delete=models.CASCADE,related_name='Categorry')
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='Companny')
    price_now = models.FloatField('Price now')
    discount = models.FloatField('discount')


    def __str__(self) -> str:
        return f'{self.name}-{self.company}'
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    