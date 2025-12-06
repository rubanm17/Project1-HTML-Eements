import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x400")

choices = ["Rock", "Paper", "Scissor"]

# --- Load images ---
rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((120, 120)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((120, 120)))
scissor_img = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((120, 120)))

image_dict = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissor": scissor_img
}

# --- GUI Labels ---
user_label = tk.Label(root, text="Your Choice", font=("Arial", 14))
user_label.pack()

user_img_label = tk.Label(root)
user_img_label.pack()

comp_label = tk.Label(root, text="Computer's Choice", font=("Arial", 14))
comp_label.pack()

comp_img_label = tk.Label(root)
comp_img_label.pack()

result_label = tk.Label(root, text="Result:", font=("Arial", 18, "bold"))
result_label.pack(pady=10)

# --- Game Logic ---
def play(user_choice):
    comp_choice = random.choice(choices)

    # show images
    user_img_label.config(image=image_dict[user_choice])
    comp_img_label.config(image=image_dict[comp_choice])

    # determine winner
    if user_choice == comp_choice:
        result_label.config(text="Result: It's a Tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissor") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissor" and comp_choice == "Paper"):
        result_label.config(text="Result: You Win!")
    else:
        result_label.config(text="Result: Computer Wins!")

# --- Buttons ---
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_rock = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("Rock"))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("Paper"))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissor = tk.Button(button_frame, text="Scissor", width=12, command=lambda: play("Scissor"))
btn_scissor.grid(row=0, column=2, padx=10)

root.mainloop()
