
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    team_id = serializers.CharField(allow_null=True, required=False)
    points = serializers.IntegerField(default=0)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.EmailField(), required=False)

class ActivitySerializer(serializers.Serializer):
    user_id = serializers.CharField()
    activity_type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()
    date = serializers.DateField()
    points = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team_id = serializers.CharField()
    total_points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    suggested_by = serializers.CharField(max_length=100)
    difficulty = serializers.CharField(max_length=50)
