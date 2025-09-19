from typing import Any, Dict
from .models import Memo


class MemoService:
    model_cls = Memo

    def create(self, data: Dict[str, Any]) -> Memo:
        title = data["title"]
        content = data["content"]
        memo = self.model_cls.objects.create(title=title, content=content)
        return memo

    def fetch(self, memo_id: int) -> Memo:
        memo = self.model_cls.objects.get(id=memo_id)
        return memo

    def fetch_all(self):
        memos = self.model_cls.objects.all()
        return memos

    def patch(self, memo_id: int, update_data: Dict[str, Any]) -> Memo:
        memo = self.model_cls.objects.get(id=memo_id)

        for field, value in update_data.items():
            setattr(memo, field, value)

        memo.save()
        return memo

    def delete(self, memo_id):
        self.model_cls.objects.get(id=memo_id).delete()
