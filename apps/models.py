import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import (TextChoices, UUIDField, CharField,
                              PositiveIntegerField, BooleanField,
                              ImageField, Model, TextField, IntegerField,
                              ForeignKey, CASCADE, SmallIntegerField)
from django.core.validators import RegexValidator


class User(AbstractUser):
    class UserType(TextChoices):
        Admin = 'admin', _('Admin')
        NewUser = 'newuser', _('New User')
        Motorist = 'motorist', _('Motorist')
        Xodovoy = 'xodovoy', _('Xodovoy')
        Elektirk = 'elektrik', _('Elektirik')
        Svarchik = 'svarshik', _('Svarshik')
        Razvalshik = 'razvalshik', _('Razvalshik')
        Avto_dokonchi = 'avto_dokon', _('Avto dokon')

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    type = CharField(verbose_name=_('user_type'), max_length=50, choices=UserType.choices, default=UserType.NewUser)
    phone_number = CharField(validators=[RegexValidator(
        regex=r'^\d{9}$',
        message="Phone number must be entered in the format: '9999998'."        "Up to 12 digits allowed.")],
        max_length=20, unique=True)
    username = CharField(max_length=255, unique=False)
    tg_id = CharField(max_length=255, unique=True, blank=False, null=True)
    balance = PositiveIntegerField(default=0, verbose_name=_('balance'))
    bot_options = CharField(max_length=255, null=True, blank=True, verbose_name=_('bot options'))
    has_registered_bot = BooleanField(default=False)
    not_read_message_count = PositiveIntegerField(default=0)
    payme_balance = PositiveIntegerField(default=0)
    photo = ImageField(upload_to='users/images', default='users/default.jpg', verbose_name=_('Photo'))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def delete(self, using=None, keep_parents=False):
        self.photo.delete(save=False)
        return super().delete(using, keep_parents)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


class Category(Model):
    name = CharField(_('name'), max_length=225)
    title = CharField(_('title'), max_length=500)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(_('name'), max_length=45)
    description = TextField(_('description'), blank=True)
    price = IntegerField(_('price'), default=0)
    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name


class React(Model):
    firstname = CharField(max_length=30)
    lastname = CharField(max_length=30)
    age = SmallIntegerField(default=0)

