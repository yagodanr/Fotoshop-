#створи тут фоторедактор Easy Editor!
from PIL import ImageFilter, Image
from PIL import ImageEnhance


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QTextEdit, QLineEdit, QListWidget, QInputDialog, QFileDialog
from os import listdir, path, mkdir
        

log = dict()
log_support = dict()
typ = "Тип"
directory = "Путь"





app = QApplication([])
win = QWidget()
win.resize(850, 600)
win.setWindowTitle("Eazy Editor")



btn1 = QPushButton("Обзор")

btn2 = QPushButton("Влево")
btn3 = QPushButton("Вправо")
btn4 = QPushButton("Зеркально")
btn5 = QPushButton("Заблюрить")
btn6 = QPushButton("Ч/Б")
btn7 = QPushButton("Констрастность")

button = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]


list_file = QListWidget()
log_list = QListWidget()


Label = QLabel("")






flag = True

#создай класс ImageEditor
class ImageProcessor():



    #создай конструктор класса
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = "Modified/"
        self.blacked = 0
    

    def loadImage(self, dir, filename):
        global flag

        log_support = dict()
        self.dir = dir
        self.filename = filename
        
        image_path = path.join(dir, filename)
        self.image = Image.open(image_path)
        
        if flag:
            log_support = dict()
            log_support[typ] = "load"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": LOAD"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True

        
    
    def show_image(self, path):
        Label.hide()
        Pixmapimage = QPixmap(path)
        w, h = Label.width(), Label.height()
        Pixmapimage = Pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        Label.setPixmap(Pixmapimage)
        Label.show()
    

    def save_image(self):
        the_path = path.join(self.dir, self.save_dir)
        if not (path.exists(the_path) or path.isdir(the_path)):
            mkdir(the_path)
        image_path = path.join(the_path, self.filename)
        self.image.save(image_path)
        



    
    
    def left(self):
        global flag

        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

        if flag:
            log_support = dict()
            log_support[typ] = "left"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": LEFT"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True

    def right(self):
        global flag

        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

        if flag:
            log_support = dict()
            log_support[typ] = "right"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": RIGHT"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True

    def flip(self):
        global flag

        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

        if flag:
            log_support = dict()
            log_support[typ] = "flip"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": FLIP"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True
    
    def blur(self):
        global flag

        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

        if flag:
            log_support = dict()
            log_support[typ] = "blur"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": BLUR"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True
    
    def bl_wh__RGB(self):
        global flag

        if flag:
            log_support = dict()
            log_support[typ] = "bl_wh__RGB"
            log_support[directory] = [self.dir, self.filename]
            

            
        





        if self.blacked == 0:
            self.bl_wh()
            
            self.blacked = 1
            if flag:
                log[str(len(log))+": bl_wh"] = log_support
        else:
            self.RGB()

            self.blacked = 0
            if flag:
                log[str(len(log))+": RGB"] = log_support
        log_list.clear()
        log_list.addItems(log.keys())
        flag = True
        
        
    def bl_wh(self):

        self.image = self.image.convert("L")

        self.save_image()
        image_path = path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)
    def RGB(self):
        global flag
        



        
        start = len(log.keys())-1
        m = start-1
        key_list = log.keys()
        keyses = list()
        for i in key_list:
            keyses.append(i)
        
        for i in range(start, 0, -1):
            k = keyses[i]
            k0 = keyses[start]
            if log[k][directory][1] != log[k0][directory][1]:
                break
            else:
                m=i
        grhh = keyses[m]
        direct = log[grhh][directory][0]
        filename = log[keyses[m]][directory][1]
        flag = False
        workimage.loadImage(direct, filename)
        for i in range(m, start+1):
            flag = False
           
            if log[keyses[i]][typ] == "left":
                workimage.left()
            elif log[keyses[i]][typ] == "right":
                workimage.right()
            elif log[keyses[i]][typ] == "flip":
                workimage.flip()
            elif log[keyses[i]][typ] == "blur":
                workimage.blur()
            elif log[keyses[i]][typ] == "contrast":
                workimage.contrast()



        self.save_image()
        image_path = path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)


    
    def contrast(self):
        global flag

        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance (1.5)
        self.save_image()
        image_path = path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)

        if flag:
            log_support = dict()
            log_support[typ] = "contrast"
            log_support[directory] = [self.dir, self.filename]
            log[str(len(log))+": CONTRAST"] = log_support

            log_list.clear()
            log_list.addItems(log.keys())
        flag = True
    
    def contur(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.save_image()
        image_path = path.join(self.dir, self.save_dir, self.filename)
        self.show_image(image_path)

    
    

#отображение картинки   
workimage = ImageProcessor()
log_workimage = ImageProcessor()

mark = 0

def showChosenImage():
    global mark
    
    if list_file.currentRow() >= 0:
        filename = list_file.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = path.join(workimage.dir, workimage.filename)
        workimage.show_image(image_path)
    
    if mark == 0:
        button[1].clicked.connect(workimage.left)
        button[2].clicked.connect(workimage.right)
        button[3].clicked.connect(workimage.flip) 
        button[4].clicked.connect(workimage.blur)
        button[5].clicked.connect(workimage.bl_wh__RGB)  
        button[6].clicked.connect(workimage.contrast)
        mark = 1





def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def filter(files, formats):
    result = []
    for filename in files:
        for form in formats:
            if filename.endswith(form):
                result.append(filename)
    return(result)

def showFilenamesList():
    formats = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
    chooseWorkdir()
    filenames = filter(listdir(workdir), formats)
    list_file.clear()
    list_file.addItems(filenames)

def showLogMoment():
    global flag
    if log_list.currentRow() >= 0:
        data = log_list.currentItem().text()
        start = int(data[0])
        m = start-1
        key_list = log.keys()
        keyses = list()
        for i in key_list:
            keyses.append(i)
        
        for i in range(start, 0, -1):
            k = keyses[i]
            k0 = keyses[start]
            if log[k][directory][1] != log[k0][directory][1]:
                break
            else:
                m=i
        grhh = keyses[m]
        direct = log[grhh][directory][0]
        filename = log[keyses[m]][directory][1]

        flag = False
        log_workimage.loadImage(direct, filename)

        log_workimage.blacked = 0

        for i in range(m, start+1):
            flag = False
            
            if log[keyses[i]][typ] == "left":
                log_workimage.left()
            elif log[keyses[i]][typ] == "right":
                log_workimage.right()
            elif log[keyses[i]][typ] == "flip":
                log_workimage.flip()
            elif log[keyses[i]][typ] == "blur":
                log_workimage.blur()
            elif log[keyses[i]][typ] == "bl_wh__RGB":
                log_workimage.bl_wh__RGB()
            elif log[keyses[i]][typ] == "contrast":
                log_workimage.contrast()
    


    
    











#отредактируй изображение и сохрани результат

main_H = QHBoxLayout()
V1 = QVBoxLayout()
V2 = QVBoxLayout()
H = QHBoxLayout()




V1.addWidget(button[0])
V1.addWidget(list_file)

V2.addWidget(Label, 80)
H.addWidget(button[1])
H.addWidget(button[2])
H.addWidget(button[3])
H.addWidget(button[4])
H.addWidget(button[5])
H.addWidget(button[6])
V2.addLayout(H, 20)


main_H.addLayout(V1, 20)
main_H.addLayout(V2, 60)
main_H.addWidget(log_list, 20)









list_file.currentRowChanged.connect(showChosenImage)
log_list.currentRowChanged.connect(showLogMoment)

button[0].clicked.connect(showFilenamesList)























win.setLayout(main_H)


win.show()
app.exec_()