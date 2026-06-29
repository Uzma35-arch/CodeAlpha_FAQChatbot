# 🤖 FAQ Chatbot

A simple desktop-based FAQ Chatbot developed using **Python**, **Tkinter**, and **Scikit-learn**. The chatbot answers frequently asked questions related to **Python Programming** and **Artificial Intelligence** by matching user input with the most relevant question stored in a CSV dataset.

---

## 📌 Features

* Interactive Graphical User Interface (GUI)
* Built with Tkinter
* Answers Frequently Asked Questions (FAQs)
* Uses Machine Learning for text similarity
* Reads questions and answers from a CSV file
* Easy to customize by adding more FAQs
* Fast and lightweight desktop application

---

## 🛠 Technologies Used

* Python 3.x
* Tkinter
* Pandas
* Scikit-learn
* NumPy

---

## 📂 Project Structure

```
FAQChatbot/
│
├── main.py              # Main application
├── faq.csv              # Questions and answers dataset
├── README.md            # Project documentation
├── requirements.txt     # Required Python libraries
└── screenshots/
      ├── home.png
      └── chatbot.png
```

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FAQChatbot.git
```

### 2. Open the Project Folder

```bash
cd FAQChatbot
```

### 3. Install Required Libraries

```bash
pip install pandas
pip install numpy
pip install scikit-learn
```

or

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

The chatbot window will open.

---

## 📄 Dataset Format

The chatbot reads questions from a CSV file.

Example:

| Question                  | Answer                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------- |
| What is Python?           | Python is a programming language.                                                       |
| What is AI?               | Artificial Intelligence enables machines to perform tasks requiring human intelligence. |
| What is Machine Learning? | Machine Learning is a branch of AI that learns from data.                               |

The CSV file must contain these columns:

```
Question
Answer
```

---

## 🧠 How It Works

1. Loads the FAQ dataset using Pandas.
2. Converts all questions into numerical vectors using **TF-IDF Vectorizer**.
3. Converts the user's question into a vector.
4. Computes **Cosine Similarity** between the user query and all stored questions.
5. Returns the answer with the highest similarity score.

---

## 💬 Example

**User:**

```
What is Python?
```

**Bot:**

```
Python is a high-level programming language used for web development, AI, data science, automation, and many other applications.
```

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/home.png
screenshots/chatbot.png
```

---

## 🚀 Future Improvements

* Voice input
* Voice output
* Dark mode
* Database support
* Online API integration
* Better Natural Language Processing
* Multiple chatbot themes
* User login system
* Chat history
* Export conversations

---

## 🎯 Learning Objectives

This project demonstrates:

* Python Programming
* GUI Development with Tkinter
* Data Handling using Pandas
* Machine Learning Basics
* Natural Language Processing
* Text Vectorization
* Cosine Similarity
* CSV File Handling

---

## 📋 Requirements

* Python 3.10 or later
* Pandas
* NumPy
* Scikit-learn
* Tkinter

---

## 👩‍💻 Author

**Uzma Gul**

Student Project

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and improve this project for educational purposes.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork the project
* 🛠 Contribute improvements
* 🐞 Report bugs by opening an issue

Thank you for visiting this project!
