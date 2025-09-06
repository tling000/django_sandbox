from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MemoSerializer
from .models import Memo


class MemoDetailView(APIView):
    def get(self, request: Request, id: int) -> HttpResponse:
        data = Memo.objects.get(id=id)
        serializer = MemoSerializer(data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MemoListView(APIView):
    def get(self, request: Request) -> HttpResponse:
        data = Memo.objects.all()
        serializer = MemoSerializer(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
