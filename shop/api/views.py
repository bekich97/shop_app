from shop.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.db.models import Q


@api_view(["GET"])
@permission_classes([AllowAny])
def index(request):
    status = None
    query_string = None
    if request.GET.get("status"):
        status = request.GET.get("status")
    if request.GET.get("qs"):
        query_string = request.GET.get("qs")

    products = Product.objects.all()

    if status:
        products = products.filter(status=status)
    
    if query_string:
        products = products.filter(
            Q(title__icontains=query_string) |
            Q(code__icontains=query_string)
        )
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def detail(request, id):
    product = Product.objects.filter(id=id).first()
    if not product:
        return Response({"detail": "Product not found!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
