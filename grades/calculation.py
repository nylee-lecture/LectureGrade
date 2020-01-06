from django.shortcuts import render

from grades.models import GradeData

## 등수, 평균점수 계산 클래스
class Calcualtion():

    ## 평균점수 계산 함수
     # term은 'mid' 또는 'final' 선택 필수
    def getAverage(lecture, year, semester, term):
        data = GradeData.objects.filter(lecture = lecture, year = year, semester = semester)
        average = 0

        if term is "mid":
            mid_term = 0
            for score in data:
                mid_term += score.mid_term
                # print(mid_term)
            average = mid_term / len(data)

        else:
            final_term = 0
            for score in data:
                final_term += score.final_term
                # print(mid_term)
            average = final_term / len(data)

        return round(average, 2)


    def getMyPosition(sid, lecture, year, semester, term):


        total_data = ''
        my_data=''
        if term is "mid":
            total_data = GradeData.objects.filter(lecture = lecture, year = year, semester = semester).order_by('-mid_term')
            my_data = GradeData.objects.filter(sid = sid, lecture=lecture, year=year, semester=semester).order_by('mid_term')
        else:
            total_data = GradeData.objects.filter(lecture=lecture, year=year, semester=semester).order_by('-final_term')
            my_data = GradeData.objects.filter(sid=sid, lecture=lecture, year=year, semester=semester).order_by('final_term')

        # print(total_data)
        total_list = []
        for score in total_data:
            if term is 'mid':
                total_list.append(score.mid_term)
            else:
                total_list.append(score.final_term)

        myPostion = 1
        if term is 'mid':
            for i in range(len(total_list)):
                if my_data[0].mid_term < total_list[i]:
                    myPostion = myPostion + 1
        else:
            for i in range(len(total_list)):
                if my_data[0].final_term < total_list[i]:
                    myPostion = myPostion + 1

        return myPostion