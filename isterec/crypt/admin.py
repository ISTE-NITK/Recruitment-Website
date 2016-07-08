from django.contrib import admin
from crypt.models import CryptRecData
from crypt.models import File, Question, Answer

class FileInline(admin.StackedInline):
    model = File
    extra = 0

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
	
class CryptRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline,FileInline]

class FileAdmin(admin.ModelAdmin):
    list_display = ('file',)
	
admin.site.register(CryptRecData,CryptRecDataAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Question)
admin.site.register(Answer)