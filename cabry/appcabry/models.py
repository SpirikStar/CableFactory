from django.db import models


class Questionblock(models.Model):
    title_question = models.TextField(
        'Вопрос',
        null=False,
    )

    class Meta:
        verbose_name = ("вопрос")
        verbose_name_plural = ("Добавление вопроса формы")

    def __str__(self):
        return self.title_question


class QuestionApiblock(models.Model):
    num_qust = models.IntegerField(
        'Номер вопроса',
        null=False,
    )
    id_api_question = models.ForeignKey(
        Questionblock, on_delete=models.CASCADE, verbose_name='Вопрос')

    class Meta:
        verbose_name = ("вопрос")
        verbose_name_plural = ("Управление вопросами в форме")

    def __str__(self):
        return self.id_api_question.title_question


class Answeroptionsblock(models.Model):
    title_answer_options = models.TextField(
        'Вариант ответа',
        null=False,
    )
    encoding_answer_options = models.CharField(
        'Кодировка',
        blank=True,
        null=True,
        max_length=50
    )

    class Meta:
        verbose_name = ("вариант ответа")
        verbose_name_plural = ("Управление ответами и вариантностью")

    def __str__(self):
        return self.title_answer_options


class Questionsweroptionblock(models.Model):
    id_title_question = models.ForeignKey(
        QuestionApiblock, on_delete=models.CASCADE, verbose_name='Вопрос')
    id_title_answer_options = models.ForeignKey(
        Answeroptionsblock, on_delete=models.CASCADE, verbose_name='Вариант ответа')

    class Meta:
        verbose_name = ("пункт")
        verbose_name_plural = ("Управление связями и логикой проекта")

    def __str__(self):
        return self.id_title_question.id_api_question.title_question


class ALLQuestionsweroptionblock(models.Model):
    id_title_q = models.ForeignKey(
        QuestionApiblock, on_delete=models.CASCADE, verbose_name='Вопрос')
    id_title_a = models.ForeignKey(
        Answeroptionsblock, on_delete=models.CASCADE, verbose_name='Вариант ответа')

    def __str__(self):
        return self.id_title_q.id_api_question.title_question


class Qstionsweblock(models.Model):
    id_q = models.ForeignKey(Questionsweroptionblock,
                             on_delete=models.CASCADE, verbose_name='Вопрос')
    id_quest = models.ForeignKey(
        ALLQuestionsweroptionblock, on_delete=models.CASCADE, verbose_name='Кому')

    class Meta:
        verbose_name = ("элемент")
        verbose_name_plural = ("Связь и ключ | Шаг")

    def __str__(self):
        return self.id_q.id_title_question.id_api_question.title_question
