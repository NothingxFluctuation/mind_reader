#!python3
from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
counter=11
root=Tk()
root.config(bg='#7773ce')
seafom='#a4d3b6'
beet='#1f3658'
nm=StringVar()
#this is the profile set for every student on the harvard and i think it would be easy to make thi
nm.set('Person')
def ask_name():
	root1=Tk()
	root1.withdraw()
	name=simpledialog.askstring('Person\'s Name','Enter Your Name Here: ')
	global nm
	nm.set(name)
	root1.destroy()
ppl_blv=StringVar()
ppl_blv.set('You are a very trusting person, you believe in people and what they say.You are influenced by your emotions and mostly get hurt.')
dom_in=StringVar()
dom_in.set('You are a very dominant person, who tends to control and lead in a group.')
artis=StringVar()
artis.set('You are an artist kind of person who has interest in the art world.You like paintings, cartoons and other art stuff.You enjoy theoretical discussions as well as next person.')
ambit_in=StringVar()
ambit_in.set('You are an ambitious person. Your career and success are both high on your priority.')
 
def profile():
	root2=Tk()
	root2.title('Profile')
	root2.config(bg='#4282b0')
	frame=Frame(root2)
	frame1=Frame(root2)
	frame1.config(bg=beet)
	lbl=Label(frame,text='Personality Data',fg=seafom,bg='#4169E1',font='times 25 bold',anchor=W,width=45)
	lbl.pack(side='left',fill=X,expand=True)
	name=Label(frame1,text='Personality Test Report:  '+str(nm.get()),fg='black',bg='#4169E1',font='times 22 bold')
	name.pack(side='top',fill=X)
	faith=Label(frame1,text='People and Emotions',fg=seafom,bg=beet,font='times 20 bold',anchor=W)
	faith.pack(side='top',fill=X)
	faith_label=Message(frame1,text=str(ppl_blv.get()),fg='#4282b0',bg=beet,font='times 14 bold')
	faith_label.pack(side='left',fill=X)
	domin=Label(frame1,text='Dominance',fg=seafom,bg=beet,font='times 20 bold',anchor=W)
	domin.pack(side='top',fill=X)
	domin_label=Message(frame1,text=str(dom_in.get()),fg='#4282b0',bg=beet,font='times 14 bold')
	domin_label.pack(side='left',fill=X)
	art=Label(frame1,text='Artistic',fg=seafom,bg=beet,font='times 20 bold',anchor=W)
	art.pack(side='top',fill=X)
	art_label=Message(frame1,text=str(artis.get()),fg='#4282b0',bg=beet,font='times 14 bold')
	art_label.pack(side='left',fill=X)
	ambit=Label(frame1,text='Ambitious',fg=seafom,bg=beet,font='times 20 bold',anchor=W)
	ambit.pack(side='top',fill=X)
	ambit_label=Message(frame1,text=str(ambit_in.get()),fg='#4282b0',bg=beet,font='times 14 bold')
	ambit_label.pack(side='left',fill=X)
	frame.pack(side='top',fill=X)
	frame1.pack(side='top',fill=X)
	root2.mainloop
def main():
	root3=Tk()
	root3.withdraw()
	q1=tkinter.messagebox.askyesno('Q1','You Value Justice Higher Than Mercy?')
	q2=tkinter.messagebox.askyesno('Q2','You Like Reason Than Feelings?')
	q3=tkinter.messagebox.askyesno('Q3','You Get Bored if you have to read Theoretical Books?')
	q4=tkinter.messagebox.askyesno('Q4','You Believe in Magic and Other Supernatural things?')
	q5=tkinter.messagebox.askyesno('Q5','Your Actions are Frequently Influenced by Other People?')
	q6=tkinter.messagebox.askyesno('Q6','For you, Money is more important than Emotions?')
	q7=tkinter.messagebox.askyesno('Q7','You Find it difficult to talk about your feelings?')
	q8=tkinter.messagebox.askyesno('Q8','You usually Plan Your actions in advance?')
	q9=tkinter.messagebox.askyesno('Q9','You prefer to isolate yourself from outside noises?')
	q10=tkinter.messagebox.askyesno('Q10','You like Talking in Code (e.g. WTF,BTW,ILU) ?')
	tkinter.messagebox.showinfo('Test End','Test is Complete.')
	global ppl_blv,adapt_in,dom_in,artis,intlct_in,ambit_in		
	if q1==True and q2==True:
		ppl_blv.set('You don\'t believe in people. You just don\'t trust others more than you.You keep your emotions under a tight grip and will never let them interfere in decision making.')
	else:
		pass
	if q7==True and q5==True:
		dom_in.set('You are a submissive kind of person, who wants to be controlled and cared by others.')
	else:
		pass
	if q10==True and q8==True:
		artis.set('You are not an artist kind of person, you want everything straight. You like chemistry. You think irrationally and believe what others say.  ')
	else:
		pass
	if q2==False and q6==False:
		ambit_in.set('You have limited ambitions. You want to enjoy life and wait until life brings something good for you.')
	root3.destroy()
	profile()
def counter_label(label):
	def count():
		global counter
		counter-=1
		label.config(text='The Test Session will start in '+str(counter)+' seconds.')
		label.after(1000,count)
		if counter<=0:
			root.destroy()
			ask_name()
			if nm.get()!='':
				main()
			else:
				root4=Tk()
				root4.withdraw()
				tkinter.messagebox.showerror('Empty Error','You haven\'t typed anything.')
	count()
root.title('Q&A')
label=Label(root,fg='black',bg='#7773ce',font='times 25 bold')
label.pack()
if nm.get()!='':
	counter_label(label)
root.mainloop()	
