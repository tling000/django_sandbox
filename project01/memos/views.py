from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .use_cases import MemoUseCase
from .serializers import MemoSerializer


class MemoDetailView(APIView):
    def get(self, request: Request, id: int) -> HttpResponse:
        use_case = MemoUseCase()
        data = use_case.fetch(memo_id=id)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> HttpResponse:
        pass

    def patch(self, request: Request, id: int) -> HttpResponse:
        pass

    def delete(self, request: Request, id: int) -> HttpResponse:
        pass


class MemoListView(APIView):
    def get(self, request: Request) -> HttpResponse:
        use_case = MemoUseCase()
        data = use_case.fetch_all()
        serializer = MemoSerializer(data, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
