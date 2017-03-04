from django.contrib import admin

# Register your models here.
from snipetss.models import Snippet



class snipetadmin(admin.ModelAdmin):
	fields = ('title', 'code')
	#list_display= ('title', 'code')
	#list_filter =('title', 'code')
	class Meta:
		model= Snippet

admin.site.register(Snippet, snipetadmin)
