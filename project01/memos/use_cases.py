from typing import Any, Dict, List
from .services import MemoService
from .serializers import MemoSerializer


class MemoUseCase:
    service = MemoService()
    serializer = MemoSerializer

    def fetch(self, memo_id: int) -> Dict[str, Any]:
        memo = self.service.fetch(memo_id)
        result = self.serializer(instance=memo).data
        return result

    def fetch_all(self) -> List[Dict[str, Any]]:
        memos = self.service.fetch_all()
        result = self.serializer(instance=memos, many=True).data
        return result

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        memo = self.service.create(data)
        result = self.serializer(instance=memo).data
        return result

    def delete(self, memo_id: int):
        self.service.delete(memo_id)
