import random, sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.create_widgets()

    def create_widgets(self):
        #------
        self.hiragana = {"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か":"ka", "き":"ki", "く":"ku",
 "け": "ke", "こ": "ko", "さ": "sa", "し": "shi", "す" :"su", "せ": "se",
 "そ":"so", "た":"ta","ち": "chi", "つ": "tsu", "て":"te", "と":"to", "な":"na",
 "に":"ni", "ぬ":"nu", "ね":"ne","の":"no","は":"ha", "ひ":"hi", "ふ":"fu",
 "へ":"he", "ほ":"ho", "ま":"ma", "み":"mi", "む":"mu", "め":"me", "も":"mo",
 "や":"ya", "ゆ":"yu", "よ":"yo", "ら":"ra", "り":"ri","る":"ru","れ": "re",
 "ろ":"ro", "わ":"wa","を":"wo","ん":"n"}
        self.simples = list(self.hiragana.keys())
        random.shuffle(self.simples)
        #------

        self.lbl = QtWidgets.QLabel("にほん")
        self.lbl.setFont(QtGui.QFont("SansSerif",30))
        self.lbl2 = QtWidgets.QLabel("")
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Start")
        self.btn.setToolTip("you ca use the <b>Tab</b> button")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.lbl)
        h_box.addStretch()

        h2_box = QtWidgets.QHBoxLayout()
        h2_box.addStretch()
        h2_box.addWidget(self.lbl2)
        h2_box.addStretch()

        hbt_box = QtWidgets.QHBoxLayout()
        hbt_box.addStretch()
        hbt_box.addWidget(self.btn)
        hbt_box.addStretch()

        hv_box = QtWidgets.QVBoxLayout()
        hv_box.addLayout(h_box)
        hv_box.addLayout(h2_box)
        hv_box.addWidget(self.le)
        hv_box.addLayout(hbt_box)



        self.setLayout(hv_box)
        self.show()
#-----------------------------------------------------------------------------------------------------------------------

class Pylc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pylc, self).__init__()
        self.w = Window()
        self.setCentralWidget(self.w)
        self.create_widgets()

    def create_widgets(self):
        bar = self.menuBar()
        self.stat = self.statusBar()
        self.sho = False

        file = bar.addMenu("File")
        view = bar.addMenu("View")
        cards = bar.addMenu("Card")


        quit_action = QtWidgets.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        next_action = QtWidgets.QAction("&Next", self)
        next_action.setShortcut(QtCore.Qt.Key_Tab)
        answer_action = QtWidgets.QAction("Answers", self, checkable = True)
        answer_action.setChecked(False)
        kana_action = QtWidgets.QMenu("Kanas", self)
        hiragana_action = QtWidgets.QAction("Hiragana", self)
        katakana_action= QtWidgets.QAction("Katakana", self)


        file.addAction(quit_action)
        view.addAction(answer_action)
        view.addAction(next_action)
        cards.addMenu(kana_action)
        kana_action.addAction(hiragana_action)
        kana_action.addAction(katakana_action)


        quit_action.triggered.connect(QtWidgets.QApplication.instance().quit)
        self.w.btn.clicked.connect(self.start_check)
        answer_action.triggered.connect(self.togglemenu)
        next_action.triggered.connect(self.w.btn.click)
        katakana_action.triggered.connect(self.katakana)
        hiragana_action.triggered.connect(self.hiragan)





        self.show()
        self.setWindowTitle("にほん")

    def start_check(self):
        name = self.sender().text()
        if name == "Start":
            self.w.btn.setText("Check")
            self.w.lbl.setText(self.w.simples.pop())
            if self.sho:
                self.stat.showMessage(self.w.hiragana[self.w.lbl.text()])
            else:
                pass
            self.w.lbl2.setText("how do you pronounce it?")
        else:
            if self.w.le.text() == self.w.hiragana[self.w.lbl.text()]:
                self.w.lbl2.setText("Correct")
                try:
                    self.w.lbl.setText(self.w.simples.pop())
                    if self.sho:
                        self.stat.showMessage(self.w.hiragana[self.w.lbl.text()])
                    else:
                        pass
                except:
                    self.w.lbl2.setText("no more things")
                    self.w.lbl.setText("にほん")
                    self.w.btn.setText("Start")
                    self.w.simples = list(self.w.hiragana.keys())
                    random.shuffle(self.w.simples)

            else:
                self.w.lbl2.setText("you're wrong")
            self.w.le.clear()

    def togglemenu(self, state):
        if state:
            self.stat.show()
            self.sho = True
            try:
                self.stat.showMessage(self.w.hiragana[self.w.lbl.text()])
            except:
                self.stat.showMessage("-")

        else:
            self.stat.hide()
            self.sho = False

    def katakana(self):
        if self.w.btn.text() == "Start":
            self.w.hiragana ={"ア":"a", "イ":"i", "ウ": "u", "エ":"e", "オ":"o"}
            self.w.simples = list(self.w.hiragana.keys())
            random.shuffle(self.w.simples)

        else:
            self.w.lbl2.setText("you have to finis this deck first")

    def hiragan(self):
        if self.w.btn.text() == "Start":
            self.w.hiragana = {"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か":"ka", "き":"ki", "く":"ku",
 "け": "ke", "こ": "ko", "さ": "sa", "し": "shi", "す" :"su", "せ": "se",
 "そ":"so", "た":"ta","ち": "chi", "つ": "tsu", "て":"te", "と":"to", "な":"na",
 "に":"ni", "ぬ":"nu", "ね":"ne","の":"no","は":"ha", "ひ":"hi", "ふ":"fu",
 "へ":"he", "ほ":"ho", "ま":"ma", "み":"mi", "む":"mu", "め":"me", "も":"mo",
 "や":"ya", "ゆ":"yu", "よ":"yo", "ら":"ra", "り":"ri","る":"ru","れ": "re",
 "ろ":"ro", "わ":"wa","を":"wo","ん":"n"}
            self.w.simples = list(self.w.hiragana.keys())
            random.shuffle(self.w.simples)
        else:
            self.w.lbl2.setText("you can't do that now")






app = QtWidgets.QApplication(sys.argv)
w = Pylc()
sys.exit(app.exec_())
