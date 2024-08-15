Hotel Management System
Welcome to the Hotel Management System! 🎉 This handy Python app helps you manage your hotel’s room reservations with ease. Here’s a quick overview of what you can do with it:

What You Can Do
1. View Rooms
Open a window to see a table with all room details, including room ID, current status, guest name, and room service status.
If there are no rooms or data yet, you’ll just see the table headers—no empty rows cluttering your view.
2. Check In a Guest
Easily check in a guest by providing the room ID and their name. The app will update the room’s status to ‘Occupied’ and show the guest’s name.
3. Check Out a Guest
To check out a guest, simply enter the room ID. The room will be marked as ‘Vacant’ and the guest’s name will be set to ‘empty’.
4. Add a New Room
Want to add a new room? Just enter a room ID, and the room will be added to the system. Each room ID must be unique.
How to Get Started
Make Sure You Have the Essentials:

Python 3.x installed on your computer.
Tkinter (which comes with Python).
SQLite (also included with Python).
Run the App:

Clone this repository to your computer.
Open a terminal or command prompt and navigate to the project directory.
Run the application with this command:
bash
Copy code
python hotel_management_app.py
How It Works
Database Setup
The app creates a SQLite database called hotel_management.db with a rooms table. This table has columns for room ID, guest name, and room status.
Viewing Rooms
A new window shows a table with room details. If there’s no data, you’ll only see the column headers.
Checking In
Opens a dialog where you enter the room ID and guest name. The app updates the room’s status and guest name accordingly.
Checking Out
Opens a dialog where you enter the room ID. The app updates the room’s status to ‘Vacant’ and sets the guest name to ‘empty’.
Adding a Room
Opens a dialog to enter a new room ID. The room is then added to the database.
The Interface
When you launch the app, you’ll see a main window with buttons for each function:

View Rooms: See all rooms in a new window.
Check In: Opens a dialog to check in a guest.
Check Out: Opens a dialog to check out a guest.
Add Room: Opens a dialog to add a new room.
Acknowledgments
This app is inspired by simple hotel management concepts and the powerful Tkinter library. A big thanks to the Python community for their support and the amazing libraries they provide!

Feel free to tweak or enhance this app as needed to fit your specific needs. If you have any questions or need help, just let us know!
