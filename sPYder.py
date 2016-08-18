


import os,sys
import urllib
import scapy
from PyQt4 import QtGui,QtCore, QtWebKit
#import browser

class MainWindow(QtGui.QWidget):
	#number of tabs limit
	i=15
	
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setGeometry(0,0,500,650)
		self.setWindowTitle('Tabbed')
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.resize(800,600)
		self.setMinimumSize(500,650)
		
				
		#tab widget
		tab_widget=QtGui.QTabWidget(self)
		tabs=[]
		p_vertical=[]
		#add tab
		def adder(self):
			if len(tabs)<10:
				tabs.append(tabber())
				p_vertical.append(QtGui.QVBoxLayout(tabs[-1]))
				tab_widget.addTab(tabs[-1],'tab'+str(len(tabs)))
				self.setLayout(vbox)
		
		#remove tab
		def remover(self):
			if len(tabs)>1:
				ind=tab_index()
				tabs.pop(ind)
				p_vertical.pop(ind)
				tab_widget.removeTab(ind)
		
		#tab layout
		def tabber():
			tabcentral=QtGui.QWidget()
			tabframe=QtGui.QFrame(tabcentral)
			tabgrid = QtGui.QVBoxLayout(tabframe)
			tabgrid.setMargin(0)
			tabgrid.setSpacing(0)
			tabmain = QtGui.QHBoxLayout(tabcentral)
			tabmain.setSpacing(0)
			tabmain.setMargin(1)
			#address
			tb_url = QtGui.QLineEdit(tabframe)
			##buttons
			bt_back = QtGui.QPushButton(tabframe)
			bt_ahead = QtGui.QPushButton(tabframe)
			bt_add = QtGui.QPushButton(tabframe)
			bt_rem = QtGui.QPushButton(tabframe)
			bt_go = QtGui.QPushButton(tabframe)
			bt_kill = QtGui.QPushButton(tabframe)
			###button styles and activities
			bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
			bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))
			bt_kill.setIcon(QtGui.QIcon().fromTheme("process-stop"))
			bt_go.setText('Go')
			bt_go.setFixedWidth(50)
			bt_add.setText('+')
			bt_add.setFixedWidth(50)
			bt_add.clicked.connect(adder)
			bt_rem.setText('-')
			bt_rem.setFixedWidth(50)
			bt_rem.clicked.connect(remover)
			address_area=QtGui.QHBoxLayout()
			address_area.addWidget(bt_back)
			address_area.addWidget(bt_ahead)
			address_area.addWidget(tb_url)
			address_area.addWidget(bt_go)			
			address_area.addWidget(bt_add)
			address_area.addWidget(bt_rem)
			address_area.addWidget(bt_kill)
			tabgrid.addLayout(address_area)
			html=QtWebKit.QWebView()
			tabgrid.addWidget(html)
			tabmain.addWidget(tabframe)
			
			#browse
			default_url = "www.google.com"
			def browse():
				"""
				Make a web browse on a specific url and show the page on the
				Webview widget.
				"""
				curl = tb_url.text() if tb_url.text() else default_url
				if not curl[:7]=='http://':
					url='http://'+curl
				html.load(QtCore.QUrl(url))
				html.show()
			
			tabmain.connect(tb_url, QtCore.SIGNAL("returnPressed()"), browse)
			tabmain.connect(bt_go, QtCore.SIGNAL("clicked()"), browse)
			tabmain.connect(bt_back, QtCore.SIGNAL("clicked()"), html.back)
			tabmain.connect(bt_ahead, QtCore.SIGNAL("clicked()"), html.forward)
			tabmain.connect(bt_kill, QtCore.SIGNAL("clicked()"),html.forward)
			
			tb_url.setText(default_url)
			browse()
			return tabcentral
		
        ##within tab
		tabs.append(tabber())
		
		##
		'''tabButton = QtGui.QToolButton(self)
		tabButton.setText('+')
		tab_widget.setCornerWidget(self.tabButton)
		tabButton.clicked.connect(self.adder)
		
		tabs.append(tabButton)'''
		p_vertical.append(QtGui.QVBoxLayout(tabs[-1]))
		tab_widget.addTab(tabs[-1],'tab1')
		#tab_widget.setTabText(0,'working')
				
		#Tab Index
		def tab_index():
			curr=tab_widget.currentIndex()
			return curr
		
		vbox=QtGui.QVBoxLayout()
		vbox.addWidget(tab_widget)
		self.setLayout(vbox)
		
		
	
	#center position the window
	def center(self):
		screen=QtGui.QDesktopWidget.screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
def main():
	app=QtGui.QApplication(sys.argv)
	frame=MainWindow()
	frame.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
