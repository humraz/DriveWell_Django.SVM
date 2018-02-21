from django.contrib import admin

# Register your models here.
from snipetss.models import Snippet
from snipetss.models import MyPhoto



class snipetadmin(admin.ModelAdmin):
	fields = ('drivername', 'score')
	#list_display= ('title', 'code')
	#list_filter =('title', 'code')
	class Meta:
		model= Snippet



admin.site.register(Snippet, snipetadmin)
class photoadmin(admin.ModelAdmin):
	fields = ('name', 'image')
	#list_display= ('title', 'code')
	#list_filter =('title', 'code')
	class Meta:
		model= MyPhoto

admin.site.register(MyPhoto, photoadmin)
