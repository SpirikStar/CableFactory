from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Questionblock, Answeroptionsblock, Questionsweroptionblock, QuestionApiblock, Qstionsweblock, ALLQuestionsweroptionblock

def HomeForm(request):

    all_qust = {}
    for data_qust in QuestionApiblock.objects.all().order_by('num_qust'):
        if data_qust.num_qust == 1:
            all_qust.update({data_qust.num_qust: {data_qust.id_api_question:[i.id_title_answer_options for i in Questionsweroptionblock.objects.filter(id_title_question=data_qust.id)]}})
        else:
            all_qust.update({data_qust.num_qust: data_qust.id_api_question})
    data = {
        'qust': all_qust
    }
    return render(request, 'appcabry/homeMain.html', data)

def HomePostData(request):
    if request.method == 'POST':
        info_title = str(request.POST['nameDataTitleValue']).split('&$&')
        KeyNum = int(info_title[0])
        KeyTitle = int(Questionblock.objects.get(title_question=str(info_title[1])).id)
        DataPodc = int(Answeroptionsblock.objects.get(title_answer_options=str(info_title[2])).id)

        all_qust = {}
        
        countNum = Questionblock.objects.all().count()
        if KeyNum <= countNum:
            KeyNum +=1

        try:
            keyOP = Questionsweroptionblock.objects.get(id_title_question=QuestionApiblock.objects.get(id_api_question=KeyTitle), id_title_answer_options=DataPodc)
            for i in Qstionsweblock.objects.filter(id_q=keyOP):
                obj = ALLQuestionsweroptionblock.objects.get(id=i.id)
                all_qust.update({int(obj.id_title_q.num_qust): {str(obj.id_title_q):[]}})

            for iSet in Qstionsweblock.objects.filter(id_q=keyOP):
                obj = ALLQuestionsweroptionblock.objects.get(id=iSet.id)          
                all_qust[int(obj.id_title_q.num_qust)][str(obj.id_title_q)].append(str(obj.id_title_a))

            return JsonResponse(all_qust)
        except:
            return HttpResponse()

def DataForm(request):
    pass
    if request.method == 'POST':
        res = {}
        rash = {}
        reshjoul = {}
        for data_qust in QuestionApiblock.objects.all().order_by('num_qust'):
            dataUI = f"{data_qust.num_qust}&$&{data_qust.id_api_question}"
            selected_option = str(request.POST.get(str(dataUI), None))
            dataSHOU = selected_option.split('&$&')
            try:
                sh = Answeroptionsblock.objects.get(title_answer_options=str(dataSHOU[2]))
                try:
                    res.update({dataSHOU[0]: sh.encoding_answer_options})
                    reshjoul.update({sh.title_answer_options: sh.encoding_answer_options})
                except:
                    pass
            except:
                return HttpResponse(f'В одном из полей допущена ошибка!')
        for i in Answeroptionsblock.objects.all():
            rash.update({i.title_answer_options:i.encoding_answer_options})
        data = {
            'Res':res,
            'Rash':rash,
            'Decryption':reshjoul
        }

        return render(request, 'appcabry/mainRes.html', data)
