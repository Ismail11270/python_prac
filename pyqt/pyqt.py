import PyQt5.QtWidgets as qt
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class Window(qt.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 Lab')
        self.setGeometry(500, 300, 800, 600)
        # Init tabs
        self.tab1 = qt.QWidget()
        self.tab2 = qt.QWidget()
        self.tab3 = qt.QWidget()
        self.tabs = qt.QTabWidget()
        self.tabOneLayout = qt.QHBoxLayout()
        self.tabTwoLayout = qt.QHBoxLayout()
        self.tabThreeLayout = qt.QHBoxLayout()
        self.setCentralWidget(self.tabs)
        self.initTabs()
        # Set menu action
        # File menu
        self.exitAction = qt.QAction('Exit', self)
        # Task 1 menu actions
        self.openTaskOne = qt.QAction('Open', self)
        # Task 2 menu actions
        self.clearTaskTwo = qt.QAction('Clear', self)
        self.openTaskTwo = qt.QAction('Open', self)
        self.saveTaskTwo = qt.QAction('Save', self)
        self.saveAsTaskTwo = qt.QAction('Save As', self)
        # Task 3 menu actions
        self.clearTaskThree = qt.QAction('Clear', self)
        self.prepareMenu()

    def prepareMenu(self):
        # File menu prep
        fileMenu = self.menuBar().addMenu("File")
        self.exitAction.setShortcut("Alt+F4")
        fileMenu.addAction(self.exitAction)
        # Task 1 menu prep
        taskOneMenu = self.menuBar().addMenu("Task 1")
        self.openTaskOne.setShortcut("Ctrl+G")
        taskOneMenu.addAction(self.openTaskOne)
        # Task 2 menu prep
        taskTwoMenu = self.menuBar().addMenu("Task 2")
        self.clearTaskTwo.setShortcut("Ctrl+W")
        self.openTaskTwo.setShortcut("Ctrl+O")
        self.saveTaskTwo.setShortcut("Ctrl+S")
        self.saveAsTaskTwo.setShortcut("Ctrl+K")
        taskTwoMenu.addActions([self.clearTaskTwo, self.openTaskTwo, self.saveTaskTwo, self.saveAsTaskTwo])
        # Task 3 menu prep
        taskThreeMenu = self.menuBar().addMenu("Task 3")
        self.clearTaskThree.setShortcut("Ctrl+Q")
        taskThreeMenu.addAction(self.clearTaskThree)
        # Triggers
        fileMenu.triggered.connect(self.handleMenuTrigger)
        taskOneMenu.triggered.connect(self.handleMenuTrigger)
        taskTwoMenu.triggered.connect(self.handleMenuTrigger)
        taskThreeMenu.triggered.connect(self.handleMenuTrigger)

    def handleMenuTrigger(self, action: qt.QAction):
        if action == self.exitAction:
            self.close()
        if action == self.openTaskOne:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab1))
            self.openImage()
        elif action == self.clearTaskTwo:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab2))
            # todo
        elif action == self.openTaskTwo:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab2))
            # todo
        elif action == self.saveTaskTwo:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab2))
            # todo
        elif action == self.saveAsTaskTwo:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab2))
            # todo
        elif action == self.clearTaskThree:
            self.tabs.setCurrentIndex(self.tabs.indexOf(self.tab3))
            # todo

    def openImage(self):
        fileName, selectedFilter = qt.QFileDialog.getOpenFileName(self, "Select an image file", "",
                                                                  "All Files (*);; JPG (*.jpg);; "
                                                                  "PNG (*.png);; GIF (*.gif)")
        if not fileName:
            return
        x = self.tabOneLayout.itemAt(0)
        img: qt.QLabel
        if x:
            img = x.widget()
        else:
            img = qt.QLabel()
            self.tabOneLayout.addWidget(img)
        pixmap = qtg.QPixmap(fileName)
        resized = pixmap.scaled(self.tab1.width(), self.tab1.height(), qtc.Qt.KeepAspectRatio)
        img.setPixmap(resized)

    def initTabs(self):
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.setMovable(True)
        self.tab1.setLayout(self.tabOneLayout)
        self.tab2.setLayout(self.tabTwoLayout)
        self.tab3.setLayout(self.tabThreeLayout)


if __name__ == '__main__':
    app = qt.QApplication([])
    window = Window()
    window.show()
    app.exec_()