from tkinter import * 
import random
pontos = [0, 0]	
class Jogo:
	
	
	
	def __init__(self, raiz):
		self.raiz = raiz
		Label(self.raiz, text='Jogo Pedra Papel Tesoura',font=('arial',15,'bold')).grid(row= 1, column=1	,padx=10, pady=10, columnspan=3)
		self.b1 = Button(self.raiz,text='PEDRA',width=10, command= self.pedra, bg='#FFA12D')		
		self.b1.grid(row='2',column=1, padx=10, pady=10, sticky=NSEW)
		self.b2 = Button(self.raiz, text='PAPEL',width=10, command= self.papel, bg='#FFA12D')
		self.b2.grid(row=2, column=2, padx=10, pady=10, sticky=NSEW)
		self.b3 = Button(self.raiz, text='TESOURA',command= self.tesoura,bg='#FFA12D')
		self.b3.grid(row=2, column=3, padx=10, pady=10, sticky=NSEW)
		self.msg = Label(self.raiz, bg='black')
		self.msg.grid(row=3, column=1 , padx=10, pady=10, columnspan=3)
		 
		self.msg2 = Label(self.raiz,text=f'Você:{pontos[0]} X {pontos[1]}:Robo', font=('Arial', 15, 'bold') )
		self.msg2.grid(row=4, column=1 , padx=10, pady=10, columnspan=3)
		

			
	def pedra(self):
		opc = ['pedra', 'papel', 'tesoura' ]
		robo = random.randint(0, 2)
		resu = 'pedra'
		if resu == opc[robo]:
			self.msg['text'] =f'Você empatou!. O robo tambêm colocou {opc[robo]}'
			self.msg['fg'] = '#E6E24A'
			
			
		elif resu == 'pedra' and opc[robo] == 'tesoura':
			self.msg['text']=f'Você ganhou!. O robo colocou {opc[robo]}'
			self.msg['fg'] = '#53FF86'
			self.msg['bg'] = 'black'
			pontos[0] += 1
			self.msg2['text'] = f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
		else:
			self.msg['text'] = f'Você perdeu!. O robo colocou {opc[robo]}'
			self.msg['fg']= '#FF2827'
			pontos[1] += 1
			self.msg2['text'] =f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
		
	
	def papel(self):
		opc = ['pedra', 'papel', 'tesoura' ]
		robo = random.randint(0, 2)
		resu = 'papel'
		if resu == opc[robo]:
			self.msg['text'] = f'Você empatou!. O robo tambêm colocou {opc[robo]}'
			self.msg['fg'] = '#E6E24A'
		elif resu == 'papel' and opc[robo] == 'pedra':
			self.msg['text']=f'Você ganhou!. O robo colocou {opc[robo]}'
			self.msg['fg'] = '#53FF86'
			pontos[0] += 1
			self.msg2['text'] = f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
			
		else:
			self.msg['text'] = f'Você perdeu!. O robo colocou {opc[robo]}'
			self.msg['fg']= '#FF2827'
			pontos[1] += 1
			self.msg2['text'] = f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
		
	def tesoura(self):
		opc = ['pedra', 'papel', 'tesoura' ]
		robo = random.randint(0, 2)
		resu = 'tesoura'
		if resu == opc[robo]:
			self.msg['text'] = f'Você empatou!. O robo tambêm colocou {opc[robo]}'
			self.msg['fg'] = '#E6E24A'
		elif resu == 'tesoura' and opc[robo] == 'papel':
			self.msg['text']=f'Você ganhou!. O robo colocou {opc[robo]}'
			self.msg['fg'] = '#53FF86'
			pontos[0] += 1
			self.msg2['text'] = f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
		else:

			self.msg['text'] = f'Você perdeu!. O robo colocou {opc[robo]}'
			self.msg['fg']= '#FF2827'
			pontos[1] += 1
			self.msg2['text'] = f'Você:{pontos[0]} X {pontos[1]}:Robo'
			
			
			



inst = Tk()
Jogo(inst)
inst.mainloop()