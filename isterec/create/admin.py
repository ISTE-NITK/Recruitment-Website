from django.contrib import admin
from create.models import CreateRecData
from create.models import Question
from create.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

    
class CreateRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

    

admin.site.register(CreateRecData,CreateRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
