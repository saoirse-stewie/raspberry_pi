
import subprocess
import os
from subprocess import PIPE, STDOUT, Popen
from itertools import count 
import threading
import time
from time import sleep
#import func_uart
from Tkinter import *
import Tkinter
import Tkinter as tk
from PIL import Image, ImageTk
import random
import Queue
import serial
import MySQLdb

counter =0
 
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
                	#width = 175, activebackground = "#33B5E5")
		#self.start_button_window = self.canvas.create_window(450, 250, anchor='center', window=self.start_button)
		#self.start_button.destroy()

	def choose_combo(self):
       		
 		# self.canvas.delete(self.item2)
		 self.start_button.destroy(); 
		
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
		 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
		#			width = 600, activebackground = "#33B5E5")
		# self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)	
                 self.item3 = self.canvas.create_image(80,120, image = tk_img3, anchor='w')
		 #func_uart.readlineCR(ser)

	def start_reaction(self):
		#self.canvas.delete(self.item3)
		self.combo_button.destroy()
		
		self.count_down()

	def count_down(self):
		keepTrack= False
		
		global counter
		while counter<=5:
			
			if counter == 0:
                        	self.igm = PhotoImage(file="/home/pi/project/6.png")
                        	self.image = self.igm;
                        	self.item2 = self.canvas.create_image(400,250, image = self.image, anchor=CENTER)

			root.update()
			time.sleep(1)
			counter+=1
			if counter == 1:
				self.canvas.delete(self.item2)
				FILENAME = "/home/pi/project/2.png"
                		tk_img3= ImageTk.PhotoImage(file = FILENAME)
                 		self.image=tk_img3
				self.item3 = self.canvas.create_image(400,250, image = tk_img3, anchor=CENTER)
			elif counter ==2:
				self.canvas.delete(self.item3)
                                FILENAME = "/home/pi/project/3.png"
                                tk_img4= ImageTk.PhotoImage(file = FILENAME)
                                self.image=tk_img4
                                self.item4 = self.canvas.create_image(400,250, image = tk_img4, anchor=CENTER)
			elif counter ==3:
                                self.canvas.delete(self.item4)
                                FILENAME = "/home/pi/project/4.png"
                                tk_img5= ImageTk.PhotoImage(file = FILENAME)
                                self.image=tk_img5
                                self.item5 = self.canvas.create_image(400,250, image = tk_img5, anchor=CENTER)
			elif counter ==4:
                                self.canvas.delete(self.item5)
                                FILENAME = "/home/pi/project/5.png"
                                tk_img6= ImageTk.PhotoImage(file = FILENAME)
                                self.image=tk_img6
                                self.item6 = self.canvas.create_image(400,250, image = tk_img6, anchor=CENTER)
			else:	
				self.canvas.delete(self.item6)
	
				
		counter  = count()
						

	def create_dialog(self):
		
		FILENAME = "/home/pi/project/chun.png" #TODO change picture, looks shit
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
					
					self.choose_combo()
					
				elif msg == 'Combo':
					p = subprocess.Popen(['sudo','python','./func_uart.py'], stdout=subprocess.PIPE, stderr= subprocess.PIPE)
					while True:
						out = p.stdout.read(4)
						
						if out ==  '' and p.poll() is not None:
							break
						
						if out:
							print out
					#print "received: %s" % p.stdout.readline()
					#	s = []
					#	s = p.stdout.readline()

					#	print s
						
					#	words = p.stdout.readline().split()
						#print words[0]

						#if s == "fail[' ']" or s=="fail":
						#	print "poop"
						
  
					#self.start_reaction()
				#elif msg == 'FAIL':
					#print "poop"
					#func_uart.readlineCR(ser)
					#print "poop"
				#elif msg == 'FAIL':
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
			#if msg=='FAIL':
				#print "poop"

			#if msg == "FAILURE":
				#print "you suck"
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
			
				
