import threading
import time
from Tkinter import *
import Tkinter
import Tkinter as tk
from PIL import Image, ImageTk
import random
import Queue
import serial

 
class GuiPart:
	def __init__(self, master, queue, endCommand):
		global start_button
		self.queue = queue
		#console = Tkinter.Button(master, text='done',command=endCommand)	
		#console.pack()
		FILENAME = '/home/pi/project/Abel.png'
		self.canvas = tk.Canvas(master, width=800, height=600)
		self.canvas.pack()
		tk_img = ImageTk.PhotoImage(file = FILENAME)
		self.canvas.image = tk_img
		item = self.canvas.create_image(125, 125, image=tk_img)
		igm = PhotoImage(file="/home/pi/project/Start.gif")
		master.image = igm;
		#item = self.canvas.create_image(400,300, image = igm, anchor='s')

		self.start_button = tk.Button(master, image=igm, command = self.choose_combo, anchor = 'nw',
                	width = 175, activebackground = "#33B5E5")
		self.start_button_window = self.canvas.create_window(450, 250, anchor='center', window=self.start_button)
		#self.start_button.destroy()

	def choose_combo(self):
       		 global item
		 self.start_button.destroy()

		 FILENAME = "/home/pi/project/choose_combo.gif"
        	 tk_img2= ImageTk.PhotoImage(file = FILENAME)
		 self.image=tk_img2
        	 item = self.canvas.create_image(200,50, image = tk_img2, anchor='n')

        	 igm2 = PhotoImage(file='/home/pi/project/menu.gif')
        	 root.image=igm2
		 #item = self.canvas.create_image(70,10, image = igm2, anchor='n')
        	 Menu_btn = tk.Button(root,text="Menu", command = self.create_dialog, anchor = 'w',
                        width =10, activebackground = "#33B5E5")
        	 menu_button_window = self.canvas.create_window(10,10,anchor='nw', window= Menu_btn)

	def create_dialog(self):
		
		FILENAME = "/home/pi/project/chun.png"
		window2 = tk.Toplevel(root)
		canvas = tk.Canvas(window2,width=300, height =200)
		canvas.pack()
		
		tk_img =ImageTk.PhotoImage(file=FILENAME)
		canvas.image = tk_img
		item=canvas.create_image(125,115, image=tk_img)
		
		igm4 = PhotoImage(file="/home/pi/project/quit.gif")
		window2.image= igm4
		quit_button = tk.Button(window2,image=igm4,command = self.quit, anchor = 'nw',
				width =75,activebackground = "#33B5E5")
		quit_button_window= canvas.create_window(20,20,anchor= 'w', window= quit_button)

	def quit(self):
		import sys
		sys.exit()	



	def processIncoming(self):
		while self.queue.qsize():
			try:
				msg=self.queue.get(0)
				print(msg)	
			except Queue.Empty:
				pass


class ThreadedClient:
	def __init__(self,master):
		self.master = master
		self.queue = Queue.Queue()
		self.gui = GuiPart(master,self.queue, self.endApplication)

		self.running =1
		self.thread1 = threading.Thread(target=self.workerThread1)	
		self.thread1.start()

		self.periodicCall()
	def periodicCall(self):
		self.gui.processIncoming()
		if not self.running:
			import sys
			sys.exit()
		self.master.after(200,self.periodicCall)

	def workerThread1(self):
		while self.running:
			time.sleep(rand.random()*1.5)
			ser = serial.Serial("/dev/ttyAMA0")
			ser.baudrate =9600
			msg=ser.read(1) 
			#msg = rand.random()
			self.queue.put(msg)
	def endApplication(self):
		self.running =0
	
		


rand = random.Random()
root=Tkinter.Tk()
client = ThreadedClient(root)
root.mainloop()
			
				
