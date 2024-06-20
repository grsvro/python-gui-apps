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

list = ["こんにちは", "すごい", "素晴らしい", "いいね", "かに", "えび"]

odai = random.choice(list)

def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    global odai #日本語も受け付ける
    user_input = entry1.get()
    if text1.cget("text") == user_input:
        odai = random.choice(list)
        text1.config(text=odai)
        entry1.delete(0,tk.END) #入力フィールドの消去

def enter_key(event):
    button_action()

# テキスト
text1 = tk.Label(window, text=odai, bg=fg_color, fg=bg_color)
text1.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry1.bind('<Return>', enter_key)  # エンターキーをバインド

# ボタンの作成
button1 = tk.Button(window, text="GO", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
