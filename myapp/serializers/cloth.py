from rest_framework import serializers
from myapp.models import #your_model

class clothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ['id', '....']
