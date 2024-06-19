import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())  # 入力値を取得
    if seireki > 1868 and seireki <1912:
        x = int(seireki)-1912
        label1.config(text=f"明治{x}年")  # 画面に出力
    elif seireki > 1912 and seireki <1926:
        x = int(seireki)-1926
        label1.config(text=f"大正{x}年")  # 画面に出力
    elif seireki > 1926 and seireki <1989:
        x = int(seireki)-1926
        label1.config(text=f"昭和{x}年")  # 画面に出力
    elif seireki > 1989 and seireki <2019:
        x = int(seireki)-1989
        label1.config(text=f"平成{x}年")  # 画面に出力
    elif seireki > 2019 and seireki <2026:
        x = int(seireki)-2019
        label1.config(text=f"令和{x}年")  # 画面に出力
    else:
        label1.config(text=f"?")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="西暦を和暦に変換", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
