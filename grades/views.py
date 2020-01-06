from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import User
from grades.models import GradeData
from .calculation import Calcualtion
from tablib import Dataset
from .resources import GradeResource


def index(request):
    # print(request.session['sid'])
    if request.method == 'POST':
        print("post")
        print(request.user)
    else:
        print("get")


    # if request.user is not 'AnonymousUser':
    #     sid = "none"
    # else:
    #     sid = request.user.username

    # if request.POST['username']:
    #     sid = request.POST['username']
    #     print(sid)
    # request.session['sid'] = sid
    return render(request, 'index.html')

def result(request):
    print(request.user.username)
    if request.user.is_authenticated:
        user_grades = GradeData.objects.filter(sid=request.user.username)
        # print(user_grades)
        if user_grades:
            print("ok")
        else:
            print("no")

        i = 0
        mid_average = []
        final_average = []
        mid_myPostion = []
        final_myPostion = []

        for i in range(len(user_grades)):
            temp = Calcualtion.getAverage(lecture=user_grades[i].lecture, year=user_grades[i].year, semester=user_grades[i].semester, term="mid")
            # i += 1
            mid_average.append(temp)

        for i in range(len(user_grades)):
            temp = Calcualtion.getAverage(lecture=user_grades[i].lecture, year=user_grades[i].year, semester=user_grades[i].semester, term="final")
            # i += 1
            final_average.append(temp)

        for i in range(len(user_grades)):
            temp = Calcualtion.getMyPosition(sid=user_grades[i].sid, lecture=user_grades[i].lecture, year=user_grades[i].year, semester=user_grades[i].semester, term="mid")
            mid_myPostion.append(temp)

        for i in range(len(user_grades)):
            temp = Calcualtion.getMyPosition(sid=user_grades[i].sid, lecture=user_grades[i].lecture, year=user_grades[i].year, semester=user_grades[i].semester, term="final")
            final_myPostion.append(temp)

        mylist = zip(user_grades, mid_average, final_average, mid_myPostion, final_myPostion)
        context = {'grade_list': mylist}
        # print(context)
        # lecture_info = lecture_info.split()


    return render(request, 'result.html', context)

def simple_upload(request):
    if request.method == 'POST':
        grade_resource = GradeResource()
        dataset = Dataset()
        new_grades = request.FILES['myfile']

        imported_data = dataset.load(new_grades.read())
        result = grade_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            grade_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'simple_upload.html')