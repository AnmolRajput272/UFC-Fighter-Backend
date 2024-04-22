from rest_framework import serializers
from .models import ufc_fighter, weight_division
from rest_framework.response import Response
from rest_framework import status

class ufc_fighter_serializer(serializers.ModelSerializer):
    class Meta:
        model = ufc_fighter
        fields = '__all__'
        depth = 1

    def validate(self, data):
        if data['rank'] > 15:
            raise serializers.ValidationError("Rank account be greater than 15.")
        return data
    
class user_serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class register_ufc_fighter_serializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    rank = serializers.IntegerField(allow_null=True)
    is_champ = serializers.BooleanField()
    next_opponent = serializers.CharField(allow_null=True, required=False)
    weight_division_id = serializers.IntegerField(allow_null=True, required=False)

    def validate(self, data):
        if data['weight_division_id']:
            data['weight_division'] = weight_division.objects.get(id=data['weight_division_id'])
        del data['weight_division_id']
        return data

    def create(self, validated_data):
        ufc_fighter_obj = ufc_fighter.objects.create(**validated_data)
        return Response(ufc_fighter_serializer(ufc_fighter_obj).data)
    
class weight_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    weight = serializers.IntegerField()

         