from django.contrib import admin
from chronicle.models import ChronicleRecData
from chronicle.models import Question
from chronicle.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0

    
class ChronicleRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

admin.site.register(ChronicleRecData,ChronicleRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
