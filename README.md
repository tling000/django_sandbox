# django_sandbox
Djangoによる開発を色々試行するためのリポジトリ。

# pre-push設定
Gitのデフォルトでは、フックは`.git/hooks`に定義する仕様になっている。
しかし、このリポジトリではフックをGit管理したいため、`.githooks`ディレクトリに定義している。

`.githooks`をフックの定義場所としてGitに認識させるため、下記コマンドを実行する（本リポジトリでのpush時のみ有効）。
```
git config --local core.hooksPath .githooks
```
