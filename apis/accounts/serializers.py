from rest_framework import serializers
from apis.accounts.models import User, profile

class UserProfileSerializer(serializers.Serializer):
    dob = serializers.DateField(required=False)
    address = serializers.CharField(max_length=30, required=False)
    display_image = serializers.ImageField(required=False)
     
    

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields =('username', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User(**validated_data)
        user.save()
        profile.objects.create(user=user, **profile_data)
        return user

        