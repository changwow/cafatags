from django.contrib import admin
from .models import Tags
from .models import Txt

class txtAdmin(admin.ModelAdmin):
	list_display = ('title','tag','subTitle')
	search_fields = ('title',)

admin.site.register(Tags)
admin.site.register(Txt, txtAdmin)
# Register your models here.
