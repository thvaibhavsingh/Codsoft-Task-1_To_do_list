import tkinter as tk
from tkinter import messagebox
import json

FILENAME = "todo_list_gui.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        self.task_list = self.load_tasks()
        
        # Header Label
        self.header = tk.Label(root, text="Welcome to Your To-Do List", font=("Elephant", 16))
        self.header.pack(pady=10)
        
        # Task Entry
        self.task_entry = tk.Entry(root, width=35)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=35, height=10)
        self.task_listbox.pack(pady=10)
        self.refresh_task_listbox()

        # Buttons Frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Complete Task Button
        self.complete_button = tk.Button(self.button_frame, text="Mark as Complete", command=self.complete_task)
        self.complete_button.grid(row=0, column=0, padx=5)

        # Delete Task Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Save Button
        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=0, column=2, padx=5)
    
    # Add a task to the list
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task before adding.")

    # Refresh the task listbox
    def refresh_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.task_list):
            display_task = task["task"]
            if task["completed"]:
                display_task += " (Completed)"
            self.task_listbox.insert(tk.END, f"{idx+1}. {display_task}")
    
    # Delete a task
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.task_list[selected_task_index]
            self.refresh_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Mark a task as complete
    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_list[selected_task_index]["completed"] = True
            self.refresh_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    # Load tasks from file
    def load_tasks(self):
        try:
            with open(FILENAME, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Save tasks to file
    def save_tasks(self):
        with open(FILENAME, 'w') as file:
            json.dump(self.task_list, file)
        messagebox.showinfo("Tasks Saved", "Your tasks have been saved!")

# Create and run the GUI app
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
