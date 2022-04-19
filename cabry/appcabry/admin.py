from django.contrib import admin
from .models import Questionblock, Answeroptionsblock, Questionsweroptionblock, QuestionApiblock, Qstionsweblock, ALLQuestionsweroptionblock


@admin.register(Answeroptionsblock)
class AnsweroptionsblockPanel(admin.ModelAdmin):
    list_display = ['title_answer_options', 'encoding_answer_options']
    pass


@admin.register(Questionblock)
class QuestionblockPanel(admin.ModelAdmin):
    pass


@admin.register(Qstionsweblock)
class QstionsweblockPanel(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
    # pass


@admin.register(ALLQuestionsweroptionblock)
class ALLQuestionsweroptionblockPanel(admin.ModelAdmin):
    # list_display = ['id_title_q', 'id_title_a']
    def get_model_perms(self, request):
        return {}


class Answeroptionsblockinline(admin.TabularInline):
    model = Questionsweroptionblock


class QuestionblockAdmin(admin.ModelAdmin):
    list_display = ['num_qust', 'id_api_question']
    list_filter = ('id_api_question',)
    inlines = [Answeroptionsblockinline]

    class Meta:
        model = QuestionApiblock


admin.site.register(QuestionApiblock, QuestionblockAdmin)


class CatCatalogqustalogqustinline(admin.TabularInline):
    model = Qstionsweblock


class AddCatalogqustAdmin(admin.ModelAdmin):
    list_display = ['id_title_question', 'id_title_answer_options']
    list_filter = ('id_title_question',)
    inlines = [CatCatalogqustalogqustinline]

    class Meta:
        model = Questionsweroptionblock


admin.site.register(Questionsweroptionblock, AddCatalogqustAdmin)


admin.site.site_header = 'Администрирование АИС'
admin.site.site_title = 'Администрирование АИС'
