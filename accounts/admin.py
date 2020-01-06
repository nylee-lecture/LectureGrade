from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'sname', 'joined_at', 'last_login_at', 'is_superuser', 'is_active')
    list_display_links = ('id', 'username')

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    joined_at.admin_order_field = '-date_joined'  # 가장 최근에 가입한 사람부터 리스팅
    joined_at.short_description = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'