from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва категорії')
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    def __str__(self):
        return self.name

class CountryModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Країна походження')
    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'
    def __str__(self):
        return self.name

class BrandModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва бренду')
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'
    def __str__(self):
        return self.name

class SizeModel(models.Model):
    size = models.CharField(max_length=5, verbose_name='Розміри')
    class Meta:
        verbose_name = 'Розмір'
        verbose_name_plural = 'Розміри'
    def __str__(self):
        return self.size

class SexModel(models.Model):
    sex = models.CharField(max_length=5, verbose_name='Стать')
    class Meta:
        verbose_name = 'Стать'
        verbose_name_plural = 'Стать'

    def __str__(self):
        return self.sex

class ProductsModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва товару')
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name='Категорія', default=None)
    country = models.ForeignKey(CountryModel, on_delete=models.PROTECT, verbose_name='Країна', default=None)
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, verbose_name='Бренд', default=None)
    image = models.ImageField(upload_to='products/', verbose_name='Фото')
    video = models.FileField(upload_to='products/video/', verbose_name='Відеоогляд', blank=True)
    price = models.IntegerField(verbose_name='Ціна', default=0)
    about = models.TextField(max_length=300, verbose_name='Інформація', blank=True)
    sex = models.ForeignKey(SexModel, verbose_name='Стать', on_delete=models.PROTECT, default=None)
    size = models.ManyToManyField(SizeModel, verbose_name='Розміри')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата публкації')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
    def __str__(self):
        return self.name

class AdministrationModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Імя')
    achievement = models.CharField(max_length=300, verbose_name='Досягення', blank=True)
    experience = models.CharField(max_length=300, verbose_name='Досвід', blank=True)
    skills = models.CharField(max_length=300, verbose_name='Посада', blank=True)
    image = models.ImageField(upload_to='products/admins/', verbose_name='Фото')
    bio = models.TextField(verbose_name='Біографія', blank=True)

    class Meta:
        verbose_name = 'Адмін'
        verbose_name_plural = 'Адміни'
    def __str__(self):
        return self.name