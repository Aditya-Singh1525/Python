import requests
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("405x175")
app.title("Weather App")

def on_button_click():
    city = entry.get()
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    label.configure(text=f"Weather of {response.text}")

label = ctk.CTkLabel(app, text="Enter a city name:", font=("Arial", 20))
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="City name")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Get Weather", command=on_button_click)
button.pack(pady=10)
app.mainloop()
