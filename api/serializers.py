from rest_framework import serializers
from .models import HeaderImage,Color, Size, Product, ProductImage,Category,User,OrderStatus,LaundryService





class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['code', 'postal_code']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'phone', 'address', 'zipcode', 'is_vip']
    extra_kwargs = {
      'password': {'write_only': True},
      'phone': {'required': True}
    }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user



class HeaderImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = HeaderImage
        fields = ['id', 'title', 'image_url', 'video_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request is not None:
            image_url = request.build_absolute_uri(obj.image.url)
            return image_url
        return None

    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video and request is not None:
            video_url = request.build_absolute_uri(obj.video.url)
            return video_url
        return None

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)  # Only serialize the 'image' field

class ProductSerializer(serializers.ModelSerializer):
  image_url = serializers.SerializerMethodField()
  colors = ColorSerializer(many=True, read_only=True)
  sizes = SizeSerializer(many=True, read_only=True)
  images = ProductImageSerializer(many=True, read_only=True)
  category=CategorySerializer(many=True, read_only=True)

  class Meta:
    model = Product
    fields = ['id', 'title', 'description', 'category','price', 'colors', 'sizes', 'image_url', 'images','payment_link']

  def get_image_url(self, obj):
    request = self.context.get('request')
    if obj.images.first() and request is not None:
      # Assuming your first ProductImage object has the main image
      image = obj.images.first().image
      image_url = request.build_absolute_uri(image.url)
      return image_url
    return None
  

class LaundryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryService
        fields = '__all__'
