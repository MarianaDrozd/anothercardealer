import django.utils.timezone
from django.contrib.auth import get_user_model
from django.db import models

AUTH_USER_MODEL = get_user_model()


# Create your models here.


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
    )

    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        null=True
    )

    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
    )

    ENGINE_TYPE_STRAIGHT = 'straight'
    ENGINE_TYPE_INLINE = 'inline'
    ENGINE_TYPE_FLAT = 'flat'
    ENGINE_TYPE_V = 'v'

    ENGINE_TYPES = (
        (ENGINE_TYPE_STRAIGHT, 'Straight'),
        (ENGINE_TYPE_INLINE, 'Inline'),
        (ENGINE_TYPE_FLAT, 'Flat'),
        (ENGINE_TYPE_V, 'V')
    )

    engine_type = models.CharField(
        max_length=75,
        choices=ENGINE_TYPES,
        default=ENGINE_TYPE_STRAIGHT,
    )

    POLLUTANT_CLASS_Aa = "class A+"
    POLLUTANT_CLASS_A = "class A"
    POLLUTANT_CLASS_B = "class B"
    POLLUTANT_CLASS_C = "class C"
    POLLUTANT_CLASS_D = "class D"
    POLLUTANT_CLASS_E = "class E"
    POLLUTANT_CLASS_F = "class F"
    POLLUTANT_CLASS_G = "class G"

    POLLUTANT_CLASS_CHOICES = (
        (POLLUTANT_CLASS_Aa, "A+"),
        (POLLUTANT_CLASS_A, "A"),
        (POLLUTANT_CLASS_B, "B"),
        (POLLUTANT_CLASS_C, "C"),
        (POLLUTANT_CLASS_D, "D"),
        (POLLUTANT_CLASS_E, "E"),
        (POLLUTANT_CLASS_F, "F"),
        (POLLUTANT_CLASS_G, "G"),
    )
    pollutant_class = models.CharField(
        max_length=30,
        choices=POLLUTANT_CLASS_CHOICES,
        default=POLLUTANT_CLASS_Aa,
        blank=True
    )

    price = models.PositiveIntegerField(default=0)

    property = models.ManyToManyField('cars.Property')

    fuel_type = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
        related_name='cars'
    )

    STATUS_PENDING = 'pending'
    STATUS_PUBLISHED = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending Car Sell"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    slug = models.SlugField(max_length=75)

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True
    )
    doors = models.SmallIntegerField(default=4)

    capacity = models.PositiveIntegerField(default=0)

    MECHANICAL = 'mechanical'
    AUTOMATIC = 'automatic'
    VARIATOR = 'variator'
    ROBOTIC = 'robotic'

    GEAR_CASES = (
        (MECHANICAL, 'Mechanical'),
        (AUTOMATIC, 'Automatic'),
        (VARIATOR, 'Variator'),
        (ROBOTIC, 'Robotic')
    )

    gear_case = models.CharField(
        max_length=75,
        choices=GEAR_CASES,
        default=AUTOMATIC)

    number = models.CharField(max_length=30)

    sitting_place = models.PositiveSmallIntegerField(default=4)

    first_registration_date = models.DateTimeField(default=django.utils.timezone.now)

    engine_power = models.PositiveIntegerField(default=0)

    picture = models.ForeignKey('cars.Picture', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.slug


class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Model(models.Model):
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Property(models.Model):
    CATEGORY_0 = 'Quadricycle'
    CATEGORY_A = 'Mini'
    CATEGORY_B = 'Small'
    CATEGORY_C = 'Medium'
    CATEGORY_D = 'Large'
    CATEGORY_E = 'Executive'
    CATEGORY_F = 'Luxury'
    CATEGORY_S = 'Sports coupes'
    CATEGORY_M = 'Multi purpose'
    CATEGORY_J = 'Sport utility'

    CATEGORY_CHOICES = (
        (CATEGORY_0, 'Quadricycle'),
        (CATEGORY_A, 'Mini'),
        (CATEGORY_B, 'Small'),
        (CATEGORY_C, 'Medium'),
        (CATEGORY_D, 'Large'),
        (CATEGORY_E, 'Executive'),
        (CATEGORY_F, 'Luxury'),
        (CATEGORY_M, 'Multi purpose'),
        (CATEGORY_J, 'Sport utility'),
    )

    name = models.CharField(max_length=75)

    category = models.CharField(
        max_length=75,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_0,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class FuelType(models.Model):
    FUEL_TYPE_PETROL = 'petrol'
    FUEL_TYPE_DIESEL = 'diesel'
    FUEL_TYPE_ELECTRIC = 'electric'

    FUEL_TYPE_CHOICES = (
        (FUEL_TYPE_PETROL, 'Petrol'),
        (FUEL_TYPE_DIESEL, 'Diesel'),
        (FUEL_TYPE_ELECTRIC, 'Electric')
    )

    fueltype = models.CharField(
        max_length=30,
        choices=FUEL_TYPE_CHOICES,
        default=FUEL_TYPE_PETROL,
    )

    def __str__(self):
        return self.fueltype

    class Meta:
        verbose_name = 'Fuel Type'
        verbose_name_plural = 'Fuel Types'


class Picture(models.Model):
    url = models.ImageField(
        upload_to='static/pictures',
        max_length=255,
        null=True,
        blank=True,
    )
    position = models.IntegerField()
    metadata = models.TextField()

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
