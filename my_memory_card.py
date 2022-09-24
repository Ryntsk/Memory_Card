from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
 
app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()  #горизонтальная линия 
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # добавление двух вериткалей на одну горизонталь
 
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------


def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question(): 
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

answers=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score+=1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг:',(window.score/window.total*100),'%')
    else:
        show_correct('Неверно')
        print('Рейтинг:',(window.score/window.total*100),'%')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question= question
        self.right_answer= right_answer
        self.wrong1=wrong1
        self.wrong2= wrong2
        self.wrong3=wrong3
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

questions_list=[]
questions_list.append(Question('Годусадственный язык бразилии','Португальский','Бразильский','Итальянский','Испанский'))
questions_list.append(Question('Столица Китая','Пекин','Алмата','Ухань','Токио'))
questions_list.append(Question('Когда впервые человек побывал в космосе?','1961','1899','1987','2000'))
questions_list.append(Question('Apple переводится как:','яблоко','машина','книга','телефон'))
questions_list.append(Question('Какое растение существует?','Лох индийский','Лох чилийский','Лох греческий','Лох русский'))
questions_list.append(Question('Python это','Язык программирования','змея','термин','не один из вариантов'))
questions_list.append(Question('Сколько меторв в дц?','0.1','10','100','1'))
questions_list.append(Question('Что будет новом айфоне','Дизайн','Камера','Болший экран','Ничего'))
questions_list.append(Question('Мох на дереве растет на стороне','Северной','Южной','Западной','Испанский'))
questions_list.append(Question('Годусадственный язык бразилии','Португальский','Бразильский','Итальянский','Испанский'))


def next_question():
    ''' задает случайный вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
    # поэтому можно использовать локальную переменную! 
    # случайно взяли вопрос в пределах списка
    # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ''' задает следующий вопрос из списка '''
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # если список вопросов закончился - идем сначала
    q = questions_list[window.cur_question] # взяли вопрос
    ask(q) # спросили

def click_ok():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

btn_OK.clicked.connect(check_answer)
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
btn_OK.clicked.connect(click_ok) # проверяем, что панель ответов показывается при нажатии на кнопку
window.score=0
window.total=0
next_question()
window.show()
app.exec()