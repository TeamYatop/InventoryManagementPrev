from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=40)

    def __str__(self):
        return '{},{}'.format(
            self.name,
            self.color,
        )


class Figure(models.Model):
    FIGURE_CODE = (
        ('XXS', 'DoubleExtraSmall'),
        ('XS', 'ExtraSmall'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
        ('XXL', 'DoubleExtraLarge'),
    )
    name = models.CharField(max_length=3, choices=FIGURE_CODE)


class Inventory(models.Model):
    product_code = models.ForeignKey(Product)
    size_code = models.ForeignKey(Figure)
    quantity = models.PositiveIntegerField(default=0)

    # def create(self, ):