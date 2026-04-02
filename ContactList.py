import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# --- Backend Contact Manager Class (remains unchanged) ---
class ContactManager:
    def __init__(self):
        self.contacts = {
            "Alice": "8458451234",
            "Bob": "3498309876",
            "Charlie": "7890123456",
        }

    def add_contact(self, name, phone_num):
        if not name or not phone_num:
            return "Name and phone number cannot be empty.", False
        if not phone_num.isdigit() or len(phone_num) != 10:
            return (
                "Invalid Phone Number!!",
                False,
            )

        self.contacts[name] = phone_num
        return f"Contact '{name}' with number '{phone_num}' stored successfully!", True

    def search_contact(self, name):
        if not name:
            return "Name cannot be empty.", None
        if name in self.contacts:
            return (
                f"The number for '{name}' is: {self.contacts[name]}.",
                self.contacts[name],
            )
        else:
            return f"'{name}' does not exist in your contact list.", None

    def delete_contact(self, name):
        if not name:
            return "Name cannot be empty.", False
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted successfully.", True
        else:
            return f"'{name}' does not exist in your contact list.", False

    def get_all_contacts(self):
        return self.contacts


# --- New Class for the "Show All Contacts" Window ---
class AllContactsWindow(ctk.CTkToplevel):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.title("All Contacts")
        self.geometry("450x400")
        self.resizable(False, False)

        # Make it modal (optional, but good for info windows)
        self.grab_set()  # Blocks interaction with the main window until this is closed
        self.transient(master)  # Keeps this window on top of the main window

        self._create_widgets()
        self._load_contacts()

    def _create_widgets(self):
        ctk.CTkLabel(self, text="Current Contacts", font=("Arial", 18, "bold")).pack(
            pady=10
        )

        # Frame for textbox and scrollbar
        text_frame = ctk.CTkFrame(self)
        text_frame.pack(pady=5, padx=20, fill="both", expand=True)

        self.contact_textbox = ctk.CTkTextbox(
            text_frame, width=400, height=250, wrap="word"
        )
        self.contact_textbox.pack(side="left", fill="both", expand=True)
        self.contact_textbox.configure(state="disabled")  # Make it read-only

        # Add a scrollbar
        self.textbox_scrollbar = ctk.CTkScrollbar(
            text_frame, command=self.contact_textbox.yview
        )
        self.textbox_scrollbar.pack(side="right", fill="y")
        self.contact_textbox.configure(yscrollcommand=self.textbox_scrollbar.set)

        ctk.CTkButton(self, text="Close", command=self.destroy).pack(pady=10)

    def _load_contacts(self):
        self.contact_textbox.configure(state="normal")  # Enable for editing
        self.contact_textbox.delete("1.0", "end")  # Clear current content

        contacts = self.manager.get_all_contacts()
        if not contacts:
            self.contact_textbox.insert("end", "No contacts stored yet.")
        else:
            for name, phone in contacts.items():
                self.contact_textbox.insert("end", f"Name: {name}, Phone: {phone}\n")
        self.contact_textbox.configure(state="disabled")  # Disable again


# --- Main Application Window Class ---
class ContactApp(ctk.CTk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.title("Contact List Manager")
        self.geometry("600x680")  # Adjust height as needed
        self.resizable(False, False)

        self._create_widgets()
        # No need to call _update_contact_display here anymore,
        # as the main window textbox is removed.

    def _create_widgets(self):
        # --- Add Contact Section ---
        add_frame = ctk.CTkFrame(self)
        add_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            add_frame, text="Add New Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(add_frame, text="Name:").pack(pady=(5, 0))
        self.name_entry = ctk.CTkEntry(add_frame, width=250)
        self.name_entry.pack(pady=(0, 5))

        ctk.CTkLabel(add_frame, text="Phone Number:").pack(pady=(5, 0))
        self.phone_entry = ctk.CTkEntry(add_frame, width=250)
        self.phone_entry.pack(pady=(0, 10))

        ctk.CTkButton(
            add_frame, text="Add Contact", command=self._add_contact_gui
        ).pack(pady=5)

        # --- Search Contact Section ---
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            search_frame, text="Search Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(search_frame, text="Name to Search:").pack(pady=(5, 0))
        self.search_entry = ctk.CTkEntry(search_frame, width=250)
        self.search_entry.pack(pady=(0, 5))

        ctk.CTkButton(
            search_frame, text="Search Contact", command=self._search_contact_gui
        ).pack(pady=5)
        self.search_result_label = ctk.CTkLabel(search_frame, text="", wraplength=400)
        self.search_result_label.pack(pady=5)

        # --- Delete Contact Section ---
        delete_frame = ctk.CTkFrame(self)
        delete_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            delete_frame, text="Delete Contact", font=("Arial", 16, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(delete_frame, text="Name to Delete:").pack(pady=(5, 0))
        self.delete_entry = ctk.CTkEntry(delete_frame, width=250)
        self.delete_entry.pack(pady=(0, 10))

        ctk.CTkButton(
            delete_frame, text="Delete Contact", command=self._delete_contact_gui
        ).pack(pady=5)

        # --- New "Show All Contacts" Button ---
        # This button replaces the old "Display Contacts Section" in the main window
        show_all_button = ctk.CTkButton(
            self,
            text="Show All Contacts",
            command=self._show_all_contacts_window,
        )
        show_all_button.pack(pady=20)

    def _add_contact_gui(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        message, success = self.manager.add_contact(name, phone)
        if success:
            tkmb.showinfo("Success", message)
            self._clear_entries([self.name_entry, self.phone_entry])
            # If the "All Contacts" window is open, it won't auto-update.
            # We could add logic to refresh it if it's visible, but for now,
            # the user will just close and reopen it.
        else:
            tkmb.showerror("Error", message)

    def _search_contact_gui(self):
        name = self.search_entry.get().strip()
        message, phone = self.manager.search_contact(name)
        self.search_result_label.configure(text=message)
        if phone:
            self.search_result_label.configure(text_color="green")
        else:
            self.search_result_label.configure(text_color="red")
        self._clear_entries([self.search_entry])

    def _delete_contact_gui(self):
        name = self.delete_entry.get().strip()
        message, success = self.manager.delete_contact(name)
        if success:
            tkmb.showinfo("Success", message)
            self._clear_entries([self.delete_entry])
            # Similar to add, the new window won't auto-update.
        else:
            tkmb.showerror("Error", message)

    def _show_all_contacts_window(self):
        # Create and display the new window
        AllContactsWindow(self, self.manager)

    def _clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, ctk.END)


# --- Main execution ---
if __name__ == "__main__":
    contact_manager = ContactManager()
    app = ContactApp(contact_manager)
    app.mainloop()
# This code creates a contact management application using customtkinter.
# It allows users to add, search, delete contacts, and view all contacts in a separate window.
# The application is designed to be user-friendly with clear error handling and feedback.
