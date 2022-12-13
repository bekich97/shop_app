from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Product(models.Model):

    STATUSES = [
        ("in_stock", "В наличии"),
        ("on_order", "Под заказ"),
        ("waiting", "Ожидается поступление"),
        ("no_in_stock", "Нет в наличии"),
        ("not_produced", "Не производится"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название")
    code = models.CharField(max_length=255, verbose_name="Артикул")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    status = models.CharField(max_length=255, choices=STATUSES, verbose_name="Статус")
    image = models.ImageField(upload_to="images", verbose_name="Изображение")
    # helper to save .webp format image to mediafiles directory with django way. we don't need this field on another purpose
    webp_image = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="Изображение WEBP")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

        ordering = ['title']

    def save(self, *args, **kwargs):
        if self.image:
            # Opening the uploaded file
            img = Image.open(self.image)
            output = BytesIO()
            # paste some modifications here if you want
            # after modifications save it to the output
            img.save(output, format='WEBP')
            output.seek(0)
            # save .webp format image next to core image
            self.webp_image = InMemoryUploadedFile(
                output,
                'ImageField',
                "%s.webp"%self.image.name.split('.')[0],
                'image/webp',
                sys.getsizeof(output),
                None
            )

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
