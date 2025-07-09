import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "Which Article of the Indian Constitution deals with the abolition of untouchability?", "options": ["Article 14", "Article 15", "Article 17", "Article 21"], "answer": "Article 17"},
    {"question": "Who was the first Governor-General of independent India?", "options": ["C. Rajagopalachari", "Lord Mountbatten", "Dr. Rajendra Prasad", "Sardar Vallabhbhai Patel"], "answer": "Lord Mountbatten"},
    {"question": "Which planet is known as the 'Morning Star'?", "options": ["Mars", "Venus", "Jupiter", "Mercury"], "answer": "Venus"},
    {"question": "Who wrote the book 'Discovery of India'?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "B. R. Ambedkar"], "answer": "Jawaharlal Nehru"},
    {"question": "What is the capital of Arunachal Pradesh?", "options": ["Itanagar", "Dispur", "Shillong", "Imphal"], "answer": "Itanagar"},
    {"question": "Which river is known as the 'Sorrow of Bihar'?", "options": ["Ganga", "Son", "Kosi", "Yamuna"], "answer": "Kosi"},
    {"question": "Who was known as the 'Iron Man of India'?", "options": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Lal Bahadur Shastri"], "answer": "Sardar Vallabhbhai Patel"},
    {"question": "Which Five-Year Plan was called the ‘Gadgil Yojana’?", "options": ["First", "Second", "Third", "Fourth"], "answer": "Third"},
    {"question": "Where is the headquarters of ISRO?", "options": ["Mumbai", "New Delhi", "Chennai", "Bengaluru"], "answer": "Bengaluru"},
    {"question": "Who was the first female governor of an Indian state?", "options": ["Indira Gandhi", "Sarojini Naidu", "Vijaya Lakshmi Pandit", "Kiran Bedi"], "answer": "Sarojini Naidu"}
]

current_question = 0
user_answers = [None] * len(questions)

window = tk.Tk()
window.title("🎓 The Trivia Titan 🎓")
window.geometry("650x500")
window.configure(bg="#FFF5E1")

header = tk.Label(window, text="🧠 The Trivia Titan 🧠", font=("Comic Sans MS", 24, "bold"), bg="#76D7C4", fg="#1B2631", pady=10)
header.pack(fill="x")

question_label = tk.Label(window, text="", wraplength=550, font=("Verdana", 16), bg="#FFF5E1", fg="#34495E")
question_label.pack(pady=20)

selected_option = tk.StringVar()
radio_buttons = []
for i in range(4):
    btn = tk.Radiobutton(window, text="", variable=selected_option, value="", font=("Arial", 14), bg="#FFF5E1", anchor="w", padx=20)
    btn.pack(fill="x", padx=50, pady=5)
    radio_buttons.append(btn)

feedback_label = tk.Label(window, text="", font=("Arial", 14, "italic"), bg="#FFF5E1")
feedback_label.pack(pady=10)

def load_question():
    q = questions[current_question]
    question_label.config(text=f"Q{current_question + 1}: {q['question']}")
    selected_option.set(user_answers[current_question] or "")
    feedback_label.config(text="")
    for i, opt in enumerate(q["options"]):
        radio_buttons[i].config(text=opt, value=opt)
    update_button_text()

def check_answer():
    selected = selected_option.get()
    if not selected:
        messagebox.showwarning("No selection", "Please select an option before proceeding.")
        return False
    user_answers[current_question] = selected
    correct = questions[current_question]["answer"]
    if selected == correct:
        feedback_label.config(text="✅ Correct!", fg="green")
    else:
        feedback_label.config(text="❌ Wrong!", fg="red")
    return True

def next_question():
    global current_question
    if not check_answer():
        return
    if current_question < len(questions) - 1:
        current_question += 1
        load_question()

def prev_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        load_question()

def submit_quiz():
    if not check_answer():
        return
    score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["answer"])
    if score >= 8:
        msg = "🌟 You're a Trivia Titan! Outstanding work!"
    elif score >= 4:
        msg = "⚡ Almost there! Brush up a little more!"
    else:
        msg = "💡 Keep learning! Titans aren’t born in a day!"
    messagebox.showinfo("Quiz Completed!", f"Your Score: {score}/10\n\n{msg}")
    window.quit()

def update_button_text():
    if current_question == len(questions) - 1:
        next_btn.config(text="Submit", command=submit_quiz, bg="#FF6F61")
    else:
        next_btn.config(text="Next ➡️", command=next_question, bg="#2ECC71")

btn_frame = tk.Frame(window, bg="#FFF5E1")
btn_frame.pack(pady=20)

prev_btn = tk.Button(btn_frame, text="⬅️ Previous", command=prev_question, font=("Arial", 12), bg="#F7DC6F", width=12)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(btn_frame, text="Next ➡️", command=next_question, font=("Arial", 12), bg="#2ECC71", width=12)
next_btn.grid(row=0, column=1, padx=10)

load_question()
window.mainloop()
