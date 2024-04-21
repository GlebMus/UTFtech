from django.db.models import Count, Q
from rest_framework.response import Response

from .models import FoodCategory, FoodListSerializer
from rest_framework.views import APIView


class CategoriesAPIView(APIView):
    def get(self, request):
        categories_with_published_foods = FoodCategory.objects.annotate(
            num_published_foods=Count('food', filter=(Q(food__is_publish=True)))
        )

        categories_with_published_foods = categories_with_published_foods.filter(num_published_foods__gt=0)

        print(categories_with_published_foods)

        serializer_data = FoodListSerializer(categories_with_published_foods, many=True)

        return Response(serializer_data.data)

