from rest_framework import serializers
from .models import Passport, Person


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ('id', 'scan', 'file', 'document', 'number', 'first_name', 'last_name', 'patronymic', 'nationality',
                  'birthdate', 'personal_number', 'gender', 'issue_date', 'expire_date', 'issuing_authority')

        read_only_fields = ('id',)



class PersonSerializer(serializers.ModelSerializer):
    passport = PassportSerializer(many=True)

    class Meta:
        model = Person
        fields = ('name', 'surname', 'email', 'passport')
        read_only_fields = ('id',)


class PersonListSerializer(serializers.ModelSerializer):
    passport = PassportSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'email', 'passport')
        read_only_fields = ('id',)

    def get_passports(self, obj):
        return Passport.objects.filter(user=obj).all()
