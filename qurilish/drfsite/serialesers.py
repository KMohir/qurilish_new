from rest_framework import serializers

from shop.models import Product, Category, ads, City


class adsserialers(serializers.ModelSerializer):
    class Meta:
        model= ads
        fields=('__all__')

class productserialersdetail(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    cityslug = serializers.CharField(source='city.slug')
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Product
        fields="__all__"
class productserialers(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')
    class Meta:
        model=Product
        fields="__all__"

class categoryserialers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class cityserialers(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ("id",)
# class productserialers(serializers.ModelSerializer):
#     class Meta:
#         model= Product
#         fields=('name',)
#

# class productserialers(serializers.ModelSerializer):
#     class Meta:
#         model=Product
        # exclude=("id",)
    # category_id=serializers.IntegerField()
    # city_id=serializers.IntegerField()
    # name=serializers.CharField()
    # slug=serializers.SlugField()
    # image=serializers.ImageField(read_only=True)
    # company_name=serializers.CharField()
    # description=serializers.CharField()
    # price=serializers.IntegerField()
    # available=serializers.BooleanField(default=True)
    # created=serializers.DateTimeField(read_only=True)
    # updated=serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     pro=Product.objects.create(**validated_data)
    #     return pro
    # def update(self, instance, validated_data):
    #     instance.category_id=validated_data.get("category_id",instance.category_id)
    #     instance.city_id=validated_data.get("city_id",instance.category_id)
    #     instance.slug=validated_data.get("slug",instance.slug)
    #     instance.price=validated_data.get("price",instance.price)
    #     instance.description=validated_data.get("description",instance.description)
    #
    #     instance.save()
    #     return instance
