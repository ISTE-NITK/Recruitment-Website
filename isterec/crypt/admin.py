from django.contrib import admin
from crypt.models import CryptRecData
from crypt.models import File

class FileInline(admin.StackedInline):
    model = File
    
class CryptRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [FileInline]

class FileAdmin(admin.ModelAdmin):
    list_display = ('file',)
	
admin.site.register(CryptRecData,CryptRecDataAdmin)
admin.site.register(File, FileAdmin)
