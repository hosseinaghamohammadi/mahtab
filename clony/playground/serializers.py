# serializers.py
from rest_framework import serializers
from .models import Station, Problem, StationProblem, InteractiveActivity, StationInteractiveActivity


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class InteractiveActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveActivity
        fields = '__all__'


class StationInteractiveActivitySerializer(serializers.ModelSerializer):
    activity = InteractiveActivitySerializer()

    class Meta:
        model = StationInteractiveActivity
        fields = ['activity', 'order']


class StationProblemSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()

    class Meta:
        model = StationProblem
        fields = ['problem', 'order']


class StationSerializer(serializers.ModelSerializer):
    problems = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = '__all__'

    def get_problems(self, obj):
        station_problems = StationProblem.objects.filter(station=obj).order_by('order')
        return StationProblemSerializer(station_problems, many=True).data

    def get_activities(self, obj):
        station_activities = StationInteractiveActivity.objects.filter(station=obj).order_by('order')
        return StationInteractiveActivitySerializer(station_activities, many=True).data
