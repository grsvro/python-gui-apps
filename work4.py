import tkinter as tk
import random
# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

list = []
def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    list.append(user_input)
    label1.config(text="\n".join(list))  # 画面に出力

def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    label2.config(text=random.choice(list))  # 画面に出力

text1 = tk.Label(window, text="名前はまだ無い", bg=fg_color, fg=bg_color)
text1.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ボタンの作成2
button2 = tk.Button(window, text="ランダム選択", command=button_action2)
button2.pack(pady=10)

# 出力ラベルの作成2
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
