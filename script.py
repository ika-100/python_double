# ユーザー入力を整数に変換して2倍する

number_str = input("数字を入力してください: ") # 入力された文字列を格納
try:
    number_int = int(number_str) # 文字列を整数に変換
    result = number_int * 2 # 二倍する
    print(result) # 結果を表示
except ValueError:
    print("無効な入力です。数字を入力してください。") # 数字以外が入力された場合のエラー処理