from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(["GET", "POST"])
def drink_list(request):

    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializers(drinks, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, pk):
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return JsonResponse({"message": "The drink does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializers(drink)
        return JsonResponse(serializer.data)

    if request.method == "PUT":
        serializer = DrinkSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        drink.delete()
        return JsonResponse({"message": "Drink was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
