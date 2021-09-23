class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model   = User
        fields  = ['id', 'first_name', 'last_name', 'email', 'mobile_number', 'is_active', 'is_staff', 'is_superuser']


    def validate_mobile_number(self, value):
        if mobile_number_pattern.match(value):
            return value
        else:
            raise ValidationError('Mobile number pattern is not correct.')

class LoginSerializer(serializer.Serializer):
    email = serializer.ChaerField()
    password = serializer.CharField()
    def validate(self, data):

        if email and password:
            user = authenticate(email= email, password= password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise exceptions.ValidationError("User is deactivated.")
            else:
                raise exceptions.ValidationError("unable to login")
        else:
            raise exceptions.ValidationError("Must provide email and password both.")
        return data