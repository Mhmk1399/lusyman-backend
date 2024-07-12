from rest_framework import generics,status
from .models import HeaderImage,Color, Size, Product, ProductImage,Category,OrderStatus,LaundryService
from .serializers import HeaderImageSerializer,ColorSerializer, SizeSerializer, ProductSerializer, ProductImageSerializer,CategorySerializer,UserSerializer,OrderStatus,LaundryServiceSerializer
from rest_framework.decorators import APIView
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class CheckOrderStatus(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            order_status = OrderStatus.objects.get(code=code)
            if order_status.postal_code:
                return Response({'status': 'shipped', 'postal_code': order_status.postal_code})
            else:
                return Response({'status': 'waiting for post'})
        except OrderStatus.DoesNotExist:
            return Response({'status': 'no code'}, status=status.HTTP_404_NOT_FOUND)

class UpdateOrderStatus(APIView):
    def post(self, request):
        code = request.data.get('code')
        postal_code = request.data.get('postal_code')
        order_status, created = OrderStatus.objects.get_or_create(code=code)
        order_status.postal_code = postal_code
        order_status.save()
        return Response({'status': 'updated', 'code': code, 'postal_code': postal_code})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({'token': token.key})
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
        except ValidationError as e:
            return JsonResponse(e.message_dict(), status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HeaderImageList(generics.ListAPIView):
  queryset = HeaderImage.objects.all()
  serializer_class = HeaderImageSerializer

class HeaderImageDetail(generics.RetrieveAPIView):
  queryset = HeaderImage.objects.all()
  serializer_class = HeaderImageSerializer

class HeaderImageCreate(generics.CreateAPIView):
  queryset = HeaderImage.objects.all()
  serializer_class = HeaderImageSerializer

class HeaderImageUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
  queryset = HeaderImage.objects.all()
  serializer_class = HeaderImageSerializer



class ColorList(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SizeList(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageList(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer




class LaundryServiceList(generics.ListCreateAPIView):
    queryset = LaundryService.objects.all()
    serializer_class = LaundryServiceSerializer

class LaundryServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaundryService.objects.all()
    serializer_class = LaundryServiceSerializer
    