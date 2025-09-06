from .models import Memo

class MemoService:
    model_cls = Memo

    def fetch(self, memo_id: int) -> Memo:
        memo = self.model_cls.objects.get(id=memo_id)
        return memo

    def fetch_all(self):
        memos = self.model_cls.objects.all()
        return memos
