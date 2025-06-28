from rest_framework import serializers
from .models import StaffBase, Manager, Intern

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        exclude = ['has_company_card']

class ManagerSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = '__all__'

    def get_role(self, obj):
        return obj.get_role()

class InternSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Intern
        fields = '__all__'

    def get_role(self, obj):
        return obj.get_role()
