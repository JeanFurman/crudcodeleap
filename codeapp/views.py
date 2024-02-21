from rest_framework import viewsets, status
from .models import Career
from .serializers import CareerSerializer
from rest_framework.response import Response

class CareerViewSet(viewsets.ViewSet):

    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            career = Career.objects.get(pk=pk)
        except Career.DoesNotExist:
            return self.create_error_response(
                "Career not found.", status.HTTP_404_NOT_FOUND
            )
        serializer = CareerSerializer(career)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            career = Career.objects.get(pk=pk)
            serializer = self.serializer_class(
                career, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        except Career.DoesNotExist:
            return self.create_error_response(
                "Career not found.", status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            career = Career.objects.get(pk=pk)
            career.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Career.DoesNotExist:
            return self.create_error_response(
                "Career not found.", status.HTTP_404_NOT_FOUND
            )
        
    def create_error_response(self, message, status_code):
        return Response({"error": message}, status=status_code)