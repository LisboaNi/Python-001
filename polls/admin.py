from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline): # Layout 1
class ChoiceInline(admin.TabularInline): #Layout 2
    model = Choice
    extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"] #Ou Ordenar campos - Forms

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ #Ou Classificar em Grupos - Forms
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}), 
    ]
    inlines = [ChoiceInline] #Relacionamento
    list_display = ["question_text", "pub_date", "was_published_recently"] #Ordem das colunas
    list_filter = ["pub_date"] #Barra de filtro

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)