import customtkinter as ctk
import tkinter.messagebox as tkmb  # For pop-up messages

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"


class CricketScoreboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cricket Scoreboard")
        self.geometry("600x750")

        # --- Game State Variables ---
        self.runs = 0
        self.wickets = 0
        self.balls_bowled = 0  # Track balls to calculate overs accurately
        self.max_wickets = 10  # Standard for cricket
        self.overs_per_game = None  # Can be set for a full match limit if needed
        self.history = []  # Stack to store state for undo

        self._create_widgets()
        self._update_display()  # Initial display update

    def _save_state(self):
        """Saves current state to history."""
        self.history.append(
            {
                "runs": self.runs,
                "wickets": self.wickets,
                "balls_bowled": self.balls_bowled,
            }
        )
        if len(self.history) > 20:  # Limit history size
            self.history.pop(0)

    def _create_widgets(self):
        # --- Score Display Frame ---
        score_display_frame = ctk.CTkFrame(
            self, fg_color="#1a1a1a", corner_radius=15, border_width=2, border_color="#333333"
        )
        score_display_frame.pack(pady=20, padx=20, fill="x")

        # Runs/Wickets Label (e.g., "123/4")
        self.label_score = ctk.CTkLabel(
            score_display_frame,
            text="0/0",
            font=("Helvetica", 80, "bold"),
            text_color="#2ecc71",
        )
        self.label_score.pack(pady=(20, 0))

        # Overs Label (e.g., "Overs: 12.3")
        self.label_overs = ctk.CTkLabel(
            score_display_frame,
            text="Overs: 0.0",
            font=("Helvetica", 32),
            text_color="#bdc3c7",
        )
        self.label_overs.pack(pady=(0, 20))

        # --- Scoring Buttons Section ---
        scoring_label = ctk.CTkLabel(self, text="Runs", font=("Helvetica", 20, "bold"))
        scoring_label.pack(pady=(10, 5))
        
        scoring_frame = ctk.CTkFrame(self, fg_color="transparent")
        scoring_frame.pack(pady=5, padx=20)

        # Run Buttons
        runs = [0, 1, 2, 3, 4, 6]
        for i, r in enumerate(runs):
            btn_text = "Dot" if r == 0 else f"+{r}"
            btn_cmd = self._add_dot_ball if r == 0 else lambda val=r: self._add_runs(val)
            btn_color = "#34495e" if r == 0 else "#2980b9"
            if r == 4 or r == 6: btn_color = "#e67e22"
            
            button = ctk.CTkButton(
                scoring_frame,
                text=btn_text,
                font=("Helvetica", 24, "bold"),
                command=btn_cmd,
                width=80,
                height=60,
                fg_color=btn_color,
                hover_color="#34495e",
            )
            button.grid(row=i//3, column=i%3, padx=10, pady=10)

        # --- Extras Section ---
        extras_label = ctk.CTkLabel(self, text="Extras", font=("Helvetica", 20, "bold"))
        extras_label.pack(pady=(20, 5))
        
        extras_frame = ctk.CTkFrame(self, fg_color="transparent")
        extras_frame.pack(pady=5, padx=20)
        
        extra_btns = [
            ("Wide", self._add_wide),
            ("No Ball", self._add_no_ball),
            ("Wicket", self._add_wicket)
        ]
        
        for i, (text, cmd) in enumerate(extra_btns):
            btn_color = "#f39c12" if "Ball" in text or "Wide" in text else "#c0392b"
            button = ctk.CTkButton(
                extras_frame,
                text=text,
                font=("Helvetica", 20, "bold"),
                command=cmd,
                width=130,
                height=60,
                fg_color=btn_color,
                hover_color="#e74c3c" if "Wicket" in text else "#d35400"
            )
            button.grid(row=0, column=i, padx=10, pady=10)

        # --- Controls Section ---
        controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        controls_frame.pack(pady=30, padx=20, fill="x")

        self.button_undo = ctk.CTkButton(
            controls_frame,
            text="Undo",
            font=("Helvetica", 20),
            command=self._undo_last_action,
            width=150,
            height=50,
            fg_color="#7f8c8d",
            hover_color="#95a5a6"
        )
        self.button_undo.pack(side="left", expand=True, padx=10)

        self.button_reset = ctk.CTkButton(
            controls_frame,
            text="Reset",
            font=("Helvetica", 20),
            command=self._reset_score,
            width=150,
            height=50,
            fg_color="#34495e",
            hover_color="#2c3e50"
        )
        self.button_reset.pack(side="right", expand=True, padx=10)

    def _update_display(self):
        """Updates the labels with current runs, wickets, and overs."""
        overs_full = self.balls_bowled // 6
        overs_balls = self.balls_bowled % 6
        self.label_score.configure(text=f"{self.runs}/{self.wickets}")
        self.label_overs.configure(text=f"Overs: {overs_full}.{overs_balls}")

    def _show_all_out_message(self):
        """Displays an alert when all batsmen are out."""
        tkmb.showinfo("All Out!", "All batsmen are out! Innings complete.")
        # Optionally disable all run/wicket buttons here
        self._toggle_buttons(False)

    def _toggle_buttons(self, enable: bool):
        """Enables or disables relevant buttons."""
        for (
            child
        ) in self.children.values():  # Iterate through all widgets in the window
            if isinstance(child, ctk.CTkFrame):
                for (
                    btn_child
                ) in child.winfo_children():  # Iterate through widgets in frames
                    if isinstance(btn_child, ctk.CTkButton) and btn_child not in [
                        self.button_reset
                    ]:  # Exclude reset
                        btn_child.configure(state="normal" if enable else "disabled")
        # Specifically re-enable reset button
        self.button_reset.configure(state="normal")

    def _add_runs(self, run_value):
        """Adds runs to the score and updates overs."""
        if self.wickets < self.max_wickets:
            self._save_state()
            self.runs += run_value
            self.balls_bowled += 1
            self._update_display()
            if (
                self.wickets == self.max_wickets
            ):  # Check again after adding runs if a wicket might have caused "all out" from previous action
                self._show_all_out_message()
        else:
            self._show_all_out_message()

    def _add_dot_ball(self):
        """Increments ball count without adding runs."""
        if self.wickets < self.max_wickets:
            self._save_state()
            self.balls_bowled += 1
            self._update_display()
        else:
            self._show_all_out_message()

    def _add_wide(self):
        """Adds 1 run for wide, doesn't increment ball count."""
        if self.wickets < self.max_wickets:
            self._save_state()
            self.runs += 1
            self._update_display()
        else:
            self._show_all_out_message()

    def _add_no_ball(self):
        """Adds 1 run for no ball, doesn't increment ball count."""
        if self.wickets < self.max_wickets:
            self._save_state()
            self.runs += 1
            self._update_display()
        else:
            self._show_all_out_message()

    def _add_wicket(self):
        """Adds a wicket to the score."""
        if self.wickets < self.max_wickets:
            self._save_state()
            self.wickets += 1
            self.balls_bowled += 1  # A wicket also counts as a ball
            self._update_display()
            if self.wickets == self.max_wickets:
                self._show_all_out_message()
        else:
            self._show_all_out_message()

    def _undo_last_action(self):
        """Reverts to the previous state."""
        if self.history:
            state = self.history.pop()
            self.runs = state["runs"]
            self.wickets = state["wickets"]
            self.balls_bowled = state["balls_bowled"]
            self._update_display()
            self._toggle_buttons(True)
        else:
            tkmb.showinfo("Undo", "No actions to undo.")

    def _reset_score(self):
        """Resets all score variables to zero."""
        confirm = tkmb.askyesno(
            "Reset Score", "Are you sure you want to reset the score?"
        )
        if confirm:
            self._save_state()
            self.runs = 0
            self.wickets = 0
            self.balls_bowled = 0
            # Keep history so reset can be undone
            self._update_display()
            self._toggle_buttons(True)  # Re-enable buttons after reset


# --- Main execution ---
if __name__ == "__main__":
    app = CricketScoreboard()
    app.mainloop()
