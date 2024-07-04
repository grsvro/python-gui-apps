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


#リセット
def button_action0():
    global XO
    XO = 0
    text1.config(text="")
    for row in buttons:
        for button in row:
            button.config(text="",state=tk.NORMAL)


#ボタン
XO = 0
def button_action(i,j):
    global XO
    if XO == 0:
        buttons[i][j].config(text="O", state=tk.DISABLED)
        XO = 1
        if not win("O"):
            cpt()
    else:
        buttons[i][j].config(text="X", state=tk.DISABLED)
        XO = 0
    
    if win("O"):
        text1.config(text="Oの勝利！")
    elif win("X"):
        text1.config(text="Xの勝利！")

#勝利条件
def win(player):
    for row in buttons:
        if (row[0].cget("text") == player and
            row[1].cget("text") == player and
            row[2].cget("text") == player):
            return True
    for col in range(3):
        if (buttons[0][col].cget("text")== player and
            buttons[1][col].cget("text")== player and
            buttons[2][col].cget("text") == player):
            return True
    if (buttons[2][0].cget("text") == player and
        buttons[1][1].cget("text") == player and
        buttons[0][2].cget("text") == player):
        return True
    if (buttons[0][0].cget("text") == player and
        buttons[1][1].cget("text") == player and
        buttons[2][2].cget("text") == player):
        return True
    return False

#コンピューター
def cpt():
        #勝ちに行く
        for i in range(3):
            for j in range(3):
                if buttons[i][j].cget("text") == "":
                    buttons[i][j].config(text="X")
                    if win("X"):
                        button_action(i,j)
                        return
                    buttons[i][j].config(text="")
        #妨害
        for i in range(3):
            for j in range(3):
                if buttons[i][j].cget("text") == "":
                    buttons[i][j].config(text="O")
                    if win("O"):
                        buttons[i][j].config(text="X")
                        button_action(i,j)
                        return
                    buttons[i][j].config(text="")
        #ランダム
        cpt_list = [(i,j)for i in range(3) for j in range(3) if buttons[i][j].cget("text") == ""]
        i,j = random.choice(cpt_list)
        button_action(i,j)


# テキスト
text1 = tk.Label(window, text="", bg=bg_color, fg=fg_color, font=("Helvetiva",25))
text1.pack(pady=10)

# テキスト
text2 = tk.Label(window, text="あなたはOです", bg=bg_color, fg=fg_color, font=("Helvetiva",25))
text2.pack(pady=10)

# リセットボタンの作成
button0 = tk.Button(window, text="リセット", command=button_action0, font=("Helvetiva",25))
button0.pack(pady=10)

# フレームの作成
frame = tk.Frame(window, padx=0, pady=0, bg=bg_color)
frame.pack(pady=10)


# ボタン
buttons = []
for i in range(3):
    row_button = []
    for j in range(3):
        button = tk.Button(frame, text="",command=lambda row=i, col=j: button_action(row, col), font=("Helvetiva",25))
        button.grid(row=i, column=j)
        row_button.append(button)
    buttons.append(row_button)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
