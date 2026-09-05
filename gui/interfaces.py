import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFrame, QLineEdit
)
from src.downloads import download, change_format


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TubeFetch")
        self.setFixedSize(920, 700)

        header_frame = QFrame()
        header_frame.setObjectName("header")
        header_frame.setStyleSheet("""
                    #header {
                        background-color: #2b2b2b;
                        border-radius: 13px;
                        padding: 1px;
                    }
                    QLabel { color: white; font-size: 18px; font-weight: bold; }
                    QLineEdit {border: 2px solid #89b4fa;    
                               border-radius: 5px;          
                               padding: 1px;                
                               background-color: #ffffff;    
                               color: grey;}""")
        header_frame.setFixedSize(900, 48)

        left_frame = QFrame()
        left_frame.setObjectName("left")
        left_frame.setStyleSheet("""
                    #left {
                        background-color: #2b2b2b;
                        border-radius: 10px;
                        padding: 4px;
                        }
                            """)
        left_frame.setFixedSize(560, 450)

        right_frame = QFrame()
        right_frame.setObjectName("right")
        right_frame.setStyleSheet("""
                            #right {
                                background-color: #2b2b2b;
                                border-radius: 10px;
                                padding: 4px;
                                }
                                    """)
        right_frame.setFixedSize(330, 450)

        main_layout = QVBoxLayout()
        main_layout.addWidget(header_frame)
        header_layout = QHBoxLayout(header_frame)
        info_layout = QHBoxLayout()
        down_layout = QHBoxLayout()

        info_left_layout = QVBoxLayout()
        info_left_layout.addWidget(left_frame)
        info_right_layout = QVBoxLayout()
        info_right_layout.addWidget(right_frame)

        info_layout.addLayout(info_left_layout)
        info_layout.addLayout(info_right_layout)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(info_layout)
        main_layout.addLayout(down_layout)

        down_widget = QWidget()
        down_widget.setMaximumSize(900, 200)
        down_widget.setStyleSheet(".QWidget { background-color: #2b2b2b; }")

        self.btn_push = QPushButton("Push")
        self.btn_push.setFixedSize(80, 30)
        self.btn_setting = QPushButton("Settings")
        self.btn_setting.setFixedSize(80, 30)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('Вставьте ваше url с youtube')
        self.url_input.setFixedSize(650, 30)

        header_layout.addWidget(self.btn_setting, alignment=Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(self.url_input, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        header_layout.addWidget(self.btn_push, alignment=Qt.AlignmentFlag.AlignRight)


        down_layout.addWidget(down_widget)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
