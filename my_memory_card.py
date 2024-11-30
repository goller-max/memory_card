#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Как зовут капитана Зенита в футболе  в 2024 году?', 'Дуглас Сантос', 'Артём Дзюба', 'Дмитрий Баринов', 'Хетаг Хосонов'))
question_list.append(Question('Сколько лет Дугласу Сантосу в 2024 году?', '30', '34', '28', '21'))
question_list.append(Question('Какой номер на футболке Дугласа Сантоса в 2024 году', '3', '99', '52', '22'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

question = QLabel('Как зовут капитана Зенита в футболе  в 2024 году?')

RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('Дуглас Сантос')
rbtn_2 = QRadioButton('Артём Дзюба')
rbtn_3 = QRadioButton('Дмитрий Баринов')
rbtn_4 = QRadioButton('Хетаг Хосонов')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

btn_answer = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Результаты теста:')
lb_Result = QLabel('Правильно/Неправильно')
lb_correct = QLabel('Дуглас Сантос')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_answer, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answer.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(result):
    lb_Result.setText(result)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Молодец!!!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!!!')

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def start_test():
    if btn_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.setLayout(layout_card)
btn_answer.clicked.connect(start_test)
main_win.total = 0
main_win.score = 0
next_question()
main_win.resize(400, 300)
main_win.show()
app.exec()