# minimini_test
## 注意事項
### このテストはlinux環境での実行を前提としています。debian環境で正常に動作することを確認しています。
### このテストは複数のコマンドを順次実行するテストは用意されていません。もし、[;],[||],[&&]による実行制御
### を実装している場合、それらで適切に区切ることで複数コマンドを実行することができます。
## このテストの使い方
### minishell実行ファイルをディレクトリへ入れる。
### minishell内のプロンプトをコピーし、main.pyファイル内のminishell_prompt定数に設定。
### python3 main.pyを実行する。
## テスト方法
### 任意の実行したいコマンドを記述したファイルを作成。
### execコマンドを入力後、実行したいコマンドを入力する。
### exec_allコマンドを実行し、プロンプトに実行したいコマンドを記述したファイルを指定する。
### anlysisコマンドでexit_status,stdout,stderrの合計エラー数を表示する。
### showコマンドで現在実行したコマンドの結果を全て表示する。
### searchコマンドでエラーステータスのdiff、標準出力のdiff、標準エラー出力のdiffを基準に検索できる。
### clearコマンドでウィンドウをクリア。
### 実行結果がlogディレクトリ内に日付をフォーマットしたログ・ファイル名で出力される。
