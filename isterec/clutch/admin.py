from django.contrib import admin
from clutch.models import ClutchRecData
from clutch.models import Question
from clutch.models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer

    
class ClutchRecDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno','mobileno','email')
    inlines = [AnswerInline]

admin.site.register(ClutchRecData,ClutchRecDataAdmin)
admin.site.register(Question)
admin.site.register(Answer)
# Register your models here.
