
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
		FILENAME = '/home/pi/project/ryu.jpg'
		self.canvas = tk.Canvas(master, width=800, height=600)
		self.canvas.pack()
		tk_img = ImageTk.PhotoImage(file = FILENAME)
		self.canvas.image = tk_img
		self.item = self.canvas.create_image(320, 300, image=tk_img)
		self.igm = PhotoImage(file="/home/pi/project/start.png")
		master.image = self.igm;
		self.item2 = self.canvas.create_image(400,300, image = self.igm, anchor='s')

		#self.start_button = tk.Button(master, image=self.igm, command = self.choose_combo, anchor = 'nw',
                	#width = 175, activebackground = "#33B5E5")
		#self.start_button_window = self.canvas.create_window(450, 250, anchor='center', window=self.start_button)
	

		#self.start_button.destroy()


	def choose_combo(self):
       		
 		 self.canvas.delete(self.item2)
		 
		# self.start_button.destroy(); 
		
		 FILENAME = "/home/pi/project/choose.png"
        	 tk_img2= ImageTk.PhotoImage(file = FILENAME)
		 self.image=tk_img2
        	 self.item = self.canvas.create_image(200,50, image = tk_img2, anchor='n')

        	 igm2 = PhotoImage(file='/home/pi/project/menu.gif')
        	 root.image=igm2
		 #item = self.canvas.create_image(70,10, image = igm2, anchor='n')
        	 Menu_btn = tk.Button(root,text="Menu", command = self.create_dialog, anchor = 'w',
                        width =10, activebackground = "#33B5E5")
        	 menu_button_window = self.canvas.create_window(10,10,anchor='nw', window= Menu_btn)

		 FILENAME = "/home/pi/project/bread+butter2.png"
                 tk_img3= ImageTk.PhotoImage(file = FILENAME)
                 self.image=tk_img3
		 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
		#			width = 600, activebackground = "#33B5E5")
		# self.combo_buttonindow = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)	
                 self.item3 = self.canvas.create_image(80,120, image = tk_img3, anchor='w')

		 FILENAME = "/home/pi/project/cr lp.png"
                 tk_img4= ImageTk.PhotoImage(file = FILENAME)
                 self.image2=tk_img4
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                 self.item4 = self.canvas.create_image(150,350, image = tk_img4, anchor='s')

		 FILENAME = "/home/pi/project/sl lp.png"
                 tk_img5= ImageTk.PhotoImage(file = FILENAME)
                 self.image3=tk_img5
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                 self.item5 = self.canvas.create_image(150,450, image = tk_img5, anchor='s')
		

		 #func_uart.readlineCR(ser)
	
	def highLight(self):
                self.canvas.delete(self.item4)
		self.canvas.delete(self.item3)
		FILENAME = "/home/pi/project/cr lp2.png"
                tk_img4= ImageTk.PhotoImage(file = FILENAME)
                self.image2=tk_img4
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item4 = self.canvas.create_image(150,350, image = tk_img4, anchor='s')


		self.e = Text(self.canvas,height=2,width=32,state=NORMAL)
                self.e.place(x=120,y=250)
                #self.e.geometry('30x30')
                #self.e.pack(expand=YES)
                #e.delete(0,END)
                self.e.insert(END,"Combo's with: S LP, CR HP, C HK")

		FILENAME = "/home/pi/project/bread+butter.png"
                tk_img5= ImageTk.PhotoImage(file = FILENAME)
                self.image3=tk_img5
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item3 = self.canvas.create_image(80,120, image = tk_img5, anchor='w')

		FILENAME = "/home/pi/project/sl lp.png"
                tk_img6= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img6
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item5 = self.canvas.create_image(150,450, image = tk_img6, anchor='s')
	def highLightCr_mp(self):
		self.canvas.delete(self.item4)
                self.canvas.delete(self.item3)
		self.canvas.delete(self.item3)

		

		FILENAME = "/home/pi/project/bread+butter.png"
                tk_img5= ImageTk.PhotoImage(file = FILENAME)
                self.image3=tk_img5
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item3 = self.canvas.create_image(80,120, image = tk_img5, anchor='w')

		FILENAME = "/home/pi/project/cr lp.png"
                tk_img4= ImageTk.PhotoImage(file = FILENAME)
                self.image2=tk_img4
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item4 = self.canvas.create_image(150,350, image = tk_img4, anchor='s')
		
		self.e = Text(self.canvas,height=2,width=32,state=NORMAL)
                self.e.place(x=310,y=250)
                #self.e.geometry('30x30')
                #self.e.pack(expand=YES)
                #e.delete(0,END)
                self.e.insert(END,"Combo's with LP, CR MP, CR HK")

		FILENAME = "/home/pi/project/sl lp2.png"
                tk_img6= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img6
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item5 = self.canvas.create_image(150,450, image = tk_img6, anchor='s')

	def choice(self):
		self.canvas.delete(self.item4)
                self.canvas.delete(self.item3)
                self.canvas.delete(self.item3)
		self.e.destroy()
                root.update()

		
			
		FILENAME = "/home/pi/project/cr lp2.png"
                tk_img4= ImageTk.PhotoImage(file = FILENAME)
                self.image2=tk_img4
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item4 = self.canvas.create_image(150,350, image = tk_img4, anchor='s')



		FILENAME = "/home/pi/project/sl lp2.png"
                tk_img6= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img6
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item5 = self.canvas.create_image(150,450, image = tk_img6, anchor='s')
		

		FILENAME = "/home/pi/project/bread+butter.png"
                tk_img7= ImageTk.PhotoImage(file = FILENAME)
                self.image5=tk_img7
                 #self.combo_button = tk.Button(root, image=tk_img3, command = self.start_reaction, anchor = 'w',
                #                       width = 600, activebackground = "#33B5E5")
                # self.combo_button_window = self.canvas.create_window(80,120,anchor='w', window= self.combo_button)    
                self.item3 = self.canvas.create_image(80,120, image = tk_img7, anchor='w')
		


	def start_reaction(self):
		self.canvas.delete(self.item3)
		self.canvas.delete(self.item4)
		self.canvas.delete(self.item5)

		
		self.count_down()
		return

	def count_down(self):
		keepTrack= False
		
		global counter
		while counter<=5:
			
			if counter == 0:
                        	self.igm = PhotoImage(file="/home/pi/project/1.png")
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
	def failure(self, words, words2, words3, words4,words5,words6):
		
		FILENAME = "/home/pi/project/fail.png"
               	tk_img6= ImageTk.PhotoImage(file = FILENAME)
               	self.image=tk_img6
                self.item6 = self.canvas.create_image(400,250, image = tk_img6, anchor=CENTER,state=NORMAL)
		#print words
		self.e = Text(self.canvas,height=10,width=30,state=NORMAL)
		self.e.place(x=410,y=280)
		
		if words4 == "Success":
			
			self.e.insert(END,"Link one: " + words2)
			self.e.insert(END,"\nLink two: " + words4)
			self.e.insert(END, "\nTime:  " + words)
			self.e.insert(END, "\nFrames: " + words5);
		elif words2 == "Success":
			self.e.insert(END,"Link one: " + words2)
			self.e.insert(END, "\nLink two: " + words4 )
			self.e.insert(END, "\nTime: " +  words3)
			self.e.insert(END, "\nFrames: " +  words6)
		else:
			self.e.insert(END,"Link one: " + words2)
			self.e.insert(END, "\nTime:  " + words)
                        self.e.insert(END, "\nFrames: " + words5);
			self.e.insert(END,"\nLink two: " + words4)
			self.e.insert(END, "\nTime:" +  words3)
                        self.e.insert(END, "\nFrames:" +  words6)



		root.update()
                time.sleep(5)
		return
	
	def deleteItem(self):
		#self.e.config(state=DISABLED)
		self.e.destroy()
		root.update()
		self.canvas.itemconfig(self.item6, state=HIDDEN)
		root.update()
		time.sleep(2)
		return
 		

	def success(self):

                FILENAME = "/home/pi/project/succ.png"
                tk_img7= ImageTk.PhotoImage(file = FILENAME)
                self.image2=tk_img7
                self.item2 = self.canvas.create_image(400,250, image = tk_img7, anchor=CENTER,state=NORMAL)
                root.update()
                time.sleep(5)
                return

        def deleteSuccess(self):
                self.canvas.itemconfig(self.item2, state=HIDDEN)
                root.update()
                time.sleep(2)
                return

	def block(self, words, words2, words3, words4,words5,words6):

                FILENAME = "/home/pi/project/block.png"
                tk_img6= ImageTk.PhotoImage(file = FILENAME)
                self.image=tk_img6
                self.item6 = self.canvas.create_image(400,250, image = tk_img6, anchor=CENTER,state=NORMAL)
                #print words
                self.e = Text(self.canvas,height=10,width=30,state=NORMAL)
                self.e.place(x=410,y=280)
                #self.e.geometry('30x30')
                #self.e.pack(expand=YES)
                #e.delete(0,END)
                if words4 == "Success":

                        self.e.insert(END,"Link one: " + words2)
                        self.e.insert(END,"\nLink two: " + words4)
                        self.e.insert(END, "\nTime:  " + words)
                        self.e.insert(END, "\nFrames: " + words5);
                elif words2 == "Success":
                        self.e.insert(END,"Link one: " + words2)
                        self.e.insert(END, "\nLink two: " + words4 )
                        self.e.insert(END, "\nTime: " +  words3)
                        self.e.insert(END, "\nFrames: " +  words6)
                else:
                        self.e.insert(END,"Link one: " + words2)
                        self.e.insert(END, "\nTime:  " + words)
                        self.e.insert(END, "\nFrames: " + words5);
                        self.e.insert(END,"\nLink two: " + words4)
                        self.e.insert(END, "\nTime: " +  words3)
                        self.e.insert(END, "\nFrames: " +  words6)



                root.update()
                time.sleep(5)
                return
	
	def deleteBlock(self):
                #self.e.config(state=DISABLED)
                self.e.destroy()
                root.update()
                self.canvas.itemconfig(self.item6, state=HIDDEN)
                root.update()
                time.sleep(2)
                return


	def try_again(self):
		FILENAME = "/home/pi/project/try.png"
                tk_img7= ImageTk.PhotoImage(file = FILENAME)
                self.image2=tk_img7
                self.item2 = self.canvas.create_image(400,250, image = tk_img7, anchor=CENTER,state=NORMAL)
                root.update()
		
		FILENAME = "/home/pi/project/yes2.png"
                tk_img8= ImageTk.PhotoImage(file = FILENAME)
                self.image3=tk_img8
                self.item3 = self.canvas.create_image(300,300, image = tk_img8, anchor=CENTER,state=NORMAL)
                root.update()

	
		FILENAME = "/home/pi/project/no.png"
                tk_img9= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img9
                self.item4 = self.canvas.create_image(450,300, image = tk_img9, anchor=CENTER,state=NORMAL)
                root.update()

		time.sleep(2)
		return

	def try_button(self):
                self.canvas.delete(self.item4)
		
		self.canvas.delete(self.item3)

		FILENAME = "/home/pi/project/no2.png"
                tk_img9= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img9
                self.item4 = self.canvas.create_image(450,300, image = tk_img9, anchor=CENTER,state=NORMAL)
                root.update()
		
		
		FILENAME = "/home/pi/project/yes.png"
                tk_img8= ImageTk.PhotoImage(file = FILENAME)
                self.image3=tk_img8
                self.item3 = self.canvas.create_image(300,300, image = tk_img8, anchor=CENTER,state=NORMAL)
                root.update()

	def deleteTry(self):
		
		self.canvas.delete(self.item2)
		self.canvas.delete(self.item4)
		self.canvas.delete(self.item3)
		root.update()
		return


		
						

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
	
	def stats(self,list):
		
		self.canvas.delete(self.item2)
                self.canvas.delete(self.item4)
                self.canvas.delete(self.item3)
                root.update()

		FILENAME = "/home/pi/project/ms.png"
                tk_img9= ImageTk.PhotoImage(file = FILENAME)
                self.image4=tk_img9
                self.item4 = self.canvas.create_image(450,150, image = tk_img9, anchor='w',state=NORMAL)
              	


                FILENAME = "/home/pi/project/f.png"
                tk_img8= ImageTk.PhotoImage(file = FILENAME)
                self.image3=tk_img8
                self.item3 = self.canvas.create_image(300,150, image = tk_img8, anchor='w',state=NORMAL)
                

		stat = str(list)[1:-1]

                output = stat.split(",")
                print output


		self.e = Text(self.canvas,height=10,width=50,state=NORMAL)
                self.e.place(x=200,y=200)

		self.e.insert(END,"1.   ")
                self.e.insert(END, "    " + output[0])
                self.e.insert(END, "    " + output[4])
                self.e.insert(END, "    " + output[2])
		self.e.insert(END, "    " + output[5])
		self.e.insert(END,"\n2.   ")
                self.e.insert(END, "    " + output[6])
                self.e.insert(END, "    " + output[10])
                self.e.insert(END, "    " + output[8])
                self.e.insert(END, "    " + output[11])
		self.e.insert(END,"\n3.   ")
                self.e.insert(END, "    " + output[12])
                self.e.insert(END, "    " + output[16])
                self.e.insert(END, "    " + output[14])
                self.e.insert(END, "    " + output[17])
		self.e.insert(END,"\n4.   ")
                self.e.insert(END, "    " + output[18])
                self.e.insert(END, "    " + output[22])
                self.e.insert(END, "    " + output[20])
                self.e.insert(END, "    " + output[23])
		self.e.insert(END,"\n5.   ")
                self.e.insert(END, "    " + output[24])
                self.e.insert(END, "    " + output[28])
                self.e.insert(END, "    " + output[26])
                self.e.insert(END, "    " + output[29])


	
		root.update() 


		

		#print list


		#stat = str(list)[1:-1]

		#output = stat.split(",")
		#print len(output)

	def processIncoming(self):
		list = []
		while self.queue.qsize():
			try:
				msg=self.queue.get(0)

				print(msg)

				if msg == 'Start':
					
					self.choose_combo()
				
				elif msg == 'highL':
					self.highLight()
				elif msg == 'choc2':
					self.choice()

				elif msg == 'hicom':
					self.highLightCr_mp()
				
						
				elif msg == 'combo':
					state = 1
					#self.start_reaction()	
					p = subprocess.Popen(['sudo','python','-u','./func_uart.py'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
					self.start_reaction()
					test = 0
					stats = " "
					
					for line in p.stdout.readline():
						#list.append(line)
						#print list
					#print p.stdout.readline()	
					
						#state = False

					
						while True:
						#for line in io.TextIOWrapper(p.stdout,encoding="utf-8"):
							#out = p.stdout.read(12)
							out = p.stdout.readline()
							
							#p.stdout.flush()
							#list.append(out)
							#print list
							if out == 'start\n':
								self.try_again()
							if out == 'button\n':
								#print "getting there"
								self.try_button()
							if out == 'ye\n':
								self.deleteTry()
							if out == 'no\n':
								self.stats(list)
												
							if out ==  '' and p.poll() is not None:							
								break
						
							if out:
								print out
								words = out.split(",")
								#print words[0],words[1],words[2]	
								#list.append(words)
								if words[0] == 'fail':
									state = 2
									time.sleep(0.5)
									#print words[0], words[1]
									break
								elif words[0] == 'succ':
									state = 3
									break
								elif words[0]=='block':
									state = 4
									break
							
						rc = p.poll()
						
						if state==2:
							list.append(words[1])
							list.append(words[2])
							list.append(words[3])
							list.append(words[4])
							list.append(words[5])
							list.append(words[6])
							#print list
							self.failure(words[1],words[2],words[3],words[4],words[5],words[6])
							self.deleteItem()
						elif state == 3:
							#list.append(words[1])
                                                        #list.append(words[2])
                                                        #list.append(words[3])
                                                        #list.append(words[4])
                                                        #list.append(words[5])
                                                        #list.append(words[6])
							#print list
							self.success()
							self.deleteSuccess()
						elif state==4:
							list.append(words[1])
                                                        list.append(words[2])
                                                        list.append(words[3])
                                                        list.append(words[4])
                                                        list.append(words[5])
                                                        list.append(words[6])
							#print list
							self.block(words[1],words[2],words[3],words[4],words[5],words[6])
							self.deleteBlock()

			
						state = 1
					
					#self.try_again()
							#state = True
						#if test==4:
					
							#sys.stdout.write('try again')
							#test = 0 

					#self.try_button = tk.Button(root, text= "try again?", command = self.try_again, anchor = 'w',
                			 #                      width = 15, activebackground = "#33B5E5")
                			#self.try_button_window = self.canvas.create_window(80,120,anchor='w', window= self.try_button)    

						
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
			
			if msg=='combo':
				#time.sleep(0)
				self.running=0
				#self.thread1.sleep()
				#time.sleep(10)
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
			
				
