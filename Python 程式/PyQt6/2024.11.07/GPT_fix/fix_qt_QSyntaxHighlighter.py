import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QMenu, QFileDialog, QMessageBox
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, QKeySequence, QAction  # 修正 QAction 匯入位置
from PyQt6.QtCore import QRegularExpression

def format(color, style=''):
    _color = QColor()
    if isinstance(color, (tuple, list)):
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Weight.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format

# Syntax styles
STYLES = {
    'keyword': format([200, 120, 50], 'bold'),
    'operator': format([150, 150, 150]),
    'brace': format('darkGray'),
    'defclass': format([220, 220, 255], 'bold'),
    'string': format([20, 110, 100]),
    'string2': format([30, 120, 110]),
    'comment': format([128, 128, 128]),
    'self': format([150, 85, 140], 'italic'),
    'numbers': format([100, 150, 190]),
}

class PythonHighlighter(QSyntaxHighlighter):
    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'raise',
        'return', 'try', 'while', 'yield', 'None', 'True', 'False',
    ]

    operators = [
        r'=', r'==', r'!=', r'<', r'<=', r'>', r'>=',
        r'\+', r'-', r'\*', r'/', r'//', r'\%', r'\*\*',
        r'\+=', r'-=', r'\*=', r'/=', r'\%=',
        r'\^', r'\|', r'\&', r'\~', r'>>', r'<<',
    ]

    braces = [
        r'\{', r'\}', r'\(', r'\)', r'\[', r'\]',
    ]

    def __init__(self, document):
        super().__init__(document)
        self.tri_single = (QRegularExpression("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegularExpression('"""'), 2, STYLES['string2'])

        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword']) for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator']) for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace']) for b in PythonHighlighter.braces]

        rules += [
            (r'\bself\b', 0, STYLES['self']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        self.rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            matchIterator = expression.globalMatch(text)
            while matchIterator.hasNext():
                match = matchIterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

        self.setCurrentBlockState(0)
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        start = 0 if self.previousBlockState() == in_state else delimiter.match(text).capturedStart()
        add = delimiter.match(text).capturedLength() if start >= 0 else 0

        while start >= 0:
            match = delimiter.match(text, start + add)
            end = match.capturedStart() if match.hasMatch() else -1
            length = (end - start + add + match.capturedLength()) if end >= 0 else len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.match(text, start + length).capturedStart() if end < 0 else end
            self.setCurrentBlockState(in_state if end < 0 else 0)
        return self.currentBlockState() == in_state

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupFileMenu()
        self.setupHelpMenu()
        self.setupEditor()
        self.setCentralWidget(self.editor)
        self.resize(800, 400)

    def about(self):
        QMessageBox.about(self, "About Syntax Highlighter",
                          "<p>The <b>Syntax Highlighter</b> example shows how to perform syntax highlighting "
                          "by subclassing QSyntaxHighlighter and using regular expressions.</p>")

    def newFile(self):
        self.editor.clear()

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py *.pyw)")
        if fileName[0]:
            with open(fileName[0], encoding='utf8') as file:
                self.editor.setPlainText(file.read())

    def setupEditor(self):
        font = QFont()
        font.setFixedPitch(True)
        font.setPointSize(13)
        self.editor = QPlainTextEdit()
        self.editor.setFont(font)
        self.editor.setStyleSheet("QPlainTextEdit { font-family: 'Consolas'; color: #ccc; background-color: #2b2b2b; }")
        self.highlighter = PythonHighlighter(self.editor.document())

    def setupFileMenu(self):
        fileMenu = QMenu("&File", self)
        self.menuBar().addMenu(fileMenu)

        new_action = QAction("&New", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(self.newFile)
        fileMenu.addAction(new_action)

        open_action = QAction("&Open...", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.openFile)
        fileMenu.addAction(open_action)

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(QApplication.quit)
        fileMenu.addAction(exit_action)

    def setupHelpMenu(self):
        helpMenu = QMenu("&Help", self)
        self.menuBar().addMenu(helpMenu)

        about_action = QAction("&About", self)
        about_action.triggered.connect(self.about)
        helpMenu.addAction(about_action)

        about_qt_action = QAction("About &Qt", self)
        about_qt_action.triggered.connect(QApplication.aboutQt)
        helpMenu.addAction(about_qt_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
