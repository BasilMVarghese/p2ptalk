import sys, traceback, Ice
from Receiver_ui_demo import *
sys.path.append("..")
import data
class sendfileI(data.sendfile):
	def sendstringfile(self,data,filename):
		self.ReceivedData=[]
		self.ReceivedData.append(data)
		self.ReceivedData.append(filename)
		print "datareceived"
		return True
class window(Ui_MainWindow):
	def setupUi(self,QMainWindow):
		Ui_MainWindow.setupUi(self,QMainWindow)
		self.SetUserNameButton.clicked.connect(self.setUserName)
		self.setUpConnection()
	def setUpConnection(self):
		self.Connetionstatus = 0
		self.ic = None
		try:
		    self.ic = Ice.initialize(sys.argv)
		    self.adapter = self.ic.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
		    self.object = sendfileI()
		    self.adapter.add(self.object,self.ic.stringToIdentity("SimplePrinter"))
		    self.adapter.activate()
		    #self.ic.waitForShutdown() 	
		except:
		    traceback.print_exc()
		    status = 1
 	
	def setUserName(self):
		self.UserNamestring=self.UserName.text()
		self.Status.append("New UserName:: "+self.UserNamestring)
if __name__=='__main__': 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
