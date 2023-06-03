from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # picked all the data from Customer model using __all__
        fields = "__all__"
