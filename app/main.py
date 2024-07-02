import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import google.generativeai as genai
from dotenv import load_dotenv

# Configure Google Generative AI
load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Function to open image and display it
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global img_path
        img_path = file_path
        img = Image.open(file_path)
        img.thumbnail((350, 350))
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img

# Function to analyze the image
def analyze_image():
    if img_path:
        img = Image.open(img_path)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(["What is in this photo?", img])
        result_label.configure(text=response.text)

# Create main window
root = ctk.CTk()
root.title("Image Analysis")
root.geometry("450x550")
ctk.set_appearance_mode("dark")  

img_path = None  

# Create a scrollable frame
scrollable_frame = ctk.CTkScrollableFrame(root, width=450, height=400)
scrollable_frame.pack(pady=0, padx=0, fill="both", expand=True)

upload_icon = ctk.CTkImage(Image.open("upload_icon.png").resize((20, 20)))

open_btn = ctk.CTkButton(scrollable_frame, text=" Open Image", fg_color="#912BBC", command=open_image, image=upload_icon, compound="left")
open_btn.pack(pady=20)

img_label = ctk.CTkLabel(scrollable_frame, text="")
img_label.pack(pady=20)

submit_btn = ctk.CTkButton(scrollable_frame, text="Submit", fg_color="#912BBC", command=analyze_image)
submit_btn.pack(pady=20)

result_label = ctk.CTkLabel(scrollable_frame, text="", wraplength=400)
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
