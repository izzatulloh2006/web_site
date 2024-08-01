from django.contrib import admin
from .models import React
from django.utils.safestring import mark_safe
from apps.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.proxies import AdminUserProxy


admin.site.register(React)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("phone_number", "image_tag", "first_name", "last_name", "is_staff", 'type')
    fieldsets = (
        (None, {"fields": ("type", "phone_number", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", 'photo')}),
        (
            _("Permissions"),
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def image_tag(self, obj):
        if obj.photo:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return '-'

    image_tag.short_description = 'Image'

    def custom_image(self, obj: User):
        return mark_safe('<img src="{}"/>'.format(obj.photo.url))

    custom_image.short_description = "Image"

    def get_course_count(self, obj):
        return obj.course_set.count()

    # def small_image(self, obj):
    #     return '<img src="%s" style="max-width:100px; max-height:100px" />' % obj.image.url
    #
    # small_image.allow_tags = True

    @admin.register(AdminUserProxy)
    class CustomAdminUserProxyAdmin(UserAdmin):
        list_display = ("phone_number", 'photo', "first_name", "last_name", "is_staff")
        fieldsets = (
            (None, {"fields": ("type", "phone_number", "password")}),
            (_("Personal info"), {"fields": ("first_name", "last_name", 'photo')}),
            (
                _("Permissions"),
                {
                    'fields': (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        )

        def get_queryset(self, request):
            return super().get_queryset(request).filter(type=User.UserType.ADMIN)

        def image_tag(self, obj):
            if obj.photo:
                return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
            return '-'

        image_tag.short_description = 'Image'

        def get_course_count(self, obj):
            return obj.course_set.count()
