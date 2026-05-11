from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Team', {'fields': ('team',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Team', {'fields': ('team',)}),
    )
    list_display = UserAdmin.list_display + ('team',)

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
