from typing import Any, Dict
from .models import Memo


class MemoService:
    model_cls = Memo

    def fetch(self, memo_id: int) -> Memo:
        memo = self.model_cls.objects.get(id=memo_id)
        return memo

    def fetch_all(self):
        memos = self.model_cls.objects.all()
        return memos

    def create(self, data: Dict[str, Any]) -> Memo:
        title = data["title"]
        content = data["content"]
        memo = self.model_cls.objects.create(title=title, content=content)
        return memo

    def delete(self, memo_id):
        self.model_cls.objects.get(id=memo_id).delete()
