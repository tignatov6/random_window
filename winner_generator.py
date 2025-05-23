#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
#from numba import njit
import random
import time

#создание элементов интерфейса
app = QApplication([]) # приложение
window = QWidget() #окно

#@njit
def FRandom():  
    timer1 = time.time()
    num = random.randint(1,10000000000000000000000000)
    #time.sleep(1)
    timer2 = time.time()
    a = [num, timer1,timer2]
    return a

#Функции
def ShowNumber():
    rnd = FRandom()
    lableNumber.setText(str(rnd[0]))
    print(str(float((rnd[2]-1) - rnd[1])))
    

vertLine = QVBoxLayout()
lable = QLabel('Жми чтоб получить случайное число')
lableNumber = QLabel('?')
button = QPushButton('Получить число')
button.clicked.connect(ShowNumber)

#привязка элементов к вертикальной линии
vertLine.addWidget(lable)
vertLine.addWidget(lableNumber)
vertLine.addWidget(button)
window.setLayout(vertLine)
#обработка событий

#запуск приложения
window.show() # показать окно
app.exec() # запустить приложение