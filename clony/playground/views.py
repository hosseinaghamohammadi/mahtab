from datetime import datetime
from datetime import timedelta

from django.db.models import F
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import (Student,
                     Problem,
                     ProblemAttempt,
                     User,
                     InteractiveActivity,
                     Station,
                     StationBasedEvent,
                     InteractiveAttempt,
                     StationProblem,
                     StationInteractiveActivity,
                     EventAttempt,
                     )
from .serializers import StationSerializer
from .forms import UserCreationForm, SignUpFrom, LogInForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.sessions.models import Session

filter_mapping_db_to_template = {
    'hard': 'جاافتاده',
    'medium': 'آشنا',
    'easy': 'مبتدی',
    '1': 'اول',
    '2': 'دوم',
    '3': 'سوم',
    '4': 'چهارم',
    '5': 'پنجم',
    '6': 'ششم',
    '7': 'هفتم',
    '8': 'هشتم',
    '9': 'نهم',
    '10': 'دهم',
    '11': 'یازدهم',
    '12': 'دوازدهم',
}
filter_mapping_template_to_db = {
    'جاافتاده': 'hard',
    'آشنا': 'medium',
    'مبتدی': 'easy',
    'اول': '1',
    'دوم': '2',
    'سوم': '3',
    'چهارم': '4',
    'پنجم': '5',
    'ششم': '6',
    'هفتم': '7',
    'هشتم': '8',
    'نهم': '9',
    'دهم': '10',
    'یازدهم': '11',
    'دوازدهم': '12',
}


def check_activity_1(request):
    challenge_type = request.POST['type']
    result = request.POST['result']
    id = request.POST['id']
    submission = request.POST['submission']
    if challenge_type == 'activity':
        if id == '1':
            if result == '1':
                return True
            else:
                return False


def check_activity_2(request):
    challenge_type = request.POST['type']
    result = request.POST['result']
    id = request.POST['id']
    submission = request.POST['submission']
    if challenge_type == 'activity':
        if id == '2':
            if result == '1':
                return True
            else:
                return False


def check_activity_3(submission):
    pass


def check_activity_4(submission):
    pass


activity_submission_check = {
    '1': check_activity_1,
    '2': check_activity_2,
    '3': check_activity_3,
    '4': check_activity_4
}


def t(request):
    return render(request, 'instruction.html')


# post request
def create_problem(request):
    if request.method == 'POST':
        print(request.POST['txt'])
        # if request.POST['activity']:
        #     pass
        # else:
        p = Problem(name='test',
                    description='testing',
                    grades_and_difficulty='1-hard,2-medium',
                    problem_statement=request.POST['txt'],
                    type=1,
                    source_type=2)
        p.save()
        return render(request, 'instruction.html')


@login_required
def problem_bank(request):
    whole_string = []
    filters = request.GET.get('constraints')
    problems_list = Problem.objects.all()
    if filters:
        for f in filters.split('، '):
            print(f)
            whole_string.append(filter_mapping_template_to_db[f])
        whole_string = '-'.join(whole_string)
        print(whole_string)
        problems_list = Problem.objects.filter(grades_and_difficulty__contains=whole_string)

    seven_days_ago = datetime.now() - timedelta(minutes=1)
    user = request.user
    recent_attempts = ProblemAttempt.objects.filter(student=user, created_at__gte=seven_days_ago).values_list('problem_id', flat=True)
    print(recent_attempts)
    tasks_to_show = problems_list.exclude(id__in=recent_attempts)
    print(tasks_to_show)
    answered_tasks = ProblemAttempt.objects.filter(student=user).values_list('problem_id', flat=True)
    print(answered_tasks)
    return render(request, 'single-task.html', {'tasks': tasks_to_show, 'answered_tasks': answered_tasks})
    # return render(request, 'single-task.html', {'tasks': Problem.objects.all()})


@login_required
def filter_tasks(request):
    return render(request, 'filter-tasks.html', {'tasks': Problem.objects.all()})


def cs_classes(request):
    return render(request, 'cs-classes.html')


@login_required
def submit_problem_answer(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        user_choice = request.POST['user_choice']
        task = Problem.objects.get(pk=int(task_id))

        if task.type == 'multiple choice-text':

            attempt = ProblemAttempt(
                problem=task,
                student=request.user,
                student_answer=user_choice,
                score_type='solving'
            )

            message = ''
            if user_choice == task.answer:
                message = 'positive'
                attempt.is_correct = True
                attempt.score = 36
                print('correct!')
            else:
                message = 'negative'
                attempt.is_correct = False
                attempt.score = 0
                print('wrong!')

            response_data = {
                'status': 'success',
                'message': message,
                'task_id': task.id,
                'user_choice': user_choice
            }
            attempt.save()
            return JsonResponse(response_data)
        else:
            return JsonResponse({'status': 'error', 'message': 'invalid task type'})
    else:
        return JsonResponse({'status': 'error', 'message': 'invalid request'})


@login_required
def submit_activity_answer(request):
    pass


##############################################################################


def get_progress(user):
    print('started')
    stations = Station.objects.filter(event__name__contains='1403 Winter').order_by('order')

    solved_stations = []
    current_station = None
    next_problem = None
    next_activity = None

    for station in stations:
        problems = StationProblem.objects.filter(station=station).order_by('order')
        activities = StationInteractiveActivity.objects.filter(station=station).order_by('order')

        all_problems_solved = all(
            EventAttempt.objects.filter(
                participant=user,
                problem=sp.problem,
                station=station,
                is_correct=True
            ).exists()
            for sp in problems
        )

        all_activities_solved = all(
            EventAttempt.objects.filter(
                participant=user,
                interactive_activity=sa.activity,
                station=station,
                is_correct=True
            ).exists()
            for sa in activities
        )

        if all_problems_solved and all_activities_solved:
            solved_stations.append(station)
        else:
            current_station = station
            for i, sp in enumerate(problems):
                if not EventAttempt.objects.filter(
                        participant=user,
                        problem=sp.problem,
                        station=station,
                        is_correct=True
                ).exists():
                    next_problem = (i, sp.problem)
                    break
            for i, sa in enumerate(activities):
                if not EventAttempt.objects.filter(
                        participant=user,
                        interactive_activity=sa.activity,
                        station=station,
                        is_correct=True
                ).exists():
                    next_activity = (i, sa.activity)
                    break
            break
    
    return solved_stations, current_station, next_problem, next_activity


# get request
@login_required
def event_homepage(request):
    # the page the user sees after logging in
    # seeing the progress in stations and "resume journey" button

    if request.method == 'GET':
        return render(request, 'homepage.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'invalid request'})


def public_homepage(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/adventure_in_close_land/')
        else:
            return render(request, 'public_homepage.html')
    else:
        return JsonResponse({'status': 'error', 'message': 'invalid request'})


# get request
@login_required
def journey_page(request):
    # the page the user sees after clicking on "resume journey" button
    # showing the current station, next problem, and solved stations
    return render(request, 'journey-details.html')


# post request
@login_required
def submit_event_problem_answer(request):
    user = request.user
    if request.method == 'POST':
        problem_id = request.POST['problem_id']
        user_submission = request.POST['user_choice']
        problem = Problem.objects.get(id=int(problem_id))

        result = (problem.answer == user_submission)

        attempt = EventAttempt(
            participant=user,
            station=StationProblem.objects.get(problem__id=problem_id).station,
            problem=problem,
            interactive_activity=None,
            is_problem=True,
            is_correct=result,
            student_answer=user_submission,
        )
        attempt.save()

        response_data = {
            'status': 'success',
            'message': 'positive' if result else 'negative',
            'problem_id': problem_id,
            'user_submission': user_submission,
        }
        return JsonResponse(response_data)

    return JsonResponse({'status': 'error', 'message': 'invalid request'})


# post request
@login_required
def submit_event_activity_answer(request):
    user = request.user
    if request.method == 'POST':
        activity_id = int(request.POST['id'])
        user_submission = request.POST['submission']

        check_activity = activity_submission_check.get(str(activity_id))

        if check_activity:
            is_correct = check_activity(request)

            solved_stations, current_station, next_problem, next_activity = get_progress(request.user)

            attempt = EventAttempt(
                participant=user,
                # according to next line, each activity has to be assigned to one and only one station
                # it is changed so that you can assign each activity to multiple stations
                station=current_station,
                # next line is changed in a way that if the activity is not associated with the station, it behaves
                # like a problem
                interactive_activity=StationInteractiveActivity.objects.get(station=current_station, activity__id=activity_id).activity,
                # InteractiveActivity.objects.get(id=activity_id),
                problem=None,
                is_problem=False,
                is_correct=is_correct,
                student_answer=user_submission,
            )
            attempt.save()

            response_data = {
                'status': 'success',
                'message': 'positive' if is_correct else 'negative'
                # 'activity_id': activity_id,
                # 'user_submission': user_submission,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'status': 'error', 'message': 'activity not found'})

    return JsonResponse({'status': 'error', 'message': 'invalid request'})


@login_required
def problem_page(request, problem_index):
    if request.method == 'GET':
        solved_stations, current_station, next_problem, next_activity = get_progress(request.user)
        station_problems = StationProblem.objects.filter(station=current_station).order_by('order')
        problem = Problem.objects.get(id=station_problems[problem_index].problem.id)
        return render(request, 'event_problem_page.html', {'tasks': [problem], 'answered_tasks': []})


@login_required
def activity_page(request, activity_index):
    if request.method == 'GET':
        solved_stations, current_station, next_problem, next_activity = get_progress(request.user)
        station_activities = StationInteractiveActivity.objects.filter(station=current_station).order_by('order')
        activity = InteractiveActivity.objects.get(id=station_activities[activity_index].activity.id)
        print(activity)
    return render(request, f'{activity.html_file_name}.html', {'activity': activity})


# API for the journey page
@login_required
def journey_details(request):
    # the data for the journey page details (current station, next problem, and solved stations)
    # the data is sent as a JSON response

    # current_station_serializer, solved_stations_serializer, next_problem_index
    # current_station, solved_stations, next_problem_index

    user = request.user
    solved_stations, current_station, next_problem, next_activity = get_progress(user)

    # serializing solved stations and append them to a list
    solved_stations_serialized = []
    for s in solved_stations:
        solved_stations_serialized.append(StationSerializer(s).data)

    # serializing the current station
    current_station_serialized = StationSerializer(current_station).data
    # f = open('t.txt', 'w', encoding='utf-8')
    # f.write(current_station, next_problem, next_activity, solved_stations)
    # f.close()
    return JsonResponse({'current_station': current_station_serialized,
                         'next_problem_index': next_problem[0] if next_problem else -1,
                         'next_activity_index': next_activity[0] if next_activity else -1,
                         'solved_stations': solved_stations_serialized,
                         })


def not_found(request, p):
    return HttpResponse('423')


# get request
def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/homepage')
        else:
            form = LogInForm()
            return render(request, 'login-page.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            request.session['username'] = username
            request.session.save()
            return render(request, 'homepage.html', {'user': user})
        else:
            return render(request, 'login-page.html', {'login_error': 'wrong username or password.'})
    else:
        return HttpResponse('request method is not valid')


def signup_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/adventure_in_close_land/')
        else:
            form = SignUpFrom()
            return render(request, 'signup-page.html', {'form': form})
    elif request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/adventure_in_close_land')
        else:
            form = SignUpFrom(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                # print(username, raw_password)
                user = authenticate(username=username, password=raw_password)
                if user:
                    user.save()
                    auth_login(request, user)
                    return redirect('/adventure_in_close_land/')
                else:
                    return HttpResponse('no user error!')
            else:
                return HttpResponse(form.error_messages)
    else:
        return HttpResponse('request method is not valid')


def logout_receiver(request):
    auth_logout(request)
    Session.objects.filter(session_key=request.session.session_key).delete()
    return redirect('/')


def empty_redirect(request):
    if request.method == 'GET':
        return redirect('/homepage')


def small_dimensions(request):
    return render(request, 'small-dimensions.html')