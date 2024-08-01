from django.utils.translation import gettext_lazy as _
from apps.models import User


class AdminUserProxy(User):
    class Meta:
        proxy = True
        verbose_name = _("Admin")
        verbose_name_plural = _("Admins")

