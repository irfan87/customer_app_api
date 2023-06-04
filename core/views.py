from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer


@api_view(["GET", "POST"])
def customers_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CustomerSerializer(data=request.data)

        # verified if the customer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"customers": serializer.data}, status=status.HTTP_201_CREATED
            )


@api_view(["GET", "PUT", "DELETE"])
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CustomerSerializer(customer)
        return Response({"customer": serializer.data})

    if request.method == "PUT":
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"customer": serializer.data})
        # if update / put is not working
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        customer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
