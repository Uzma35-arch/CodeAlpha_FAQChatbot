import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime

# Load FAQ Dataset
data = pd.read_csv("data/faq.csv")
questions = data["Question"].tolist()
answers = data["Answer"].tolist()

# Train Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_response(user_input):
    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    if best_score > 0.30:
        return answers[best_match_index]
    else:
        return (
            "Sorry, I don't understand that question. "
            "Please try asking something else."
        )


def send_message():
    user_message = user_entry.get().strip()

    if user_message == "":
        return

    current_time = datetime.datetime.now().strftime("%H:%M")

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(
        tk.END,
        f"[{current_time}] You: {user_message}\n"
    )

    response = get_response(user_message)

    chat_box.insert(
        tk.END,
        f"[{current_time}] Bot: {response}\n\n"
    )

    chat_box.config(state=tk.DISABLED)

    chat_box.see(tk.END)

    user_entry.delete(0, tk.END)


def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)
    chat_box.config(state=tk.DISABLED)


# Main Window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("750x600")
root.resizable(False, False)

# Header
header = tk.Label(
    root,
    text="FAQ Chatbot using Tkinter and Scikit-Learn",
    font=("Arial", 16, "bold")
)
header.pack(pady=10)

# Chat Area
chat_box = scrolledtext.ScrolledText(
    root,
    width=85,
    height=25,
    font=("Arial", 10),
    state=tk.DISABLED
)
chat_box.pack(padx=10, pady=10)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

user_entry = tk.Entry(
    input_frame,
    width=60,
    font=("Arial", 12)
)
user_entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    input_frame,
    text="Send",
    width=10,
    command=send_message
)
send_button.pack(side=tk.LEFT)

clear_button = tk.Button(
    root,
    text="Clear Chat",
    width=15,
    command=clear_chat
)
clear_button.pack(pady=10)

# Enter Key Support
user_entry.bind(
    "<Return>",
    lambda event: send_message()
)

# Welcome Message
chat_box.config(state=tk.NORMAL)
chat_box.insert(
    tk.END,
    "Bot: Welcome! Ask me a question.\n\n"
)
chat_box.config(state=tk.DISABLED)

root.mainloop()