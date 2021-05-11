from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.register(models.User,UserAdmin)

UserAdmin.fieldsets[2][1]['fields'] = (
'is_active',
'is_staff',
'is_superuser',
'is_author',
'special_user',
'groups',
'user_permissions',
'branch_Id',
'branch_name'
)
UserAdmin.list_display+=('is_author','branch_Id','branch_name')
