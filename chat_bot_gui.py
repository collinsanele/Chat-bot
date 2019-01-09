#A GUI for my chatbot in tkinter
#collinsanele@gmail.com
import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class BotGui():
	def __init__(self, *args):
		self.window = tk.Tk()
		self.window.configure(bg='black')
		self.bot = ChatBot('Houdini')
		
		
		with open('chatbot.txt') as f:
			conversation = f.readlines()
		self.bot.set_trainer(ListTrainer)
		self.bot.train(conversation)
		
		
		
		
		
		self.banner_font = ('times', 9, 'bold')
		#self.text_font = ('times', 5)
		
		
		self.label_banner = tk.Label(text='My Chat Bot', fg='green', bg= 'black', font=self.banner_font)
		self.label_banner.place(x=260, y=35, in_=self.window)
		
		
		self.label_input =  tk.Label(text='Chat with bot:', bg='black', fg='white')
		self.label_input.place(x=20, y=120, in_=self.window)
		
		
		self.text_input = tk.Text(height='8', width='40')
		self.text_input.place(x=10, y=180, in_=self.window)
		
		
		self.btn_chat = tk.Button(text='Chat',
		bg='green', fg='yellow', command=self.process)
		self.btn_chat.place(x=20, y=480, in_=self.window)
		
		
		self.btn_quit = tk.Button(text='Quit',
		bg='red', fg='yellow', command=self.window.destroy)
		self.btn_quit.place(x=560,  y=480, in_=self.window)
		
		
		
		self.text_display = tk.Text(height='12', width='40')
		self.text_display.place(x=10, y=580, in_=self.window)
		
		
	def process(self, *args):
		try:
			user_input = self.text_input.get('1.0', tk.END)
			reply = self.bot.get_response(user_input)
			self.text_display.delete('1.0', tk.END)
			self.text_display.insert(tk.END, reply)
			self.text_input.delete('1.0', tk.END)
		except:
			talk = 'Please talk to me'
			self.text_display.delete('1.0', tk.END)
			self.text_display.insert(tk.END, talk)

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
app = BotGui()
app.window.mainloop()
	
	














