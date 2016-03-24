
import subprocess
import threading
import time
#import func_uart
from Tkinter import *
import Tkinter
import Tkinter as tk
from PIL import Image, ImageTk
import random
import Queue
import serial
import MySQLdb
 
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
		self.item = self.canvas.create_image(125, 125, image=tk_img)
		self.igm = PhotoImage(file="/home/pi/project/Start.gif")
		master.image = self.igm;
		self.item2 = self.canvas.create_image(400,300, image = self.igm, anchor='s')

		#self.start_button = tk.Button(master, image=self.igm, command = self.choose_combo, anchor = 'nw',
                #	width = 175, activebackground = "#33B5E5")
		#self.start_button_window = self.canvas.create_window(450, 250, anchor='center', window=self.start_button)
		#self.start_button.destroy()

	def choose_combo(self):
       		
 		 self.canvas.delete(self.item2)
		 
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

		 FILENAME = "/home/pi/project/combo1.gif"
                 tk_img3= ImageTk.PhotoImage(file = FILENAME)
                 self.image=tk_img3
		# self.combo_button = tk.Button(root, image=tk_img3, command = self.cr_mp_cr_hp, anchor = 'w',
		#			width = 400, activebackground = "#33B5E5")
		# self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)	
                 self.item3 = self.canvas.create_image(80,120, image = tk_img3, anchor='w')
		 #func_uart.readlineCR(ser)

	def start_reaction(self):
		self.canvas.delete(self.item3)	

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



	def processIncoming(self):
		while self.queue.qsize():
			try:
				msg=self.queue.get(0)
				print(msg)
				if msg == 'Start':
					#print msg
					#execfile("func_uart.py")  
					self.choose_combo()
					#func_uart.readlineCR()
				elif msg == 'Combo':
					#subprocess.call(['sudo','/home/pi/project/func_uart.py'])
					#subprocess.call("./func_uart.py",shell=True)
					subprocess.Popen(['sudo','python','./func_uart.py'])
					self.start_reaction()
					#func_uart.readlineCR(ser)
					#print "poop"
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
			ser = serial.Serial(port = "/dev/ttyAMA0",
					    baudrate = 9600,
					    parity = serial.PARITY_NONE,
				            stopbits = serial.STOPBITS_ONE,
					    bytesize = serial.EIGHTBITS,
					    timeout = 1)
			msg=ser.read(5)
			ser.flushInput()
			#if msg == "okgou":
			#	print "hi"
			#	if __name__ == '__main__':

					#func_uart.readlineCR(ser)
				#self.choose_combo()

				#execfile("func_uart.py")   
			#msg = rand.random()
			self.queue.put(msg)
			#ser.write('ok')
	def endApplication(self):
		self.running =0
	

	
					

rand = random.Random()
root=Tkinter.Tk()
client = ThreadedClient(root)
root.mainloop()
			
				
