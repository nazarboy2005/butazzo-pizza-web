from django.db import models


class PicturesModel(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='gallery')

    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ScrollModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField('discounted_food')
    discount = models.PositiveSmallIntegerField(default=0)



    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Discounted Product'
        verbose_name_plural = 'Discounted Products'