from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton
g = 0
class Created():
    def __init__(self, name_win, question, answer, g):
        self.name_win = name_win
        self.question = question
        self.answer = answer
        self.g = g
    def create_all(self):
        app = QApplication([])
        win = QWidget()
        answer_win = QWidget()
        ase = QVBoxLayout()
        supers = QLabel('ты должен ответить!')
        ase.addWidget(
            supers, alignment = Qt.AlignCenter
            )
        answer_win.setLayout(ase)
        win.setWindowTitle(self.name_win)
        win.show()
        question = QLabel(self.question)
        a = self.answer
        button = QPushButton('Ответить')
        answer = list()
        for i in a:
            answer.append(QRadioButton(i))
        v_line = QVBoxLayout()
        h_line1 = QHBoxLayout()
        h_line2 = QHBoxLayout()

        v_line.addWidget(
            question, alignment = Qt.AlignCenter
        )
        for i in range(2):
            h_line1.addWidget(
                answer[i], alignment = Qt.AlignCenter
            )
        v_line.addLayout(h_line1)

        for i in range(2, 4):
            h_line2.addWidget(
                answer[i], alignment = Qt.AlignCenter
            )
        v_line.addLayout(h_line2)

        v_line.addWidget(
            button, alignment = Qt.AlignCenter
        )
        def not_hot():
            global ans
            ans = False
            print('not_hot')
        def hot():
            global ans
            ans = True
            print('hot')
        def super_hot():
            b = QPushButton('Следущий вопрос')
            if ans == True:
                supers.setText('Это правильный ответ!')
                self.g += 1
                print(self.g)
            else:
                supers.setText("Это не правильный ответ! ;(")
            ase.addWidget(
                b, alignment = Qt.AlignCenter
            )
            answer_win.show()
            b.clicked.connect(ass)
        def ass():
            win.close()
            answer_win.close()
        for i in range(1, 4):
            answer[i].clicked.connect(not_hot)
        answer[0].clicked.connect(hot)
        button.clicked.connect(super_hot)
        win.setLayout(v_line)
        app.exec_()
        return self.g
arsen = Created('1 вопрос из 3', 'Как меня зовут?', ['Арсен', 'Антонио', 'Даник', 'Хот потато'], g)
arsens = Created('2 вопрос из 3', 'Как думаешь ты человек?', ['Да', 'Нет', 'Наверное', 'Шкибиди доп'], arsen.create_all())
arsens = Created('3 вопрос из 3', 'Ты создан богом?', ['Я в этом уверен!', 'Нет', 'Наверное', 'Да наверное'], arsens.create_all())
print('У тебя ', arsens.create_all(), 'баллов')
