import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

moves = ["Rock", "Paper", "Scissors"]

player_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 14))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Winner: ", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

# ---------- Buttons ----------
rock_btn = tk.Button(
    root, text="Rock", width=10,
    command=lambda: (
        player_label.config(text="Your Choice: Rock"),
        (lambda comp: [
            computer_label.config(text=f"Computer Choice: {comp}"),
            result_label.config(text="Winner: " + (
                "Tie" if comp == "Rock" else
                "You Win" if comp == "Scissors" else
                "Computer Wins"
            ))
        ])(random.choice(moves))
    )
)
rock_btn.pack()

paper_btn = tk.Button(
    root, text="Paper", width=10,
    command=lambda: (
        player_label.config(text="Your Choice: Paper"),
        (lambda comp: [
            computer_label.config(text=f"Computer Choice: {comp}"),
            result_label.config(text="Winner: " + (
                "Tie" if comp == "Paper" else
                "You Win" if comp == "Rock" else
                "Computer Wins"
            ))
        ])(random.choice(moves))
    )
)
paper_btn.pack()

scissor_btn = tk.Button(
    root, text="Scissors", width=10,
    command=lambda: (
        player_label.config(text="Your Choice: Scissors"),
        (lambda comp: [
            computer_label.config(text=f"Computer Choice: {comp}"),
            result_label.config(text="Winner: " + (
                "Tie" if comp == "Scissors" else
                "You Win" if comp == "Paper" else
                "Computer Wins"
            ))
        ])(random.choice(moves))
    )
)
scissor_btn.pack()

# ---------- Reset Button ----------
reset_btn = tk.Button(
    root, text="Reset Game", width=12,
    command=lambda: (
        player_label.config(text="Your Choice: "),
        computer_label.config(text="Computer Choice: "),
        result_label.config(text="Winner: ")
    )
)
reset_btn.pack(pady=15)

root.mainloop()