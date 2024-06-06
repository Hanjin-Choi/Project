from rest_framework import serializers
from .models import Finance, Option

class FinanceSerializer(serializers.ModelSerializer):
    class FinanceOptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Option
            fields = ('pk', 'save_trm', 'intr_rate', 'intr_rate2')

    option_set = FinanceOptionSerializer(read_only=True, many=True)

    class Meta:
        model = Finance
        fields='__all__'
        read_only_fields = ('prdt_category',)

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields ='__all__'
        read_only_fields =('finance',)