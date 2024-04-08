from django.db import models
from django import forms
import datetime
from account.models import CustomUser

YEAR_CHOICES = [(year, str(year)) for year in range(1960, int(datetime.date.today().year))]

class YearField(models.Field):
    description = "A field to store years only"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('choices', YEAR_CHOICES)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('null', True)
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'IntegerField'

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        if value is None or isinstance(value, int):
            return value
        return int(value)

    def get_prep_value(self, value):
        if value is None:
            return None
        return str(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': YearFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class YearFormField(forms.TypedChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['coerce'] = int
        kwargs['choices'] = YEAR_CHOICES
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        value = super().to_python(value)
        if value in self.empty_values:
            return None
        return value

class TempUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    user_agent = models.CharField(max_length=50)
    device_family = models.CharField(max_length=255)
    device_brand = models.CharField(max_length=255,null=True)
    device_model = models.CharField(max_length=255,null=True)
    browser_family = models.CharField(max_length=255,null=True)
    browser_version_string = models.CharField(max_length=255,null=True)
    device_os_family = models.CharField(max_length=255,null=True)
    device_os_version_string = models.CharField(max_length=255,null=True)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_touch_capable = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    is_bot = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Temporary users"

    def __str__(self):
        return self.device_family

class Car(models.Model):
    price = models.PositiveIntegerField()
    make = models.CharField(max_length=100, choices=None)
    model = models.CharField(max_length=100, blank=True)
    year = YearField()
    size_of_engine = models.CharField(max_length=50, choices=[
        ("1000cm dan kichik","1000cm dan kichik"),
        ("1000cm dan - 2000cm gacha","1000cm dan - 2000cm gacha"),
        ("2000cm dan - 3000cm gacha","2000cm dan - 3000cm gacha"),
        ("3000cm dan - 3500cm gacha","3000cm dan - 3500cm gacha"),
        ("3500cm dan katta","3500cm dan katta")
        #("3000cm dan katta","3000cm dan katta")
    ])
    type_of_car = models.CharField(max_length=20, choices=[
        ("Benzin-Dizel","Benzin-Dizel"),
        ("Elektr-Gibrid","Elektr-Gibrid")
    ])
    result_price = models.IntegerField(default=0, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

