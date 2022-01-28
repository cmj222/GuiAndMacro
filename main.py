

# 기본 베이스 임포트
import os
import os.path
import sys

# 이미지 인식 기능 임포트
import pytesseract
from PIL import Image

# ui 관련 임포트
from PyQt5 import QtCore
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import *
from easydict import EasyDict
from win32api import GetSystemMetrics
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


# 옆의 main.ui의 카피 패스로 경로를 따온다.
# 폼클래스를 정의한다. uic에서 ui타입을 로딩한다. 대상은 경로와 같다.
# form_class = uic.loadUiType("./main.ui")[0] 작동했던 원본. 하지만 exe로 전환시 문제됨.
# FileNotFoundError: [Errno 2] No such file or directory: './main.ui'
#uic.loadUi(r'F:\POA_program\main.ui', self)
form_class = uic.loadUiType(r'C:\Users\chlal\PycharmProjects\GuiAndMacro\main.ui')[0]


class WindowClass(QMainWindow, form_class):
    # 윈도우클래스는 q메인윈도우를 상속받아서 폼클래스로 전달할 것이다.

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ##################
        ### 변수선언구간 ###
        ##################

        # 파일경로 관련 변수
        self.model = QFileSystemModel()  # 탐색기시스템
        self.tree = self.tree_view  # 오브젝트와 연결
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 실행파일이 있는 폴더
        self.PoaMemo = str(self.BASE_DIR) + '/PoaMemo'  # 메모내용들이 담길 폴더
        self.PoaList = str(self.BASE_DIR) + '/PoaList'
        self.crawler = ''  # 탐색기에서 선택한 대상의 경로포함 폴더이름
        self.current_path = ''  # 탐색기로 경로지정해서 열은 현재 폴더경로

        ####################
        ### 자동실행 함수들 ###
        ####################

        # 첫화면 #
        self.FileSystem(self.PoaMemo)  # basePath를 받아서 파일탐색기를 띄워라

        ###########################
        ### 버튼 트리거, 반응 구간 ###
        ###########################

        # 폴더보기 버튼을 누르면 선택한 폴더를 새창에서 연다
        self.btn_OpenFile.clicked.connect(self.openMemoFolder)

        # 자동추가 버튼을 누르면 자동추가모드라는 함수를 시행한다.
        self.button_addFolder.clicked.connect(self.addMemoFolder)

        # 자동추가모드 화면에서 새로 추가를 누르면 새로추가함수를 시행한다
        self.Button_addNewImageNText.clicked.connect(self.addNewTextImage)
        self.Button_useImage_addText.clicked.connect(self.useImage_addText)
        # 보기모드 버튼을 누르면 보기모드라는 함수를 시행한다.
        self.button_view.clicked.connect(self.viewPage)


# 상단의 이미지뷰의 이미지



# 이미지 인식의 베이직
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
A = Image.open('이미지.png')
result = pytesseract.image_to_string(A, lang='kor')
result = result.replace(" ","")
print(result)
