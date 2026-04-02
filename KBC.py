import random
import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class KBCGameLogic:
    def __init__(self):
        self.questions = [
            {
                "question": "Which animal is known to be the slowest in the world?",
                "options": {"a": "Sloth", "b": "Turtle", "c": "Snail", "d": "Koala"},
                "correct_answer": "a",
            },
            {
                "question": "Which car currently holds the record for the fastest production car?",
                "options": {
                    "a": "Bugatti Chiron Super Sport 300+",
                    "b": "Koenigsegg Jesko Absolut",
                    "c": "SSC Tuatara",
                    "d": "Hennessey Venom F5",
                },
                "correct_answer": "b",
            },
            {
                "question": "What is the capital of France?",
                "options": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Rome"},
                "correct_answer": "c",
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
                "correct_answer": "b",
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": {
                    "a": "Vincent van Gogh",
                    "b": "Pablo Picasso",
                    "c": "Leonardo da Vinci",
                    "d": "Claude Monet",
                },
                "correct_answer": "c",
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": {
                    "a": "Atlantic Ocean",
                    "b": "Indian Ocean",
                    "c": "Arctic Ocean",
                    "d": "Pacific Ocean",
                },
                "correct_answer": "d",
            },
            {
                "question": "Which country is famous for the Great Wall?",
                "options": {"a": "Japan", "b": "China", "c": "India", "d": "Egypt"},
                "correct_answer": "b",
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": {"a": "O2", "b": "H2O", "c": "CO2", "d": "NaCl"},
                "correct_answer": "b",
            },
            {
                "question": "How many continents are there in the world?",
                "options": {"a": "5", "b": "6", "c": "7", "d": "8"},
                "correct_answer": "c",
            },
            {
                "question": "Which gas do plants absorb from the atmosphere?",
                "options": {
                    "a": "Oxygen",
                    "b": "Nitrogen",
                    "c": "Carbon Dioxide",
                    "d": "Hydrogen",
                },
                "correct_answer": "c",
            },
            {
                "question": "What is the highest mountain in Africa?",
                "options": {
                    "a": "Mount Everest",
                    "b": "Mount Kilimanjaro",
                    "c": "Mount Kenya",
                    "d": "Mount Elbrus",
                },
                "correct_answer": "b",
            },
            {
                "question": "What is the capital city of Australia?",
                "options": {
                    "a": "Sydney",
                    "b": "Melbourne",
                    "c": "Canberra",
                    "d": "Perth",
                },
                "correct_answer": "c",
            },
        ]
        self.current_question = None
        self.score = 0
        self.played_questions_indices = []
        self.max_questions_to_ask = 5  # Let's ask 5 questions per game for a quick play

    def start_game(self):
        self.score = 0
        self.played_questions_indices = []
        return "Game Started!"

    def get_next_question(self):
        if len(self.played_questions_indices) >= self.max_questions_to_ask:
            return None  # No more questions to ask

        available_indices = [
            i
            for i in range(len(self.questions))
            if i not in self.played_questions_indices
        ]

        if not available_indices:
            # This handles case where all questions have been asked if max_questions_to_ask >= total questions
            return None

        question_index = random.choice(available_indices)
        self.current_question = self.questions[question_index]
        self.played_questions_indices.append(question_index)

        q_text = self.current_question["question"]
        options_text = "\n".join(
            [
                f"{key.upper()}. {value}"
                for key, value in self.current_question["options"].items()
            ]
        )
        return f"{q_text}\n{options_text}"

    def check_answer(self, user_ans):
        if not self.current_question:
            return "No question active.", False

        correct_key = self.current_question["correct_answer"]
        correct_value = self.current_question["options"][correct_key]

        # Allow for 'a', 'b', 'c', 'd' or the full text answer (case-insensitive)
        if (
            user_ans.lower().strip() == correct_key.lower()
            or user_ans.lower().strip() == correct_value.lower()
        ):
            self.score += 1
            return "Correct!", True
        else:
            return (
                f"Incorrect. The correct answer was {correct_key.upper()}. {correct_value}",
                False,
            )

    def get_score(self):
        return self.score

    def get_total_questions_asked(self):
        return len(self.played_questions_indices)

    def is_game_over(self):
        return len(self.played_questions_indices) >= self.max_questions_to_ask


class KBCApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.game = KBCGameLogic()

        self.title("Kaun Banega Crorepati!")
        self.geometry("700x550")
        self.resizable(False, False)

        self._create_widgets()
        self._start_new_game_gui()  # Start game immediately on launch

    def _create_widgets(self):
        # --- Title Frame ---
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(pady=15, padx=20, fill="x")
        ctk.CTkLabel(
            title_frame, text="Kaun Banega Crorepati!", font=("Arial", 24, "bold")
        ).pack(pady=10)

        # --- Question Display Frame ---
        question_frame = ctk.CTkFrame(self)
        question_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.question_label = ctk.CTkLabel(
            question_frame,
            text="Click 'Start New Game' to begin!",
            font=("Arial", 18),
            wraplength=600,
            justify="left",
        )
        self.question_label.pack(pady=10, padx=10)

        # --- Answer Input ---
        self.answer_entry = ctk.CTkEntry(
            self,
            width=400,
            placeholder_text="Enter your answer (a, b, c, d or full text)",
        )
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind(
            "<Return>", lambda event: self._submit_answer_gui()
        )  # Allow Enter key to submit

        # --- Buttons Frame ---
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.pack(pady=10, padx=20, fill="x")

        self.submit_button = ctk.CTkButton(
            buttons_frame,
            text="Submit Answer",
            command=self._submit_answer_gui,
            width=150,
        )
        self.submit_button.pack(side="left", padx=(0, 10), expand=True)

        self.next_question_button = ctk.CTkButton(
            buttons_frame,
            text="Next Question",
            command=self._load_next_question_gui,
            state="disabled",
            width=150,
        )
        self.next_question_button.pack(side="left", padx=(10, 0), expand=True)

        # --- Game Control Frame ---
        game_control_frame = ctk.CTkFrame(self)
        game_control_frame.pack(pady=10, padx=20, fill="x")

        self.start_game_button = ctk.CTkButton(
            game_control_frame, text="Start New Game", command=self._start_new_game_gui
        )
        self.start_game_button.pack(side="left", padx=(0, 10), expand=True)

        self.score_label = ctk.CTkLabel(
            game_control_frame, text="Score: 0/0", font=("Arial", 16)
        )
        self.score_label.pack(side="right", padx=(10, 0), expand=True)

        self._update_button_states(game_active=False)

    def _start_new_game_gui(self):
        self.game.start_game()
        self._load_next_question_gui()
        self._update_button_states(game_active=True)
        self._update_score_display()
        tkmb.showinfo(
            "KBC Game", "Welcome! The game has started. Answer 5 questions to win!"
        )

    def _load_next_question_gui(self):
        if self.game.is_game_over():
            self._end_game_gui()
            return

        question_text = self.game.get_next_question()
        if question_text:
            self.question_label.configure(text=question_text)
            self.answer_entry.delete(0, ctk.END)
            self._update_button_states(
                game_active=True
            )  # Ensure buttons are enabled for new question
            self._update_score_display()
            self.answer_entry.focus_set()  # Focus on the answer entry
        else:
            self._end_game_gui()

    def _submit_answer_gui(self):
        user_answer = self.answer_entry.get().strip()
        if not user_answer:
            tkmb.showwarning("Input Error", "Please enter your answer.")
            return

        feedback_message, is_correct = self.game.check_answer(user_answer)
        self._update_score_display()

        if is_correct:
            tkmb.showinfo("Result", feedback_message)
        else:
            tkmb.showerror("Result", feedback_message)

        # After submitting, disable submit and enable next question
        self._update_button_states(game_active=False)
        self.next_question_button.configure(state="normal")
        self.answer_entry.configure(
            state="disabled"
        )  # Disable entry until next question

        if self.game.is_game_over():
            self._end_game_gui()

    def _end_game_gui(self):
        final_score = self.game.get_score()
        total_questions = self.game.max_questions_to_ask
        tkmb.showinfo(
            "Game Over!",
            f"Game Over!\nYour final score is: {final_score} out of {total_questions} questions.",
        )
        self.question_label.configure(
            text=f"Game Over! Your final score is: {final_score}/{total_questions}"
        )
        self._update_button_states(game_active=False, game_over=True)
        self.answer_entry.configure(state="disabled")

    def _update_score_display(self):
        self.score_label.configure(
            text=f"Score: {self.game.get_score()}/{self.game.get_total_questions_asked()}"
        )

    def _update_button_states(self, game_active=False, game_over=False):
        if game_active:
            self.submit_button.configure(state="normal")
            self.next_question_button.configure(
                state="disabled"
            )  # Only enable after submission
            self.start_game_button.configure(state="disabled")
            self.answer_entry.configure(state="normal")
        elif game_over:
            self.submit_button.configure(state="disabled")
            self.next_question_button.configure(state="disabled")
            self.start_game_button.configure(state="normal")
            self.answer_entry.configure(state="disabled")
        else:  # Initial state or after a question is submitted
            self.submit_button.configure(state="disabled")
            self.next_question_button.configure(state="disabled")
            self.start_game_button.configure(state="normal")
            self.answer_entry.configure(state="disabled")


# --- Main execution ---
if __name__ == "__main__":
    app = KBCApp()
    app.mainloop()
# This code is a complete implementation of a simple KBC game using customtkinter for the GUI.
# It includes game logic, GUI components, and user interaction handling.
# The game allows users to answer questions, keeps track of the score, and provides feedback.
# The game ends after 5 questions, and the user can start a new game at any time.
# The GUI is designed to be user-friendly and responsive, with appropriate feedback messages.
# The game logic is encapsulated in the KBCGameLogic class, while the GUI is handled in the KBCApp class.
# The game is initiated when the script is run, and the main loop starts the application.
# The code is structured to be easily extendable for future enhancements or additional features.
# The game is designed to be played quickly, making it suitable for casual players.
# The questions are randomly selected from a predefined list, ensuring variety in gameplay.
# The game logic includes methods for starting the game, getting the next question, checking answers,
# and determining if the game is over.
# The GUI includes buttons for submitting answers, loading the next question, and starting a new game.
# The score is displayed prominently, and the user is informed of their performance after each question.
# The game is designed to be engaging and educational, with a mix of general knowledge questions.
