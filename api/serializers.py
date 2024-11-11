from rest_framework import serializers

from api.models import Expense,Income

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["username","email","password"]

        read_only_fields=["id"]

    def create(self,validated_data):
        
        return User.objects.create_user(**validated_data)


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:

        model=Expense

        fields="__all__"

        read_only_fields=["id"]


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:

        model=Income

        fields="__all__"

        read_only_field=["id"]