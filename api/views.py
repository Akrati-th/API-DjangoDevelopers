from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import DevSerializer
from .models import Developer


@api_view(['GET'])
def appendix(request):
    endpoints = ['/developers', '/developers/<id>', '/developers/<name>']
    return Response(endpoints)


@api_view(['GET'])
def developerList(request):
    dev = Developer.objects.all()
    serializer = DevSerializer(dev, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def developerCreate(request):
    serializer = DevSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class developerDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        dev = Developer.objects.get(id=pk)
        serializer = DevSerializer(dev, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        dev = Developer.objects.get(id=pk)
        serializer = DevSerializer(instance=dev, data=request.data)
        return Response(serializer.data)

    def delete(self, request, pk):
        dev = Developer.objects.get(id=pk)
        dev.delete()
        return Response("Developer was Deleted!")


class developerDetailbyname(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, name):
        dev = Developer.objects.get(name=name)
        serializer = DevSerializer(dev, many=False)
        return Response(serializer.data)

    def put(self, request, name):
        dev = Developer.objects.get(name=name)
        serializer = DevSerializer(instance=dev, data=request.data)
        return Response(serializer.data)

    def delete(self, request, name):
        dev = Developer.objects.get(name=name)
        dev.delete()
        return Response("Developer was Deleted!")





