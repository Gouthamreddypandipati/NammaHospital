from rest_framework import serializers
from .models import UserModel,Doctor,Reports,Courses,Docterpatient,Tests
import re

class UserInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'

    def validate(self, data):
        password=data.get('password')
        newemail=data.get('email')
        print(password)
        if not password:
            raise serializers.ValidationError('no password provided')
        if password:
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)                
            mat = re.search(pat, password)
            if not mat:
                raise serializers.ValidationError("provided password should follow this conditions : 1) length should be at least 6, 2) length should be not be greater than 20 3) Password should have at least one numeral 4) Password should have at least one uppercase letter 5) Password should have at least one lowercase letter 6) Password should have at least one of the symbols $@#")
        return data

class DocterInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

    def validate(self, data):
        password=data.get('password')
        newemail=data.get('email')
        print(password)
        if not password:
            raise serializers.ValidationError('no password provided')
        if password:
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)                
            mat = re.search(pat, password)
            if not mat:
                raise serializers.ValidationError("provided password should follow this conditions : 1) length should be at least 6, 2) length should be not be greater than 20 3) Password should have at least one numeral 4) Password should have at least one uppercase letter 5) Password should have at least one lowercase letter 6) Password should have at least one of the symbols $@#")
        return data


class ReportsInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=Reports
        fields='__all__'


class CoursesInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class DocterpatientInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=Docterpatient
        fields='__all__'


class TestspatientInfoserializer(serializers.ModelSerializer):
    class Meta:
        model=Tests
        fields='__all__'