import pytest
from memos.models import Memo
from memos.use_cases import MemoUseCase


@pytest.mark.django_db
class TestMemoUseCase:
    @pytest.fixture(autouse=True)
    def setup_data(self):
        title = 'テストタイトル'
        content = 'テストコンテンツ'
        self.memo_1 = Memo.objects.create(title=title, content=content)

    def test__fetch__一件取得できること_True(self):
        use_case = MemoUseCase()

        result = use_case.fetch(memo_id=self.memo_1.id)
        assert result
        assert result["title"] == 'テストタイトル'
        assert result["content"] == 'テストコンテンツ'

    def test__fetch__存在しないidのオブジェクトを取得できないこと_False(self):
        use_case = MemoUseCase()

        with pytest.raises(Memo.DoesNotExist):
            use_case.fetch(memo_id=0)
