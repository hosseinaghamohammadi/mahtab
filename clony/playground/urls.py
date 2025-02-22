from django.urls import path

from . import views

urlpatterns = [
    path("ins/", views.t),
    path("req/", views.create_problem),
    path("task_bank/", views.problem_bank),
    # path("filter_tasks/", views.filter_tasks),
    # path("cs_classes/", views.cs_classes),
    # path("submit_problem_answer/", views.submit_problem_answer),
    # path("submit_activity_answer/", views.submit_event_activity_answer),
    path("homepage/", views.public_homepage, name="home"),
    path("adventure/", views.event_homepage),
    path("api/journey-details/", views.journey_details),
    path("journey/", views.journey_page),
    path("adventure/problem/<int:problem_index>/", views.problem_page),
    path("adventure/activity/<int:activity_index>/", views.activity_page),
    path("submit_event_problem_answer", views.submit_event_problem_answer),
    path("submit_event_activity_answer", views.submit_event_activity_answer),
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    path("logout/", views.logout_receiver),
    path("my_projects", views.my_projects),
    # path("small_dimensions/", views.small_dimensions),
    path("", views.empty_redirect),
]

