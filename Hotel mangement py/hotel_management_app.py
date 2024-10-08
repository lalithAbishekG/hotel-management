
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Initialize the main application window
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("400x400")  # Main window size

# Define a color palette for the monochromatic theme
bg_color = "#1B263B"  # Dark Blue Background
fg_color = "#E0E1DD"  # Light Text
button_bg = "#2E4057"  # Slightly lighter dark blue for buttons
button_hover_bg = "#3B5368"  # Even lighter blue for hover

# Set up the style for ttk widgets
style = ttk.Style()
style.theme_use("clam")  # Using clam theme for better customization

# Configure custom styles
style.configure("TButton",
                background=button_bg,
                foreground=fg_color,
                font=("Helvetica", 12, "bold"),
                borderwidth=0,
                padding=10)
style.map("TButton",
          background=[("active", button_hover_bg)])

style.configure("TLabel",
                background=bg_color,
                foreground=fg_color,
                font=("Helvetica", 14))

style.configure("Treeview.Heading",
                background=button_bg,
                foreground=fg_color,
                font=("Helvetica", 12, "bold"))

style.configure("Treeview",
                background="#2C3E50",
                foreground=fg_color,
                font=("Helvetica", 12),
                rowheight=30,
                fieldbackground="#2C3E50")

# Set the background color for the root window
root.configure(bg=bg_color)

# Function to create the database and rooms table
def create_database():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INTEGER PRIMARY KEY,
        guest_name TEXT DEFAULT 'empty',
        status TEXT DEFAULT 'Vacant'
    )
    ''')
    conn.commit()
    conn.close()

# Function to view rooms in a new window
def view_rooms():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    rows = cursor.fetchall()
    conn.close()

    view_window = tk.Toplevel(root)
    view_window.title("View Rooms")
    view_window.configure(bg=bg_color)
    
    columns = ("sno", "room_id", "status", "guest_name")
    tree = ttk.Treeview(view_window, columns=columns, show='headings', height=10)
    tree.heading("sno", text="S.No")
    tree.heading("room_id", text="Room ID")
    tree.heading("status", text="Status")
    tree.heading("guest_name", text="Guest Name")

    tree.column("sno", width=50, anchor="center")
    tree.column("room_id", width=100, anchor="center")
    tree.column("status", width=100, anchor="center")
    tree.column("guest_name", width=150, anchor="center")

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for i, row in enumerate(rows):
        tree.insert("", "end", values=(i+1, row[0], row[2], row[1]))

    if not rows:
        tree.insert("", "end", values=("No data available", "", "", ""))

# Function to check in a guest
def check_in():
    def submit_check_in():
        room_id = room_id_entry.get()
        guest_name = guest_name_entry.get()
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE rooms SET guest_name=?, status='Occupied' WHERE room_id=?", (guest_name, room_id))
        if cursor.rowcount == 0:
            messagebox.showerror("Error", f"No room found with ID {room_id}.")
        else:
            messagebox.showinfo("Success", f"Checked in {guest_name} to Room {room_id}.")
        conn.commit()
        conn.close()
        checkin_window.destroy()

    checkin_window = tk.Toplevel(root)
    checkin_window.title("Check In")
    checkin_window.configure(bg=bg_color)
    
    tk.Label(checkin_window, text="Room ID:", bg=bg_color, fg=fg_color, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
    room_id_entry = tk.Entry(checkin_window, font=("Helvetica", 12))
    room_id_entry.grid(row=0, column=1, pady=5)
    
    tk.Label(checkin_window, text="Guest Name:", bg=bg_color, fg=fg_color, font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
    guest_name_entry = tk.Entry(checkin_window, font=("Helvetica", 12))
    guest_name_entry.grid(row=1, column=1, pady=5)
    
    submit_button = ttk.Button(checkin_window, text="Check In", command=submit_check_in)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Function to check out a guest
def check_out():
    def submit_check_out():
        room_id = room_id_entry.get()
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE rooms SET guest_name='empty', status='Vacant' WHERE room_id=?", (room_id,))
        if cursor.rowcount == 0:
            messagebox.showerror("Error", f"No room found with ID {room_id}.")
        else:
            messagebox.showinfo("Success", f"Checked out Room {room_id}.")
        conn.commit()
        conn.close()
        checkout_window.destroy()

    checkout_window = tk.Toplevel(root)
    checkout_window.title("Check Out")
    checkout_window.configure(bg=bg_color)
    
    tk.Label(checkout_window, text="Room ID:", bg=bg_color, fg=fg_color, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
    room_id_entry = tk.Entry(checkout_window, font=("Helvetica", 12))
    room_id_entry.grid(row=0, column=1, pady=5)
    
    submit_button = ttk.Button(checkout_window, text="Check Out", command=submit_check_out)
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Function to add a new room
def add_room():
    def submit_add_room():
        room_id = room_id_entry.get()
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rooms (room_id) VALUES (?)", (room_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Room {room_id} added successfully!")
        addroom_window.destroy()

    addroom_window = tk.Toplevel(root)
    addroom_window.title("Add Room")
    addroom_window.configure(bg=bg_color)
    
    tk.Label(addroom_window, text="Room ID:", bg=bg_color, fg=fg_color, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
    room_id_entry = tk.Entry(addroom_window, font=("Helvetica", 12))
    room_id_entry.grid(row=0, column=1, pady=5)
    
    submit_button = ttk.Button(addroom_window, text="Add Room", command=submit_add_room)
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Main buttons in the application window
view_button = ttk.Button(root, text="View Rooms", command=view_rooms)
view_button.pack(pady=10)

checkin_button = ttk.Button(root, text="Check In", command=check_in)
checkin_button.pack(pady=10)

checkout_button = ttk.Button(root, text="Check Out", command=check_out)
checkout_button.pack(pady=10)

addroom_button = ttk.Button(root, text="Add Room", command=add_room)
addroom_button.pack(pady=10)

# Run the database setup function
create_database()

# Start the main loop
root.mainloop()


