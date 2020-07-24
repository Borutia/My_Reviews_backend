from rest_framework import serializers

class User_serializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=128
    )
    email = serializers.EmailField(
        required=True,
        # validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        min_length=6
    )
    created = serializers.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    updated = serializers.DateTimeField(
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id',)
