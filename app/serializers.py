from rest_framework import serializers 

from app.models import Restaurant, Meal, Customer, Driver, Order, OrderDetails

class RestaurantSerializer(serializers.ModelSerializer):
	logo = serializers.SerializerMethodField()

	def get_logo(self, restaurant):
		request = self.context.get('request')
		logo_url = restaurant.logo.url
		return request.build_absolute_uri(logo_url)

	class Meta:
		model = Restaurant
		fields = ("id", "name", "phone", "address", "logo")


class MealSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()

	def get_image(self, meal):
		request = self.context.get('request')
		image_url = meal.image.url
		return request.build_absolute_uri(image_url)
		
	class Meta:
		model = Meal
		fields = ("id", "name", "short_description", "image", "price")

# ORDER SERIALIZER

class OrderCustomerSerailizer(serializers.ModelSerializer):
	name = serializers.ReadOnlyField(source="user.get_full_name")

	class Meta:
		model = Customer
		fields = ("id", "name", "avatar", "phone", "address")

class OrderDriverSerailizer(serializers.ModelSerializer):
	name = serializers.ReadOnlyField(source="user.get_full_name")

	class Meta:
		model = Driver
		fields = ("id", "name", "avatar", "phone", "address")

class OrderRestaurantSerailizer(serializers.ModelSerializer):

	class Meta:
		model = Restaurant
		fields = ("id", "name", "phone", "address")

class OrderMealSerailizer(serializers.ModelSerializer):

	class Meta:
		model = Meal
		fields = ("id", "name", "price")


class OrderDetailsSerailizer(serializers.ModelSerializer):
	meal = OrderMealSerailizer()

	class Meta:
		model = OrderDetails
		fields = ("id", "meal", "quantity", "sub_total")


class OrderSerializer(serializers.ModelSerializer):
	customer = OrderCustomerSerailizer()
	driver = OrderDriverSerailizer()
	restaurant = OrderRestaurantSerailizer()
	order_details = OrderDetailsSerailizer(many = True)
	status = serializers.ReadOnlyField(source="get_status_display")


	class Meta:
		model = Order
		fields = ("id", "customer", "restaurant", "driver", "order_details", "total", "status", "address")







