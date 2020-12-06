from django.contrib import admin

from members.models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    search_fields = ('email', 'uuid', 'role',)
    ordering = ('email',)
    readonly_fields = ('uuid', 'modified', 'created', 'email')
    list_display = ('email', 'uuid', 'role', 'is_active')
    list_filter = ('is_active', 'role')
    fieldsets = ((None, {'fields': ('uuid', 'email', 'role', 'is_active', 'first_name', 'last_name', 'phone_no', 'created', 'modified')}),)


admin.site.register(TeamMember, TeamMemberAdmin)