from django.contrib import admin
from charge.models import ChargeRecData
from charge.models import Question
from charge.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

    
class ChargeRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

admin.site.register(ChargeRecData,ChargeRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
