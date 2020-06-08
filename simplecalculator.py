from PyQt5 import QtWidgets
import calculator
class CalcApp(QtWidgets.QMainWindow,calculator.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = ''
        self.pushButton_0.pressed.connect(lambda: self.add_item(item=0))
        self.pushButton_1.pressed.connect(lambda: self.add_item(item=1))
        self.pushButton_2.pressed.connect(lambda: self.add_item(item=2))
        self.pushButton_3.pressed.connect(lambda: self.add_item(item=3))
        self.pushButton_4.pressed.connect(lambda: self.add_item(item=4))
        self.pushButton_5.pressed.connect(lambda: self.add_item(item=5))
        self.pushButton_6.pressed.connect(lambda: self.add_item(item=6))
        self.pushButton_7.pressed.connect(lambda: self.add_item(item=7))
        self.pushButton_8.pressed.connect(lambda: self.add_item(item=8))
        self.pushButton_9.pressed.connect(lambda: self.add_item(item=9))
        self.pushButton_plus.pressed.connect(lambda: self.add_item(item='+'))
        self.pushButton_minus.pressed.connect(lambda: self.add_item(item='-'))
        self.pushButton_sub.pressed.connect(lambda: self.add_item(item='*'))
        self.pushButton_del.pressed.connect(lambda: self.add_item(item="/"))
        self.pushButton_open.pressed.connect(lambda: self.add_item(item='('))
        self.pushButton_close.pressed.connect(lambda: self.add_item(item=')'))
        self.pushButton_ce.pressed.connect(self.clear)
        self.pushButton_equal.pressed.connect(self.calculate)
    def add_item(self,item):
        self.result+=str(item)
        self.textBrowser.clear()
        self.textBrowser.append(self.result)

    def clear(self):
        self.result = ''
        self.textBrowser.clear()

    def calculate(self):
        try:
            self.result=str(eval(self.result))
            self.textBrowser.clear()
            self.textBrowser.append(str(self.result))
        except:
            self.textBrowser.clear()
            self.textBrowser.append('на ноль делить нельзя!')
            print(self.result)

app =QtWidgets.QApplication([])
window=CalcApp()
window.show()
app.exec_()