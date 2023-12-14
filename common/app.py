import os
import sys
import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette, QBrush
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QSpacerItem, QSizePolicy

from web import configs

version = 'v1.1.4.3'


# 使用一个子线程打开浏览器
def open_baas():
    configs.check_config()
    webbrowser.open_new('http://localhost:1117/')


def start():
    # 创建应用实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    window = QWidget()
    window.setWindowTitle('蔚蓝档案-BAAS')
    window.setFixedSize(660, 250)

    base_path = ''
    # 如果我们是在 PyInstaller 打包后的版本中运行，那么改变 base_path 到正确的目录
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    # 创建一个QPixmap对象来加载图片
    pixmap = QPixmap(os.path.join(base_path, 'assets/images/fm.jpeg'))

    # 创建一个QPalette对象来设置窗口背景
    palette = QPalette()

    # 使用画笔工具设置背景图片，按比例伸缩填充整个窗口
    brush = QBrush(pixmap.scaled(window.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))

    palette.setBrush(QPalette.Window, brush)
    window.setPalette(palette)

    # 创建一个垂直布局器
    layout = QVBoxLayout()
    layout.setSpacing(0)
    lab = QLabel(
        '<!DOCTYPE html> <html> <head> <style> .centered-text { color: white; text-shadow: 4px 4px 8px #000000; font-size: 15px; font-weight: 600; font-style: italic; } </style> </head> <body> <p align="center"><span class="centered-text">【Baas】是一款完全免费开源的蔚蓝档案自动化脚本，如遇收费请立即退款！</span></p> <p align="center"><span class="centered-text">项目开源地址：https://github.com/baas-pro/baas</span></p> <p align="center"><span class="centered-text">QQ交流群：621628600</span></p></body> </html>')
    lab.setAlignment(Qt.AlignCenter)
    lab.setTextInteractionFlags(Qt.TextSelectableByMouse)
    layout.addWidget(lab)
    spacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)
    layout.addItem(spacer)
    btn = QPushButton('打开Baas')
    btn.setStyleSheet("""
    QPushButton {
        background-color: #00B0FF;
        color: white;
        font-weight:bold;
        border-style: solid;
        border-radius: 3px; 
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #40C4FF; 
    }
    QPushButton:pressed {
        background-color: #00B0FF;
    }
""")
    btn.clicked.connect(open_baas)

    btn.setFixedSize(88, 28)
    layout.addWidget(btn, 0, Qt.AlignCenter)

    v = QLabel(f'<span style="color:white;font-weight:bold;font-style: italic;">Version: {version} </span>')
    layout.addWidget(v, 0, Qt.AlignRight)

    layout.setContentsMargins(0, 5, 0, 5)
    window.setLayout(layout)

    # 显示窗口
    window.show()
    # 运行程序
    sys.exit(app.exec())
