from rest_framework import serializers
from shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "title", "code", "price", "status", "image"]

    def get_image(self, obj):
        img_data = {}
        img_name = obj.image.name
        ext_dot_position = img_name.rfind(".")
        img_data["path"] = "/media/" + img_name[:ext_dot_position]
        img_data["formats"] = [img_name[(ext_dot_position+1):], "webp"]
        return img_data
