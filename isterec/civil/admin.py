from django.contrib import admin
from civil.models import CivilRecData
from civil.models import Question
from civil.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

    
class CivilRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

admin.site.register(CivilRecData,CivilRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
