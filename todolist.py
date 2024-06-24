import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
    task = simpledialog.askstring("Add Task", "Enter a task:")
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_listbox()

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        new_task = simpledialog.askstring("Update Task", "Enter a new task:", initialvalue=tasks[task_index]["task"])
        if new_task:
            tasks[task_index]["task"] = new_task
            update_task_listbox()
    else:
        messagebox.showwarning("Update Task", "Please select a task to update.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_listbox()
    else:
        messagebox.showwarning("Delete Task", "Please select a task to delete.")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = True
        update_task_listbox()
    else:
        messagebox.showwarning("Complete Task", "Please select a task to mark as completed.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        task_listbox.insert(tk.END, f"{task['task']} - {status}")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

task_listbox = tk.Listbox(frame, width=50, height=10, bg="#e0e0e0", fg="#333333", selectbackground="#333333", selectforeground="#ffffff")
task_listbox.pack(side=tk.LEFT, padx=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=10)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, width=12, bg="#2196F3", fg="white")
update_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12, bg="#F44336", fg="white")
delete_button.grid(row=0, column=2, padx=10)

complete_button = tk.Button(button_frame, text="Complete Task", command=complete_task, width=12, bg="#FFC107", fg="white")
complete_button.grid(row=0, column=3, padx=10)

root.mainloop()

