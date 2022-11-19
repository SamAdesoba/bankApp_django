from rest_framework import serializers

from bank_app.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    # full_name = serializers.ReadOnlyField(source='first_name')
    #
    # def get_full_name(self, obj):
    #     return f'{obj.first_name} {obj.last_name} {obj.other_name}'

    class Meta:
        model = Customer
        fields = '__all__'
