from datetime import datetime
import tkinter as tk
import webbrowser

students = {
    1: ('vasyl', '10b'),
    2: ('andriy', '11b'),
    3: ('petro', '9b'),
    4: ('yuriy', '10a'),
    5: ('kateryna', '10a')
}
school_info = {
    "Назва школи": "Школа №1",
    "Місцезнаходження": "Київ",
    "Навчальна програма": "Інформатика та програмування",
    "Кількість учнів": 500,
    "Рівень освіти": "Середня школа",
    "Спеціалізація": "Інформатика"
}
def show_webbrauser():
    webbrowser.open('https://github.com/dashboard')

def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000,show_time)
    

def show_custom_message():
    custom_window = tk.Toplevel(root)
    custom_window.title("тисни якщо хочеш побачити наше превю")
    custom_window.geometry('800x1000')
    custom_window.configure(bg='#b3e0ff')
    message_text = (
        "Ласкаво просимо в інноваційну програму нашої школи, яка пропонує високотехнологічний підхід до навчання та розвитку учнів! "
        "Наша програма шкільної інформатики та технологій розроблена для того, щоб готувати учнів до високотехнологічного світу, що постійно змінюється. "
        "Основні можливості програми:\n"
        "Інтегроване Навчання Програмування:\n"
        "Наша програма надає учням можливість вивчати мови програмування на різних рівнях складності. "
        "Від основних концепцій до розробки власних проектів, ми стимулюємо та підтримуємо інтерес учнів до світу програмування.\n"
              "Проекти з Інформаційних Технологій:\n"
        "Учні отримають можливість впроваджувати свої ідеї в життя через розробку інформаційних технологій. "
        "Вони будуть залучені до створення веб-сайтів, мобільних додатків та інших цифрових проектів.\n"
        "\n"
        "Комп'ютерна Графіка та Дизайн:\n"
        "Наша програма пропонує курси з комп'ютерної графіки та дизайну, де учні можуть розвивати свої творчі та технічні навички в області "
        "візуального мистецтва та дизайну.\n"
        "\n"
        "Курси Кібербезпеки:\n"
        "У зв'язку з зростаючими викликами в галузі кібербезпеки, наші учні вивчатимуть основи безпеки в Інтернеті, етику та техніки захисту від кібератак.\n"
        "\n"
        "Зв'язок з Високотехнологічними Компаніями:\n"
        "Ми прагнемо забезпечити наших учнів можливістю взаємодії та співпраці з представниками високотехнологічних компаній, "
        "щоб вони могли отримати реальний досвід та поради від професіоналів цієї галузі.\n"
        "\n"
        "Приєднуйтеся до нашої програми та допоможіть своїм дітям розкрити свій потенціал у світі інформаційних технологій!"
    )

    for line in message_text.split('\n'):
        label = tk.Label(custom_window, text=line, width=80, font=('Arial', 14), bg='lightblue', wraplength=800, justify=tk.LEFT)
        label.grid()


def show_custom_message_1():
    global school_info
    custom_window_1 = tk.Toplevel(root)
    custom_window_1.title('інфо')
    custom_window_1.geometry('500x350')
    custom_window_1.configure(bg='#b3e0ff')
    message_text = "Загальна інформація про школу:\n"
    for school_data,school_datas in school_info.items():
        message_text += f'{school_data} : {school_datas}\n'
    label = tk.Label(custom_window_1, text=message_text, width=50, font=('Arial', 14),bg='lightblue',)
    label.grid()


def show_custom_message_2():
    global students
    custom_window_2 = tk.Toplevel(root)
    custom_window_2.title('інфо')
    custom_window_2.geometry('300x275')
    custom_window_2.configure(bg='#b3e0ff')
    message_text = "Список нових учнів:\n"
    for student_id, (student_name,student_class) in students.items():
        message_text += f"{student_id}. {student_name} - {student_class}\n"
    label = tk.Label(custom_window_2,text=message_text,width=20, font=('Arial', 14),bg='lightblue')
    label.grid()
# Створення головного вікна
root = tk.Tk()
root.title("школа")
root.geometry('750x400')
root.configure(bg='#b3e0ff')

# Створення кнопок для відображення власних повідомлень
main_label_text = "Ласкаво просимо в нашу школу!\nМи пропонуємо різні послуги та інформацію."
main_label = tk.Label(root, text=main_label_text, font=('Arial', 18), bg='lightblue')
main_label.grid(pady=20)

button_1 = tk.Button(root, text="Що ми надаємо", command=show_custom_message, width=12, height=2, font=('Arial', 16), fg='white', bg='grey')
button_1.grid(row=6, column=0, padx=20, pady=20, sticky=tk.NE)

button_2 = tk.Button(root, text="Інфо про школу", command=show_custom_message_1, width=12, height=2, font=('Arial', 16), fg='white', bg='grey')
button_2.grid(row=6, column=1, padx=10, pady=20, sticky=tk.W)

button_3 = tk.Button(root, text="Список учнів", command=show_custom_message_2, width=12, height=2, font=('Arial', 16), fg='white', bg='grey')
button_3.grid(row=5, column=0, padx=20, pady=20, sticky=tk.SE)

button_4 = tk.Button(root, text="Відкрити веб-сайт", command=show_webbrauser, width=15, height=2, font=('Arial', 16), fg='white', bg='grey')
button_4.grid(row=5, column=1, padx=10, pady=20, sticky=tk.S)

time_label = tk.Label(root, text='', font=('Arial', 24), bg='#b3e0ff')
time_label.grid(row=9, column=0, columnspan=2, pady=20)



show_time()
root.mainloop()
