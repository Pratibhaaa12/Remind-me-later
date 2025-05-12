from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer

class ReminderCreateView(APIView):
    def post(self, request):
        try:
            serializer = ReminderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response(data, status=status.HTTP_201_CREATED)
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# Create your views here.
