import tkinter as tk

def start_game():
    # Function to start the game (replace this with your actual game code)
    print("Starting Tic Tac Toe game!")
    # Replace the print statement with your code to start the game

# Create the main window
root = tk.Tk()
root.title("Welcome to Tic Tac Toe")

# Create and place widgets
welcome_label = tk.Label(root, text="Welcome to Tic Tac Toe", font=("Helvetica", 24))
welcome_label.pack(pady=20)

start_button = tk.Button(root, text="Start Game", command=start_game, font=("Helvetica", 16))
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 16))
exit_button.pack(pady=10)

# Run the main event loop
root.mainloop()
