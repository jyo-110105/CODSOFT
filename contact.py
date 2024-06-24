import tkinter as tk
from tkinter import messagebox
import pickle

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        # Initialize list to store contacts
        self.contacts = []
        
        # Load contacts from file if it exists
        self.load_contacts()
        
        # Create GUI elements
        label_name = tk.Label(root, text="Name:")
        label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        label_phone = tk.Label(root, text="Phone:")
        label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(root, width=30)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)
        
        label_email = tk.Label(root, text="Email:")
        label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(root, width=30)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)
        
        label_address = tk.Label(root, text="Address:")
        label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(root, width=30)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons
        button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        button_add.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        button_view.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        button_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        button_search.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        button_update.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        button_delete.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="WE")
        
        # Listbox to display contacts
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.grid(row=0, column=2, rowspan=9, padx=10, pady=10, sticky="NS")
        
        # Bind double-click event to listbox
        self.listbox.bind("<Double-Button-1>", self.on_listbox_select)
        
        # Populate listbox with existing contacts
        self.view_contacts()
    
    def add_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()
        address = self.entry_address.get().strip()
        
        if name and phone:  # Name and phone are required fields
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.save_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    
    def view_contacts(self):
        self.listbox.delete(0, tk.END)  # Clear existing items in the listbox
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact.name}: {contact.phone}")
    
    def search_contact(self):
        search_term = self.entry_name.get().strip()
        if not search_term:
            messagebox.showerror("Error", "Please enter a name to search.")
            return
        
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(f"{contact.name}: {contact.phone}")
        
        if results:
            self.listbox.delete(0, tk.END)
            for result in results:
                self.listbox.insert(tk.END, result)
        else:
            messagebox.showinfo("Not Found", f"No contacts found with name or phone number containing '{search_term}'.")
    
    def update_contact(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a contact to update.")
            return
        
        index = selected_index[0]
        selected_contact = self.contacts[index]
        
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()
        email = self.entry_email.get().strip()
        address = self.entry_address.get().strip()
        
        if name and phone:  # Name and phone are required fields
            selected_contact.name = name
            selected_contact.phone = phone
            selected_contact.email = email
            selected_contact.address = address
            self.save_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully.")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    
    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return
        
        index = selected_index[0]
        del self.contacts[index]
        self.save_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")
        self.view_contacts()
    
    def on_listbox_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_contact = self.contacts[index]
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(tk.END, selected_contact.name)
            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(tk.END, selected_contact.phone)
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(tk.END, selected_contact.email)
            self.entry_address.delete(0, tk.END)
            self.entry_address.insert(tk.END, selected_contact.address)
    
    def save_contacts(self):
        with open("contacts.pickle", "wb") as f:
            pickle.dump(self.contacts, f)
    
    def load_contacts(self):
        try:
            with open("contacts.pickle", "rb") as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = []
    
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

# Main function to start the application
def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
