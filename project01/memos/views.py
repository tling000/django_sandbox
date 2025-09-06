from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .use_cases import MemoUseCase
from .serializers import MemoSerializer


class MemoDetailView(APIView):
    def get(self, request: Request, id: int) -> HttpResponse:
        try:
            use_case = MemoUseCase()
            data = use_case.fetch(memo_id=id)
        except Exception as e:
            return Response({"Error": f"Internal server error: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> HttpResponse:
        pass

    def patch(self, request: Request, id: int) -> HttpResponse:
        pass

    def delete(self, request: Request, id: int) -> HttpResponse:
        try:
            use_case = MemoUseCase()
            use_case.delete(memo_id=id)
        except Exception as e:
            return Response({"Error": f"Internal server error: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)


class MemoListView(APIView):
    def get(self, request: Request) -> HttpResponse:
        try:
            use_case = MemoUseCase()
            data = use_case.fetch_all()
            serializer = MemoSerializer(instance=data, many=True)
        except Exception as e:
            return Response({"Error": f"Internal server error: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
