from django.contrib import admin
from clutch.models import ClutchRecData, File
from clutch.models import Question
from clutch.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

class FileInline(admin.StackedInline):
    model = File
    extra = 0
    
class ClutchRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline,FileInline]

class FileAdmin(admin.ModelAdmin):
    list_display = ('file',)
	
	
admin.site.register(ClutchRecData,ClutchRecDataAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
