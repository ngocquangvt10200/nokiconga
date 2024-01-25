import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("nokiconga")

        # Danh sách các câu hỏi và đáp án
        self.questions = [
            {
                'question_text': 'Our anniversary:',
                'image_path': 'noki/1.png',
                'options': [
                    'noki/1.1.png',
                    'noki/1.2.png',
                    'noki/1.3.png'
                ],
                'correct_option': 2
            },
            {
                'question_text': 'Ai nhìn ngáo nhất:',
                'image_path': 'noki/2.png',
                'options': [
                    'noki/2.1.png',
                    'noki/2.2.png',
                    'noki/2.3.png'
                ],
                'correct_option': 1
            },
            {
                'question_text': 'Most replayed song:',
                'image_path': 'noki/3.png',
                'options': [
                    'noki/3.1.png',
                    'noki/3.2.png',
                    'noki/3.3.png'
                ],
                'correct_option': 0
            },
            {
                'question_text': 'If I am sad, where can you find me?',
                'image_path': 'noki/4.png',
                'options': [
                    'noki/4.1.png',
                    'noki/4.2.png',
                    'noki/4.3.png'
                ],
                'correct_option': 1
            },
            {
                'question_text': 'Most nom nom food:',
                'image_path': 'noki/5.png',
                'options': [
                    'noki/5.1.png',
                    'noki/5.2.png',
                    'noki/5.3.png'
                ],
                'correct_option': 2
            },
            
            # Thêm các câu hỏi khác tại đây
        ]

        self.current_question_index = 0
        self.current_question = self.questions[self.current_question_index]

        # Kích thước mặc định cho tất cả hình ảnh
        self.image_size = (450, 300)

        # Font và kích thước chữ mới
        self.font = ('Helvetica', 18, 'bold')

        # Hiển thị câu hỏi đầu tiên
        self.display_question()

    def display_question(self):
        self.clear_widgets()

        # Hiển thị hình ảnh câu hỏi
        image_path = self.current_question['image_path']
        question_image = Image.open(image_path)
        question_image = question_image.resize(self.image_size)
        self.photo = ImageTk.PhotoImage(question_image)
        self.image_label = tk.Label(self.master, image=self.photo)
        self.image_label.pack()

        # Hiển thị câu hỏi văn bản
        self.question_label = tk.Label(self.master, text=self.current_question['question_text'], font=self.font)
        self.question_label.pack()

        # Hiển thị tùy chọn đáp án theo hàng ngang
        answer_frame = tk.Frame(self.master)
        answer_frame.pack()

        self.answer_buttons = []
        for i, option_path in enumerate(self.current_question['options']):
            option_image = Image.open(option_path)
            option_image = option_image.resize(self.image_size)
            option_photo = ImageTk.PhotoImage(option_image)

            button = tk.Button(answer_frame, image=option_photo, command=lambda idx=i: self.check_answer(idx))
            button.photo = option_photo
            self.answer_buttons.append(button)
            button.pack(side=tk.LEFT, padx=10)  # Sắp xếp nút theo hàng ngang với khoảng cách là 10

    def check_answer(self, selected_option):
        correct_option = self.current_question['correct_option']
        result_text = "Chính xác!!! Em đã được 1.000 đồng$$$!" if selected_option == correct_option else "Gà wáaaaaaaa! Sai rùi. Thặc ngul ngok"

        # Hiển thị thông báo pop-up
        messagebox.showinfo("Kết quả", result_text)

        # Nếu chọn đáp án đúng, chuyển sang câu hỏi tiếp theo
        if selected_option == correct_option:
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.current_question = self.questions[self.current_question_index]
                self.display_question()
            else:
                messagebox.showinfo("Kết thúc", "Chúc mừng em đã dành chiến thắng. Vui lòng chụp màn hình gửi anh để được 5.000 đồng $$$!")
        else:
            # Nếu chọn đáp án sai, không chuyển câu hỏi
            pass

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
