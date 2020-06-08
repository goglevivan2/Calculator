from PyQt5 import QtWidgets,QtGui
import calculator
class CalcApp(QtWidgets.QMainWindow,calculator.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = ''
        self.textEdit.clear()
        self.textEdit.append('')
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
        self.pushButton_pow.pressed.connect(lambda: self.add_item(item='^'))
        self.pushButton_ce.pressed.connect(self.clear)
        self.pushButton_equal.pressed.connect(self.calculate)
        self.pushButton_delsym.pressed.connect(self.delOneSymbol)

    def add_item(self,item):
        self.result = self.textEdit.toPlainText()
        self.result+=str(item)
        self.textEdit.clear()
        self.textEdit.append(self.result)

    def clear(self):
        self.result = self.textEdit.toPlainText()
        self.result = ''
        self.textEdit.clear()

    def calculate(self):
        try:
            self.textEdit.toPlainText().replace(' ','')
            if str(self.textEdit.toPlainText() )!= '':
                self.result = self.textEdit.toPlainText()
                self.result=self.result.replace('^','**')
                self.result=str(eval(self.result))
                self.textEdit.clear()
                self.textEdit.append(str(self.result))


        except:
            self.result = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.append('ERROR')

    def delOneSymbol(self):
        self.result = self.textEdit.toPlainText()
        self.result = self.result[:-1]
        self.textEdit.clear()
        self.textEdit.append(str(self.result))

app =QtWidgets.QApplication([])
window=CalcApp()
window.setFixedSize(331, 501)
window.setWindowIcon(QtGui.QIcon('D://calculator//icon.ico'))
window.show()
app.exec_()