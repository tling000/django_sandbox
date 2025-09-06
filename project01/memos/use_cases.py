from typing import Any, Dict, List
from .services import MemoService
from .serializers import MemoSerializer


class MemoUseCase:
    service = MemoService()
    serializer = MemoSerializer

    def fetch(self, memo_id: int) -> Dict[str, Any]:
        memo = self.service.fetch(memo_id)
        result = self.serializer(memo).data
        return result

    def fetch_all(self) -> List[Dict[str, Any]]:
        memos = self.service.fetch_all()
        result = self.serializer(memos, many=True).data
        return result
