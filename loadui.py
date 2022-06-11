from functools import cache
from PyQt5.QtWidgets import *
from PyQt5 import uic 
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from helpWindow import Ui_helpWindow
import sys 
import json 
from playsound import playsound
import googletrans
import textblob
import speech_recognition as sr 
import pyttsx3 

#read from json 
f = open("themes.json")
themes = json.load(f)

engine = pyttsx3.init() 

def speechToText(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout = 5)
    response = {
    "success": True,
    "error": None,
    "transcription": None
    }
    
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["success"] = False
        response["error"] = "Unable to recognize speech"
    return response

def textToSpeech(myText):
    engine.say(myText)
    engine.runAndWait()


class UI(QMainWindow): 
        def __init__(self): 
                super(UI, self).__init__()

                
                #load the ui
                uic.loadUi("form.ui", self)

                #setam icon
                self.setWindowIcon(QIcon('resources/icon.png')) 

                # widgets 
                self.textEdit_left = self.findChild(QTextEdit, "textEdit")
                self.textEdit_right = self.findChild(QTextEdit, "textEdit_2")
                self.comboBox_left = self.findChild(QComboBox, "comboBox")
                self.comboBox_right = self.findChild(QComboBox, "comboBox_2")
                self.pushButton_MIC = self.findChild(QPushButton, "pushButton")
                self.pushButton_ASC = self.findChild(QPushButton, "pushButton_2")
                self.pushButton_TRAD = self.findChild(QPushButton, "pushButton_3")
                self.pushButton_HELP = self.findChild(QPushButton, "pushButton_4")
                self.pushButton_DEL = self.findChild(QPushButton, "pushButton_5")
                self.menubar = self.findChild(QMenuBar, "menubar")
                self.menu_About = self.findChild(QMenu, "menu_About")
                self.menuExit = self.findChild(QMenu, "menuExit")
                self.colors = self.findChild(QCheckBox, "checkBox")



                # actions 
                self.pushButton_TRAD.clicked.connect(self.translate) 
                self.pushButton_DEL.clicked.connect(self.clear)
                self.colors.clicked.connect(self.checked)

                self.pushButton_MIC.clicked.connect(self.microphone)
                self.pushButton_ASC.clicked.connect(self.listen)
                self.pushButton_HELP.clicked.connect(self.help)


                # Adaugam limbile
                # dictionar cu toate limbile
                self.languages = googletrans.LANGUAGES
                #lista cu limbile 
                self.languages_list = list(self.languages.values())
                # Adaugam in comboBox 
                self.comboBox_left.addItems(self.languages_list)
                self.comboBox_right.addItems(self.languages_list)
                # setam valorile implicite
                self.comboBox_left.setCurrentText("romanian")
                self.comboBox_right.setCurrentText("english")

                #show
                self.show()

        

        def clear(self): 
                playsound('resources/sounds/click.mp3', False)
                self.textEdit_left.setPlainText(f'')
                self.textEdit_right.setText("")
                #ComboBox
                self.comboBox_left.setCurrentText("romanian")
                self.comboBox_right.setCurrentText("english")

        def translate(self): 
                playsound('resources/sounds/click.mp3')
                try: 
                        # id-ul limbii initiale 
                        for key, value in self.languages.items():
                                if(value == self.comboBox_left.currentText()): 
                                        from_language_key = key 

                        # id-ul limbii finale 
                        for key, value in self.languages.items():
                                if(value == self.comboBox_right.currentText()): 
                                        to_language_key = key 
                        
                        #convertim textul in text blob
                        words = textblob.TextBlob(self.textEdit_left.toPlainText())

                        #traducem 
                        words = words.translate(from_lang=from_language_key, to=to_language_key)

                        #Afisam 
                        self.textEdit_right.setText(str(words))

                except Exception as ex:
                        playsound('resources/sounds/error_tone.mp3', False)
                        QMessageBox.about(self, "Eroare la traducere", str(ex)) 

        
        def checked(self):
                playsound("resources/sounds/button_click.mp3", False)
                if self.colors.isChecked() == True: 
                        qApp.setStyleSheet(
                                "QMainWindow {background-color:" + themes['on-primary'] + "}"
                                "QTextEdit {background-color:" + themes['secondary'] + "}"
                                "QComboBox {background-color:white}"
                                "QPushButton {background-color:" + themes['secondary'] + "}"
                                "QPushButton#pushButton_3 {background-color:" + themes['secondary'] + "}"
                                "QMessageBox QPushButton {background-color:" + themes['error'] + "}"
                                "QCheckBox::indicator:checked{ image: url('resources/button1.png')}"
                                "QCheckBox::indicator:unchecked{ image: url('resources/button2.png')}"
                        )
                else: 
                        qApp.setStyleSheet(
                                "QMainWindow {background-color:" + themes['primary'] + "}"
                                "QTextEdit {background-color:" + themes['secondary'] + "}"
                                "QComboBox {background-color:" + themes['primary-variant'] + "}"
                                "QPushButton {background-color:" + themes['secondary-variant'] + "}"
                                "QPushButton#pushButton_3 {background-color:" + themes['secondary'] + "}"
                                "QMessageBox QPushButton {background-color:" + themes['error'] + "}"
                                "QCheckBox::indicator:checked{ image: url('resources/button1.png')}"
                                "QCheckBox::indicator:unchecked{ image: url('resources/button2.png')}"
                        )

        
        
        def microphone(self): 
                playsound('resources/sounds/click.mp3', False) 
                recognizer = sr.Recognizer()
                microphone = sr.Microphone() 
                action = 'Listening'
                print(action)

                textToSpeech(action)

                quitFlag = True
                while(quitFlag): 
                        text = speechToText(recognizer, microphone)
                        if not text["success"] and text["error"] == "API unavailable":
                                print("ERROR: {}\nclose program".format(text["error"]))
                                break
                        while not text["success"]:
                                print("I didn't catch that. What did you say?\n")
                                text = speechToText(recognizer, microphone)

                        print(text["transcription"].lower())
                        #textToSpeech(text["transcription"].lower())
                        

                        if (text["transcription"].lower() == "stop"):
                                quitFlag = False
                                #app.closeAllWindows()
                        else:
                                self.textEdit_left.setText(text["transcription"].lower())
                        
                        


        def listen(self): 
                playsound('resources/sounds/click.mp3', False)
                textToSpeech(self.textEdit_right.toPlainText())

        def help(self): 
                playsound('resources/sounds/help_button_sound.mp3', False)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_helpWindow()
                self.ui.setupUi(self.window)
                self.window.show()

        

                


#app 
app = QApplication(sys.argv)
UiWindow = UI()

qApp.setStyleSheet(
        "QMainWindow {background-color:" + themes['primary'] + "}"
        "QTextEdit {background-color:" + themes['secondary'] + "}"
        "QComboBox {background-color:" + themes['primary-variant'] + "}"
        "QPushButton {background-color:" + themes['secondary-variant'] + "}"
        "QPushButton#pushButton_3 {background-color:" + themes['secondary'] + "}"
        "QMessageBox QPushButton {background-color:" + themes['error'] + "}"
        "QCheckBox::indicator:checked{ image: url('resources/button1.png')}"
        "QCheckBox::indicator:unchecked{ image: url('resources/button2.png')}"
)

app.exec_()