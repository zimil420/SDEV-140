

"""
Event Scheduler GUI Application

This Python application provides a simple GUI for scheduling and managing events. 
Users can add, view, and delete events, with data persistence using a JSON file. 
The interface is built using Tkinter, and Pillow is used for image handling.

Features:
- Add events with name, date, and time.
- View a list of scheduled events.
- Delete selected events.
- Basic input validation and error handling.

Author: Cash Kiefer
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # For handling images
import json  # For data persistence
import re

# File to store event data
EVENTS_FILE = "events.json"

# Function to load events from JSON file
def load_events():
    try:
        with open(EVENTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save events to JSON file
def save_events(events):
    try:
        with open(EVENTS_FILE, "w") as file:
            json.dump(events, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save events: {e}")

# Function to validate date format
def is_valid_date(date_str):
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", date_str))

# Function to validate time format
def is_valid_time(time_str):
    return bool(re.match(r"^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$", time_str))

# Main Application Class
class EventSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Scheduler")
        self.root.geometry("500x400")
        
        # Load images
        try:
            self.banner_img = Image.open("banner.jpg")
            self.banner_img = self.banner_img.resize((500, 150))
            self.banner_photo = ImageTk.PhotoImage(self.banner_img)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
        
        # Main Menu
        self.main_menu()
    
    def main_menu(self):
        #Displays the main menu window.
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Image Label
        lbl_img = tk.Label(self.root, image=self.banner_photo, text="Event Scheduler Banner", compound="top")
        lbl_img.pack()
        
        # Title Label
        lbl_title = tk.Label(self.root, text="Event Scheduler", font=("Arial", 16, "bold"))
        lbl_title.pack(pady=10)
        
        # Buttons
        btn_add_event = tk.Button(self.root, text="Add Event", command=self.add_event_window)
        btn_add_event.pack(pady=5)
        
        btn_view_events = tk.Button(self.root, text="View Events", command=self.view_events_window)
        btn_view_events.pack(pady=5)
        
        btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        btn_exit.pack(pady=5)
    
    def add_event_window(self):
        #Opens the event creation window.
        new_window = tk.Toplevel(self.root)
        new_window.title("Add Event")
        new_window.geometry("400x300")
        
        tk.Label(new_window, text="Event Name:").pack()
        event_name_entry = tk.Entry(new_window)
        event_name_entry.pack()
        
        tk.Label(new_window, text="Date (YYYY-MM-DD):").pack()
        event_date_entry = tk.Entry(new_window)
        event_date_entry.pack()
        
        tk.Label(new_window, text="Time (HH:MM AM/PM):").pack()
        event_time_entry = tk.Entry(new_window)
        event_time_entry.pack()
        
        def save_event():
            #Validates input and saves the event.
            name = event_name_entry.get().strip()
            date = event_date_entry.get().strip()
            time = event_time_entry.get().strip()
            
            # Checks if all fields are filled
            if not name or not date or not time:
                messagebox.showerror("Error", "All fields must be filled!")
                return
            
            #Checks if the date is valid
            if not is_valid_date(date):
                messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")
                return
            
            #Checks if the time is valid
            if not is_valid_time(time):
                messagebox.showerror("Error", "Invalid time format! Use HH:MM AM/PM.")
                return
            
            events = load_events()
            events.append({"name": name, "date": date, "time": time})
            save_events(events)
            messagebox.showinfo("Success", "Event saved successfully!")
            new_window.destroy()
        
        btn_save = tk.Button(new_window, text="Save Event", command=save_event)
        btn_save.pack(pady=10)
    
    def view_events_window(self):
        #Opens the event list window with management options.
        new_window = tk.Toplevel(self.root)
        new_window.title("Manage Events")
        new_window.geometry("400x300")
        
        events = load_events()
        if not events:
            tk.Label(new_window, text="No events found.").pack()
            return
        
        event_list = tk.Listbox(new_window)
        event_list.pack(expand=True, fill="both", padx=10, pady=10)
        
        for event in events:
            event_list.insert(tk.END, f"{event['date']} - {event['name']} at {event['time']}")
        
        def delete_selected_event():
            try:
                selected_index = event_list.curselection()[0]
                events.pop(selected_index)
                save_events(events)
                new_window.destroy()
                self.view_events_window()
            except IndexError:
                messagebox.showerror("Error", "Please select an event to delete.")
        
        btn_delete = tk.Button(new_window, text="Delete Event", command=delete_selected_event)
        btn_delete.pack(pady=5)
        
        btn_close = tk.Button(new_window, text="Close", command=new_window.destroy)
        btn_close.pack(pady=5)

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = EventSchedulerApp(root)
    root.mainloop()
