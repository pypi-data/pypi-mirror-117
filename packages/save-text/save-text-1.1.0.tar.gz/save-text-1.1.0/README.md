# テキストを保存することのできるコマンド
## 使い方
### インストール
```sh
$ pip install save-text
```
### コマンド一覧
#### 基本的なコマンドの構文
```
$ save-text <command> [args...]
```
#### delete
テキストはidで管理されるため、idを渡すとidのテキストが削除されます。
```
$ save-text delete id
```
#### store
exampleの部分が保存されます。
```
$ save-text store example
```
#### get
テキストはidで管理されるため、idを渡すとidのテキストが表示されます。
```
$ save-text get id
```
#### list
idとテキストが一覧で表示されます。
```
$ save-text list
```
#### --help
コマンドの説明が表示されます。
```
$ save-text --help
```