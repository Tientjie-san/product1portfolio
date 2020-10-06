from django.contrib import admin
from portfolio.models import *
# Register your models here.

class AdresInline(admin.StackedInline):
    model = Adres

class InterestInline(admin.TabularInline):
    model = Interest
    extra = 0

class ImageInline(admin.StackedInline):
    model = Image
    fields = ['image']
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['profile_title', 'first_name', 'last_name', 'birth_date','driver_license']}),
        ('Contact Information', {'fields': ['phone', 'profile_email']}),
    ]
    inlines = [AdresInline, InterestInline, ImageInline]

class DescriptionInline(admin.StackedInline):
    model = Description

class TagInline(admin.TabularInline):
    model = Tag.project.through
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_title', 'live_link', 'github_link', 'date_start', 'date_end', 'profile']})
    ]
    inlines = [DescriptionInline, TagInline, ImageInline]

class TagAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('project',)

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('contact_subject', 'contact_email', 'contact_date')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Work_experience)
admin.site.register(Education)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Social)