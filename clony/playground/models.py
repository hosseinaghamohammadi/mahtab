from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)


class Admin(User):
    role = models.CharField(max_length=20, null=True, blank=True, choices=(
        (1, 'coordinator'),
        (2, 'event staff'),
        (3, 'admin'),
    ))


class Student(models.Model):
    # username, first_name, last_name, email, password, phone_number
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    grade = models.IntegerField(default=0, null=True, blank=True)
    coins = models.IntegerField(default=0, null=True, blank=True)

    # participation with problemSelection Query
    # notes = models.TextField(blank=True, null=True)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)

    note = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class StationBasedEvent(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    audience = models.CharField(max_length=1000, blank=True, null=True)

    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    grades_and_difficulty = models.CharField(max_length=200, blank=True, null=True)
    problem_statement = models.TextField(blank=True, null=True)
    topic_tags = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True, choices=(
        ('input-integer', 'input-integer'),                         # active
        ('input-text', 'input-text'),                               # active
        ('multiple choice-text', 'multiple choice-text'),           # active
        ('multiple choice-image', 'multiple choice-image'),         # ------
        ('multiple selection-text', 'multiple selection-text'),     # active
        ('multiple selection-image', 'multiple selection-image'),   # ------
        ('interactive', 'interactive')                              # ------
    ))
    source_type = models.CharField(max_length=200, blank=True, null=True, choices=(
        ('translation', 'translation'),
        ('designed', 'designed')
    ))
    answer = models.CharField(max_length=200, blank=True, null=True)
    text_choices = models.TextField(max_length=1000, blank=True, null=True)

    note = models.TextField(blank=True, null=True)


class InteractiveActivity(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    grades_and_difficulty = models.CharField(max_length=200, blank=True, null=True)
    problem_statement = models.TextField(blank=True, null=True)
    topic_tags = models.CharField(max_length=300, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    html_file_name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    note = models.TextField(blank=True, null=True)


class StationProblem(models.Model):
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('station', 'problem')


class StationInteractiveActivity(models.Model):
    station = models.ForeignKey('Station', on_delete=models.CASCADE)
    activity = models.ForeignKey('InteractiveActivity', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('station', 'activity')


class Station(models.Model):
    event = models.ForeignKey(StationBasedEvent, on_delete=models.CASCADE, blank=True, null=True)
    problems = models.ManyToManyField(Problem, through=StationProblem, blank=True, null=True)
    activities = models.ManyToManyField(InteractiveActivity, through=StationInteractiveActivity, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    note = models.TextField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ProblemAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, blank=True, null=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, blank=True, null=True)
    student_answer = models.CharField(max_length=400, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    score_type = models.CharField(max_length=200, blank=True, null=True)    # [solving, designing]
    score = models.IntegerField(default=0)

    note = models.TextField(blank=True, null=True)


class InteractiveAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, blank=True, null=True)
    activity = models.ForeignKey(InteractiveActivity, on_delete=models.CASCADE, blank=True, null=True)
    student_answer = models.CharField(max_length=400, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    score_type = models.CharField(max_length=200, blank=True, null=True)
    score = models.IntegerField(default=0)

    note = models.TextField(blank=True, null=True)


class EventAttempt(models.Model):
    participant = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    station = models.ForeignKey(Station, models.CASCADE, blank=True, null=True)
    problem = models.ForeignKey(Problem, models.CASCADE, blank=True, null=True)
    interactive_activity = models.ForeignKey(InteractiveActivity, models.CASCADE, blank=True, null=True)

    is_problem = models.BooleanField(blank=True, null=True)

    student_answer = models.CharField(max_length=1000, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    note = models.TextField(blank=True, null=True)








class ProblemSelection(models.Model):
    problems = models.ManyToManyField(Problem)
    title = models.CharField(primary_key=True, max_length=200)
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Problem Selection'
        verbose_name_plural = 'Problem Selections'


class Quiz(ProblemSelection):
    is_quiz = models.BooleanField(default=False)
    pass


class Institution(User):
    name = models.CharField(max_length=200, blank=True, null=True)
    k12_section = models.CharField(max_length=200, blank=True, null=True, choices=(
        (1, '(1-6)'),
        (2, '(7-9)'),
        (3, '(10-12)'),
        (4, '(1-9'),
        (5, '(7-12'),
        (6, '1-12')
    ))
    province = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True, choices=(
        (1, 'female'),
        (2, 'male')
    ))
    address = models.TextField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'


class Classroom(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)


class Challenge(ProblemSelection):
    organizer = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    is_challenge = models.BooleanField(default=False)


class Note(models.Model):
    author = models.ForeignKey(Admin, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
