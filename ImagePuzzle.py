# ImagePuzzle
# 	author: Zhu Sun
#	email:	sun.zhu@ubisoft.com
#	built date:				2015/3/18
#	latest updated date:	2015/3/19
# 	Here is a tool to arrange image sequence onto a single image easily, which is useful to the artist who make motion texture. 
# 	It is based on PySide and PIL which should be installed in order to ImagePuzzle works.
#	Enjoy it.

from PySide import QtGui,QtCore
import sys
import Image
import ImagePuzzle_UI

class ImageFileListWidget(QtGui.QListWidget):
	def Setup(self):
		self.setDragEnabled(True)
		self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
		self.setSortingEnabled(True)
		self.sortOrder=0
		
	def mousePressEvent(self,event):
		print "mousePressEvent"
	
	def IsImageFile(self,fileName):
		imageExtList=[".tif",".tiff",".jpg",".bmp",".tga","png"]
		for ext in imageExtList:
			if fileName.find(ext) != -1:
				return True
		return False
		
	def dragEnterEvent(self,event):
		print "dragEnterEvent"
		urls=event.mimeData().urls()
		for url in urls:
			imageFile=url.path()[1:]
			if self.IsImageFile(imageFile) and not self.findItems(imageFile,QtCore.Qt.MatchExactly):
				self.addItem(imageFile)
		
		self.sortItems(QtCore.Qt.AscendingOrder)
		
	def dropEvent(self,event):
		print "dropEvent"
		
def pil2pixmap(im):
    if im.mode != "RGB":
        im = im.convert("RGB")
    data = im.tostring()
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap
	
class ImagePuzzle(QtGui.QWidget,ImagePuzzle_UI.Ui_ImagePuzzle):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		self.retranslateUi(self)
		self.listWidget = ImageFileListWidget(self.groupBox_3)
		self.listWidget.setGeometry(QtCore.QRect(10, 20, 361, 511))
		self.listWidget.setObjectName("listWidget")
		self.listWidget.Setup()
		self.connect(self.btnOutput, QtCore.SIGNAL('clicked()'),self.OutputBtn)
		self.connect(self.btnDel, QtCore.SIGNAL('clicked()'),self.DelBtn)
		self.connect(self.btnClear, QtCore.SIGNAL('clicked()'),self.ClearBtn)
		self.connect(self.previewBtn, QtCore.SIGNAL('clicked()'),self.PreviewBtn)
		self.connect(self.sortBtn, QtCore.SIGNAL('clicked()'),self.SortBtn)
		
	def ImageMerge(self,bigWidth,bigHeight,tileX,tileY,readFileList):
		newImage=Image.new('RGBA',(bigWidth,bigHeight))
		localWidth=bigWidth/tileX
		localHeight=bigHeight/tileY
		x=0
		y=0
		for curFile in readFileList:
			img=Image.open(curFile)
			img=img.resize((localWidth,localHeight))
			newImage.paste(img,(x,y))
			
			x+=localWidth
			if x>=bigWidth - localWidth/2:
				x=0
				y+=localHeight
		return newImage
		
	def GetNewImage(self):
		resX=self.resX.value()
		resY=self.resY.value()
		tileX=self.tileX.value()
		tileY=self.tileY.value()
		itemCount=self.listWidget.count()
		readFileList=[]
		for i in range(0,itemCount,1):
			readFileList.append(self.listWidget.item(i).text())
			
		imageCount=tileX*tileY
		if len(readFileList) > imageCount:
			readFileList=readFileList[:imageCount]
			
		return self.ImageMerge(resX,resY,tileX,tileY,readFileList)
		
	def OutputBtn(self):
		print "OutputBtn"
		outputFile=self.outputPath.text()
		if outputFile is None or len(outputFile) == 0:
			print "output file is empty!"
			return
			
		newImage=self.GetNewImage()
		newImage.save(outputFile)
		
	def PreviewBtn(self):
		print "PreviewBtn"
		newImage=self.GetNewImage()
		resX,resY=newImage.size
		pixmap=pil2pixmap(newImage)
		rect=self.labelPreview.frameRect()
		if resX >= resY :
			pixmap=pixmap.scaledToWidth(rect.width())
		else:
			pixmap=pixmap.scaledToHeight(rect.height())
			
		self.labelPreview.setPixmap(pixmap)
		
	def SortBtn(self):
		if self.listWidget.sortOrder == 0:
			self.listWidget.sortItems(QtCore.Qt.DescendingOrder)
			self.listWidget.sortOrder=1
		else:
			self.listWidget.sortItems(QtCore.Qt.AscendingOrder)
			self.listWidget.sortOrder=0
		
	def ClearBtn(self):
		print "ClearBtn"
		self.listWidget.clear()
		
	def DelBtn(self):
		print "DelBtn"
		self.listWidget.takeItem(self.listWidget.currentRow())
	
if __name__=="__main__":
    DS_APP = QtGui.QApplication(sys.argv)
    DS_Widget = ImagePuzzle()
    DS_Widget.show()
    sys.exit(DS_APP.exec_())