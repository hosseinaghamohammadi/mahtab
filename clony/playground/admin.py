from django.contrib import admin
from .models import (
    User,
    Student,
    Institution,
    Classroom,
    Problem,
    ProblemSelection,
    ProblemAttempt,
    InteractiveAttempt,
    Station,
    StationBasedEvent,
    EventAttempt,
    InteractiveActivity,
    StationProblem,
    StationInteractiveActivity,
    Project,
)
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    model = Student
    extra = 2
    list_display = ['user__username', 'province', 'user__last_name', 'user__first_name', 'user__email', 'date_of_birth']
    list_filter = ['province', 'date_of_birth']
    # search_fields = ('user', 'dob', 'public_token', 'access_token', 'item_id', )
    # ordering = ('user', )
    # list_select_related = ('user', )


class StationProblemInline(admin.TabularInline):
    model = StationProblem
    extra = 1


class StationInteractiveActivityInline(admin.TabularInline):
    model = StationInteractiveActivity
    extra = 1


class StationAdmin(admin.ModelAdmin):
    inlines = (StationProblemInline, StationInteractiveActivityInline,)


admin.site.register(Student, StudentAdmin)
admin.site.register(User)
admin.site.register(InteractiveActivity)
admin.site.register(InteractiveAttempt)
admin.site.register(EventAttempt)
admin.site.register(Station, StationAdmin)
admin.site.register(StationBasedEvent)
# admin.site.register(Student)
# admin.site.register(Institution)
# admin.site.register(Classroom)
admin.site.register(Problem)
# admin.site.register(ProblemSelection)
admin.site.register(ProblemAttempt)
admin.site.register(Project)

