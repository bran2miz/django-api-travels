from rest_framework import serializers
from .models import Travel

class TravelSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('owner', 'name', 'description', 'created_at', 'updated_at')
    model = Travel