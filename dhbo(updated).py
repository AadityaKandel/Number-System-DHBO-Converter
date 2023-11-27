import tkinter.messagebox as tmsg
from tkinter import *
import math

# Import Complete

root = Tk()

# root.geometry('600x500')
root.minsize(900,500)
# root.maxsize(600,500)
root.title('Python Project')

# Creating Variable
value = IntVar()
dhbo1 = StringVar()
dhbo2 = StringVar()
val = StringVar()

powers = ['\u2070', '\u00B9', '\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
text1=""
power_in_use = []
bases = ['\u2082', '\u2088', '\u2081\u2080', '\u2081\u2086'] #2,8,10,16
base_in_use = ''
sec_base_in_use = ''
answer_text = ''
h_o_conversion = ''

hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
binary = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
octal = ['0','1','2','3','4','5','6','7']
bits=0
binary_for_octal = ['000','001','010','011','100','101','110','111']
octal_not = ['8','9']
binary_not = ['2','3','4','5','6','7','8','9']
hex_or_oct=None
errorlevel=0

# Setting Variables
value.set(110011)
val.set('6F')
dhbo1.set('B1')
dhbo2.set('D2')

# Creating Functions
def frm():
	frame = Frame(borderwidth=10,bg="white")
	return frame

def tick(frame_name,text,valuee):
	checkbutton = Radiobutton(frame_name,text=text,bg="white",fg="black",font="Arial 10 bold",value=valuee)
	if valuee[-1] == "2":
		checkbutton.config(variable=dhbo2)
	else:
		checkbutton.config(variable=dhbo1)
	checkbutton.pack()
	return checkbutton

def empty():
	Label(text="",bg="white").pack()

def identify():
	global value,hex_or_oct,val,errorlevel
	errorlevel=0
	if dhbo1.get() == "D1":
		if dhbo2.get() == "B2":
			base_checker(10,2)
			division(value.get(),10,2)
		elif dhbo2.get() == "H2":
			base_checker(10,16)
			division(value.get(),10,16)
		elif dhbo2.get() == "O2":
			base_checker(10,8)
			division(value.get(),10,8)

	elif dhbo1.get() == "B1":
		for x in binary_not:
			if x in str(value.get()):
				errorlevel+=1
			else:
				pass
		if errorlevel>0:
			tmsg.showerror('Error',"Binary only supports 1's and 0's")
		else:
			if dhbo2.get() == "D2":
				base_checker(2,10)
				multiply(value.get(),2,10)
			elif dhbo2.get() == "H2":
				base_checker(2,16)
				similarity(value.get(),2,16)
			elif dhbo2.get() == "O2":
				base_checker(2,8)
				similarity(value.get(),2,8)

	elif dhbo1.get() == "H1":
		if dhbo2.get() == "B2":
			hex_or_oct = "hex"
			base_checker(16,2)
			hex_or_oct = "hex"
			value2 = bin(int(val.get(), 16))[2:]
			similarity(value2,16,2)
		elif dhbo2.get() == "D2":
			base_checker(16,10)
			multiply(val.get(),16,10)
		elif dhbo2.get() == "O2":
			base_checker(16,10)
			multiply(val.get(),16,10)

	elif dhbo1.get() == "O1":
		for x in octal_not:
			if x in str(value.get()):
				errorlevel+=1
			else:
				pass
		if errorlevel>0:
			tmsg.showerror('Error',"Octal only supports number from 0 to 7")
		else:
			if dhbo2.get() == "D2":
				base_checker(8,10)
				multiply(value.get(),8,10)
			elif dhbo2.get() == "B2":
				hex_or_oct="oct"
				base_checker(8,2)
				hex_or_oct = "oct"
				val = str(value.get())
				value2 = bin(int(val, 8))[2:]
				similarity(value2,8,2)
			elif dhbo2.get() == "H2":
				base_checker(8,10)
				multiply(value.get(),8,10)

	else:
		tmsg.showerror('Error','Invalid Options Selected')

def multiply(v,b,s_b):
	global power_in_use,powers,text1,base_in_use,bases,answer_text,sec_base_in_use,h_o_conversion

	v1 = list(str(v))
	v1_for_hexa = v1
	v_for_hexa = []

	if b==16 and s_b == 10:
		for x in v1:
			v_for_hexa.append(hexadecimal.index(str(x)))
		v1 = v_for_hexa
	else:
		v1 = [int(digit) for digit in str(v)]

	b1 = []
	show_power(len(v1))

	b1 = []
	b2 = []
	b3 = []
	p1 = []
	t1 = []
	f1 = 0

	for i in range(len(v1)):
		b1.append(b)
		b2.append(b1[0+i]**i)

	str_b1 = []
	str_b1 = [str(x) for x in b1]
	str_v1 = []
	str_v1 = [str(y) for y in v1]
	base_and_power = []
	first_step = []
	second_step = []


	for i in range(len(b2)):
		b3.append(b2[-1-i])
		p1.append(power_in_use[-1-i])

	str_b3 = []
	str_b3 = [str(z) for z in b3]
	
	for i in range(len(b2)):
		base_and_power.append(str_b1[i]+p1[i])

	for i in range(len(b2)):
		first_step.append(str_v1[i]+'x'+base_and_power[i])
		second_step.append(str_v1[i]+'x'+str_b3[i])

	for i in range(len(b2)):
		t1.append(v1[i]*b3[i])

	third_step = []
	third_step = [str(a) for a in t1]

	for i in range(len(b2)):
		f1 = f1+t1[i]

	if b == 16 and s_b == 10:
		str_v1 = ''.join(v1_for_hexa)
	else:
		str_v1 = ''.join(str_v1)

	answer_text = f'''
	Given: ({str_v1}){base_in_use} = (?){sec_base_in_use}
	According to question,
		({str_v1}){base_in_use} = {' + '.join(first_step)}
		                    = {' + '.join(second_step)}
		                    = {' + '.join(third_step)}
		                    = {f1}

	Hence, ({str_v1}){base_in_use} = ({f1}){sec_base_in_use}
		'''
	h_text = 'To convert Hexadecimal to Octal, We first need to convert Hexa into Decimal,\n'
	o_text="To convert Octal to Hexadecimal, We first need to convert Octal into Decimal,\n"
	if dhbo1.get()=="O1" and dhbo2.get()=="H2":
		h_o_conversion = o_text+answer_text
		base_checker(10,16)
		division(f1,10,16)
	elif dhbo1.get()=="H1" and dhbo2.get()=="O2":
		h_o_conversion = h_text+answer_text
		base_checker(10,8)
		division(f1,10,8)
	else:
		area.delete(1.0,END)
		area.insert(1.0,answer_text)
	# Important is v1,b1,b3,p1 
	# v1 = [Input], b1 = [Base], b3=[Base (already multiplied)], p1=[Power Decending Order]
	# str_b1 = string [Input], base_and_power = string [both added as string]
	# t1 = Third Step Of Answer (in_int) #third_step = Same Answer (in_string)
	# f1 = Final Step Of Answer (in_int) #final_step = Same Answer (in_string)

def show_power(how_much):
	global power_in_use,powers,text1
	for i in range(how_much):
		if i>=10:
			i1 = list(str(i))
			i1 = [int(digit) for digit in str(i)]
			text1 = ""
			for x in range(len(i1)):
				text = i1[x]
				text1 = text1+powers[text]
			power_in_use.append(text1)
		else:
			power_in_use.append(powers[i])

def base_checker(b,s_b):
	global base_in_use,sec_base_in_use,bits,hex_or_oct
	if b == 2:
		base_in_use = bases[0]
	elif b == 8:
		base_in_use = bases[1]
	elif b == 10:
		base_in_use = bases[2]
	elif b == 16:
		base_in_use = bases[3]

	if s_b == 2:
		sec_base_in_use = bases[0]
		if hex_or_oct == "hex":
			bits=4
		elif hex_or_oct == "oct":
			bits=3
		else:
			pass
	elif s_b == 8:
		sec_base_in_use = bases[1]
		bits=3
	elif s_b == 10:
		sec_base_in_use = bases[2]
	elif s_b == 16:
		sec_base_in_use = bases[3]
		bits=4


def similarity(v,b,s_b):
	global sec_base_in_use,hexadecimal,binary,bits,octal,base_in_use,binary_for_octal,hex_or_oct,value
	# Suppose v = "10101011101" it's hexa answer is 55D
	# b = 2, s_b = 16
	# Dividing the given binary number (v) down_power (2) into groups of 4 bits from right to left.....
	# and appending 0's at leading position, we have the following groups,
	# By Using Table, 
	# Binary Representation:      0101 0101 1101
	# Hexadecimal Representation:   5    5    D
	# Hence, (10101011101) down_power (2) = (55D) down_power 16

	v1 = str(v)
	l1 = len(v1)
	v2 = []
	if l1 % bits != 0:
		while (True):
			if l1 % bits == 0:
				break
			else:
				l1 = l1+1
		l2 = l1-len(v1)
		for i in range(l2):
			v1 = '0'+v1
	else:
		pass
	string = ''
	if bits==4:
		initial = 3
	elif bits==3:
		initial = 2
	for i in range(len(v1)):
		string+=v1[i]
		if i==initial:
			initial=initial+bits
			v2.append(string)
			string=''
		else:
			pass
	answer_list = []
	for i in range(len(v2)):
		if bits==4:
			index = binary.index(v2[i])
			answer_list.append(hexadecimal[index])
		elif bits==3:
			index = binary_for_octal.index(v2[i])
			answer_list.append(octal[index])

	# answer_show = ''

	# for i in range(len(v2)):
	# 	answer_show = answer_show+v2[i]+"=="+answer_list[i]+'\n'

	binary_show = 'Binary Representation:        '+'  '.join(v2)
	if bits==4:
		hexa_show = 'Hexadecimal Representation:  '+'       '.join(answer_list)
	elif bits==3:
		hexa_show = 'Octal Representation:           '+'       '.join(answer_list)

	text_for_hexoct = ''
	if hex_or_oct =="hex" or hex_or_oct == "oct":
		binary_show,hexa_show = hexa_show,binary_show
		answer_list=v2
		if hex_or_oct == "hex":
			v = val.get()
			text_for_hexoct = "1 hex digits"
			bits = 4
			base_in_use = bases[3]
			sec_base_in_use = bases[0]
		elif hex_or_oct == "oct":
			v = value.get()
			text_for_hexoct = "1 octal digits"
			bits = 3
			base_in_use = bases[1]
			sec_base_in_use = bases[0]

		second_text= f'''
	Now, Dividing the given number ({v}){base_in_use} into groups of {text_for_hexoct}
	from right to left and converting each {hex_or_oct} digits to {bits} bits binary, we have the 
	following groups:
		'''
	else:
		second_text= f'''
	Now, Dividing the given number ({v}){base_in_use} into groups of {bits}
	bits from right to left and appending 0's to leading position, we have
	the following groups:
		'''
	first_text = f'''
	Given ({v}){base_in_use} = (?){sec_base_in_use}
	'''
	third_text=f'''
	Using table, 
	{binary_show}
	{hexa_show}

	Hence, ({v}){base_in_use} = ({''.join(answer_list)}){sec_base_in_use}

	'''
	answer_text=first_text+second_text+third_text
	area.delete(1.0,END)
	area.insert(1.0,answer_text)
 
def exception():
	en1.config(textvariable=val)

def non_exception():
	en1.config(textvariable=value)

def division(v,b,s_b):
	# 51 is the value, Suppose
	global base_in_use,sec_base_in_use,h_o_conversion,dhbo1,dhbo2
	v_for_text = v
	reminder = []
	dividend = []
	quotient = []
	div = 0

	inverse_r = []

	while (True):
		if v<=0:
			break
		else:
			pass
		reminder.append(v%s_b)
		dividend.append(v)
		div = v
		if v%s_b ==0:
			quotient.append(v//s_b)
		else:
			quotient.append((div-1)//s_b)
		v=(v-(v%s_b)) // s_b

	for i in range(len(reminder)):
		if s_b == 16:
			inverse_r.append(reminder[-1-i])
		else:
			inverse_r.append(str(reminder[-1-i]))

	text=f"Given, ({v_for_text}){base_in_use} = (?){sec_base_in_use}\nNow,\n"
	for i in range(len(reminder)):
		text+=f"	{dividend[i]} ÷ {s_b} = {quotient[i]} reminder is {reminder[i]}\n"
	if s_b == 16:
		final_answer = ''
		for x in inverse_r:
			final_answer+=f'{hexadecimal[x]}'
		text2 = f"Hence, ({v_for_text}){base_in_use} = ({final_answer}){sec_base_in_use}"
	else:
		text2 = f"Hence, ({v_for_text}){base_in_use} = ({''.join(inverse_r)}){sec_base_in_use}"

	if dhbo1.get()=="O1" and dhbo2.get()=="H2":
		h_o_conversion += '\nAt last, converting Decimal into Hexadecimal,\n'+text+'\n'+text2
		finalization(h_o_conversion)
	elif dhbo1.get()=="H1" and dhbo2.get()=="O2":
		h_o_conversion += '\nAt last, converting Decimal into Octal,\n'+text+'\n'+text2
		finalization(h_o_conversion)
	else:
		area.delete(1.0,END)
		area.insert(1.0,text+'\n'+text2)

def finalization(text):
	area.delete(1.0,END)
	area.insert(1.0,text)


# For converting Octal to Hexa, Convert Octal into Decimal[multiply] and then Decimal[Divide] into Hexa
# For converting Hexa to Octal, Convert Hexa into Decimal [multiply] and then Decimal[Divide] into Octal

# Creating CheckButtons
f1 = frm()
f2 = frm()
f3 = frm()
f4 = frm()

# Frame 1
ch1 = tick(f1,"Decimal","D1")
ch2 = tick(f1,"Binary","B1")

# Frame 2
ch3 = tick(f2,"Hexadecimal","H1")
ch4 = tick(f2,"Octal","O1")

# Middle Label
l1 = Label(text="TO",bg="white",fg="black",font="comicsansms 14 italic",justify=CENTER)

# Frame 3
ch5 = tick(f3,"Decimal","D2")
ch6 = tick(f3,"Binary","B2")

# Frame 4
ch7 = tick(f4,"Hexadecimal","H2")
ch8 = tick(f4,"Octal","O2")

f1.pack(side=LEFT,anchor=N)
f2.pack(side=LEFT,anchor=N)
f3.pack(side=RIGHT,anchor=N)
f4.pack(side=RIGHT,anchor=N)

l1.pack(pady=20)

l2 = Label(root, text="Enter your number below...", bg="white", fg="black", font=("Times New Roman", 14, "italic"), pady=10)
l2.pack()

en1 = Entry(textvariable=value, width=14, font=("Times New Roman", 14, "italic"), bg="white", fg="black")
en1.pack()

empty()

btn = Button(text="Calculate",font=("Times New Roman", 14, "italic"), bg="black", fg="white",command=identify)
btn.pack()

empty()

area = Text(height=20,width=70, wrap=NONE,font=('Times New Roman',14,"bold"))

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=area.yview)

scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM, fill=X)
scrollbar1.config(command=area.xview)

area.pack(fill=BOTH, side=LEFT, expand=True)
area.config(yscrollcommand=scrollbar.set)
area.config(xscrollcommand=scrollbar1.set)

# Exception List
radiobuttons = [ch1,ch2,ch4]
for x in radiobuttons:
	x.config(command=non_exception)

# Configuration
root.config(bg="white")
ch3.config(command=exception)
root.mainloop()
