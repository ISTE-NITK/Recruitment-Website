from django.contrib import admin
from credit.models import CreditRecData
from credit.models import Question
from credit.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

    
class CreditRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

admin.site.register(CreditRecData,CreditRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
