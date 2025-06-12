from rest_framework import serializers
from .models import ProductsModel, AdministrationModel, CategoryModel

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrationModel
        fields = '__all__'


