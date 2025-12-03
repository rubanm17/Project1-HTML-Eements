import tkinter as tk
import string
import random

# ---------------- GUI Window ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

# Title
label1 = tk.Label(root, text="Enter password length:", font=("Arial", 12))
label1.pack(pady=5)

# Entry for length
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack()

# Output Label
result_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
result_label.pack(pady=10)

# Output box
password_entry = tk.Entry(root, font=("Arial", 14), width=28)
password_entry.pack()

# ---------------- GENERATE BUTTON (without def) ----------------
generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12),
    command=lambda: (
        password_entry.delete(0, tk.END),   # Clear old password

        # Combine character sets
        password_entry.insert(
            0,
            "".join(
                random.choice(
                    string.ascii_lowercase +
                    string.ascii_uppercase +
                    string.digits +
                    string.punctuation
                )
                for _ in range(
                    int(length_entry.get()) if length_entry.get().isdigit() else 0
                )
            )
        )
    )
)

generate_button.pack(pady=15)

root.mainloop()