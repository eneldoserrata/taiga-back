from rest_framework import serializers

from greenmine.scrum.models import *
from picklefield.fields import dbsafe_encode, dbsafe_decode

import json

class PickleField(serializers.WritableField):
    """
    Pickle objects serializer.
    """
    def to_native(self, obj):
        return obj

    def from_native(self, data):
        return json.loads(data)


class ProjectSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = Project
        fields = ()


class MilestoneSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = Milestone
        fields = ()


class UserStorySerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = UserStory
        fields = ()


class ChangeSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = Change
        fields = ()


class ChangeAttachmentSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = ChangeAttachment
        fields = ()


class TaskSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = Task
        fields = ()


class IssueSerializer(serializers.ModelSerializer):
    tags = PickleField()

    class Meta:
        model = Issue
        fields = ()


class SeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Severity
        fields = ()


class IssueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueStatus
        fields = ()


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ()


class UserStoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStoryStatus
        fields = ()


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ()


class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = ()


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ()