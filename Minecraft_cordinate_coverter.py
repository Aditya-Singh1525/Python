import customtkinter as ctk
import tkinter.messagebox as tkmb


class MinecraftCoordConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minecraft Coordinate Converter")
        self.geometry("450x505")  # Set initial window size
        self.resizable(False, False)  # Make window non-resizable

        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "dark-blue", "green"

        self.blocks_travel_diff = 8  # Global constant for conversion ratio

        self._create_widgets()

    def _create_widgets(self):
        # --- Input Frame ---
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(
            input_frame, text="Enter Coordinates", font=("Arial", 18, "bold")
        ).pack(pady=10)

        # X-coordinate input
        ctk.CTkLabel(input_frame, text="X-coordinate:").pack(pady=(5, 0))
        self.x_entry = ctk.CTkEntry(
            input_frame, width=200, placeholder_text="e.g., 100"
        )
        self.x_entry.pack(pady=(0, 5))

        # Z-coordinate input
        ctk.CTkLabel(input_frame, text="Z-coordinate:").pack(pady=(5, 0))
        self.z_entry = ctk.CTkEntry(
            input_frame, width=200, placeholder_text="e.g., -50"
        )
        self.z_entry.pack(pady=(0, 10))

        # --- Conversion Buttons Frame ---
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, padx=20, fill="x")

        self.ow_to_nether_button = ctk.CTkButton(
            button_frame,
            text="Overworld to Nether",
            command=self._convert_overworld_to_nether,
        )
        self.ow_to_nether_button.pack(side="left", expand=True, padx=5, pady=10)

        self.nether_to_ow_button = ctk.CTkButton(
            button_frame,
            text="Nether to Overworld",
            command=self._convert_nether_to_overworld,
        )
        self.nether_to_ow_button.pack(side="right", expand=True, padx=5, pady=10)

        # --- Result Display Frame ---
        result_frame = ctk.CTkFrame(self)
        result_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            result_frame, text="Converted Coordinates:", font=("Arial", 16, "bold")
        ).pack(pady=5)
        self.result_label = ctk.CTkLabel(
            result_frame, text="", font=("Arial", 14), wraplength=350, justify="left"
        )
        self.result_label.pack(pady=5)

    def _get_coordinates(self):
        """Helper to get and validate coordinates from entry fields."""
        x_str = self.x_entry.get().strip()
        z_str = self.z_entry.get().strip()

        try:
            x_coord = int(x_str)
            z_coord = int(z_str)
            return x_coord, z_coord
        except ValueError:
            tkmb.showerror(
                "Invalid Input",
                f"Please enter valid integer numbers for X and Z coordinates.\n"
                f"You entered X: '{x_str}', Z: '{z_str}'",
            )
            return None, None

    def _convert_overworld_to_nether(self):
        x, z = self._get_coordinates()
        if x is not None and z is not None:
            nether_x = x / self.blocks_travel_diff
            nether_z = z / self.blocks_travel_diff
            self.result_label.configure(
                text=f"Overworld ({x}, {z}) converts to Nether:\n"
                f"X: {nether_x:.2f}\nZ: {nether_z:.2f}"
            )

    def _convert_nether_to_overworld(self):
        x, z = self._get_coordinates()
        if x is not None and z is not None:
            overworld_x = x * self.blocks_travel_diff
            overworld_z = z * self.blocks_travel_diff
            self.result_label.configure(
                text=f"Nether ({x}, {z}) converts to Overworld:\n"
                f"X: {overworld_x:.2f}\nZ: {overworld_z:.2f}"
            )


# --- Main execution ---
if __name__ == "__main__":
    app = MinecraftCoordConverter()
    app.mainloop()
