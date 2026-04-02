import customtkinter as ctk
import tkinter.messagebox as tkmb  # For improved error messages


class TallyCounterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Modern Tally Counter")
        self.geometry("400x550")  # Slightly taller for better spacing
        self.resizable(False, False)  # Fixed size for consistent look

        # --- Appearance Modes & Themes (Modern Look) ---
        ctk.set_appearance_mode("Dark")  # Start with Dark mode for a sleek look
        ctk.set_default_color_theme("green")  # A modern green accent

        # --- Counter Variable ---
        # Using a list allows modifying it inside functions without `nonlocal` or `self` if passed
        # For a class-based app, an instance variable is more direct and preferred.
        self.count = 0

        self._create_widgets()

    def _create_widgets(self):
        # --- Main Counter Display ---
        # Use a frame to group the count label and give it some padding
        display_frame = ctk.CTkFrame(
            self, fg_color="transparent"
        )  # Transparent background
        display_frame.pack(pady=(50, 20), padx=20, fill="x")

        self.count_label = ctk.CTkLabel(
            display_frame,
            text=str(self.count),
            font=("Arial", 90, "bold"),  # Larger, bolder font
            text_color="#2ECC71",
        )  # A vibrant green color
        self.count_label.pack(expand=True)  # Center the label

        # --- Control Buttons Frame ---
        # This frame will hold the increment and decrement buttons side-by-side
        button_controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_controls_frame.pack(pady=20, padx=20)

        # Increment Button
        self.plus_button = ctk.CTkButton(
            button_controls_frame,
            text="+",
            corner_radius=15,  # Slightly rounded corners
            font=("Arial", 60, "bold"),
            command=self._add_count,
            height=120,  # Larger hit area
            width=120,
            fg_color="#3498DB",  # A calming blue
            text_color="white",
            hover_color="#2980B9",
        )  # Darker blue on hover
        self.plus_button.pack(side="left", padx=(0, 15))  # Padding to the right

        # Decrement Button
        self.minus_button = ctk.CTkButton(
            button_controls_frame,
            text="-",
            corner_radius=15,
            font=("Arial", 60, "bold"),
            command=self._minus_count,
            height=120,
            width=120,
            fg_color="#E74C3C",  # A strong red
            text_color="white",
            hover_color="#C0392B",
        )  # Darker red on hover
        self.minus_button.pack(side="left", padx=(15, 0))  # Padding to the left

        # --- Reset Button ---
        self.reset_button = ctk.CTkButton(
            self,
            text="Reset",
            corner_radius=10,  # Moderate rounded corners
            font=("Arial", 20, "bold"),
            command=self._reset_count,
            height=50,
            width=150,
            fg_color="#F39C12",  # An energetic orange
            text_color="white",
            hover_color="#E67E22",
        )  # Darker orange on hover
        self.reset_button.pack(pady=(30, 20))  # More vertical padding

    # --- Button Command Functions ---
    def _add_count(self):
        self.count += 1
        self.count_label.configure(text=str(self.count))

    def _minus_count(self):
        if self.count > 0:
            self.count -= 1
            self.count_label.configure(text=str(self.count))
        else:
            # Use CustomTkinter's messagebox for a more integrated look
            tkmb.showwarning("Minimum Reached", "The count cannot go below zero!")
            # The old root.mainloop() would create a new, blocking window each time
            # Using tkmb is much better for simple alerts.

    def _reset_count(self):
        self.count = 0
        self.count_label.configure(text=str(self.count))


# --- Run the application ---
if __name__ == "__main__":
    app = TallyCounterApp()
    app.mainloop()
