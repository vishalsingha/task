from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Intern Assignment"
admin.site.site_title = "Intern Assignment"
admin.site.index_title = "Welcome to Food Admin Panel"



from django.utils.html import format_html


admin.site.register(KidTable)
# admin.site.register(ImageTable)


@admin.register(ImageTable) 
class ImageTableAdmin(admin.ModelAdmin):
    fields = ['kid', 'image_url', 'image_tag', 'created_on', 'updated_on', 'approved_by', 'Food_group']
    readonly_fields = ['image_tag', 'updated_on']
    radio_fields = {"Food_group": admin.HORIZONTAL}
    list_display = ('image_url', 'image_tag', 'created_on', 'updated_on', 'is_approved', 'approved_by', 'Food_group')
    # def save_model(self, request, obj, form, change):
    #     obj.approved_by = request.user
    #     obj.save()


