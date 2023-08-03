from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import status
import json

from .serializers import ViewDeveloperSerializer, CreateDeveloperSerializer
from .models import Developer


@api_view(['GET'])
def appendix(request):
    endpoints = ['/developers', '/developers/<id>', '/developers/<name>']
    return Response(endpoints)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_developer_list(request):
    try:
        dev = Developer.objects.all()
        serializer = ViewDeveloperSerializer(dev, many=True)
        return Response(serializer.data)
    except Exception as e:
        return HttpResponse(json.dumps({"error": "Something went Wrong."}), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_developer(request):
    try:
        serializer = CreateDeveloperSerializer(data=request.data)
        if not serializer.is_valid():
            return HttpResponse(json.dumps({"error": "Something went Wrong."}), status=status.HTTP_400_BAD_REQUEST)
        new_serializer = serializer.create(serializer.validated_data)
        new_serializer = ViewDeveloperSerializer(new_serializer).data
        return HttpResponse(json.dumps({"developer": new_serializer}))
    except Exception as e:
        return HttpResponse(json.dumps({"error": "Something went Wrong."}), status=status.HTTP_400_BAD_REQUEST)


class developer_info(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            dev = Developer.objects.get(id=pk)
            serializer = ViewDeveloperSerializer(dev, many=False)
            return Response(serializer.data)
        except Exception as e:
            return HttpResponse(json.dumps({"error": "Something went Wrong."}), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            dev = Developer.objects.get(id=pk)
            dev.delete()
            return Response("Developer was Deleted!")
        except Exception as e:
            return HttpResponse(json.dumps({"error": "Something went Wrong."}), status=status.HTTP_400_BAD_REQUEST)
