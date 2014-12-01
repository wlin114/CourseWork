from __future__ import division
from math import log10
a = open("hw2dataset_100.txt")
b = []
for x in a:
	if len(x) == 7:
		b.append((x[0], x[2], x[4]))

counter, improvement = 1, float('inf')

#P(G | W, H)
g_00, g_01, g_10, g_11 = [0.9158878505], [0.6666666667], [0.6447368421], [0.25]

#P(G), P(W | G), P(H | G)
p_male ,p_wm, p_hm, p_wf, p_hf = 0.7, 0.8, 0.7, 0.4, 0.3	

while(improvement > 0.001):
	print counter

	#Counters
	#male: number of male
	#w_male: number of (weight, gender | weight)
	#h_male: same to above
	male, w_male, w_female, h_male, h_female = 0, 0, 0, 0, 0
	for i in b:
		if i[0] == '0':
			male += 1
			if i[1] == '0':
				w_male += 1
			if i[2] == '0':
				h_male += 1
		elif i[0] == '1':
			if i[1] == '0':
				w_female += 1
			if i[2] == '0':
				h_female += 1
		else:
			if i[1] == '0':
				if i[2] == '0':
					#When gender is missing, weight and height are 0
					#male is increased by P(G=0 | W=0, H=0)
					male += g_00[-1]
					#w_male is P(W,G | W)
					w_male += (p_wm * p_male) / ((p_wm * p_male) + (p_wf * (1-p_male)))
					h_male += (p_hm * p_male) / ((p_hm * p_male) + (p_hf * (1-p_male)))
					w_female += (p_wf * (1-p_male)) / (p_wf * (1-p_male) + p_wm * p_male)
					h_female += (p_hf * (1-p_male)) / (p_hf * (1-p_male) + p_hm * p_male)

				else:
					male += g_01[-1]
					w_male += p_wm * p_male
					w_female += p_wf * (1 - p_male)
			else:
				if i[2] == '0':
					male += g_10[-1]
					h_male += p_hm * p_male
					h_female += p_hf * (1-p_male)
				else:
					male += g_11[-1]

	female = 200 - male
	print  male, female, w_male, h_male, w_female, h_female

	#updating for following probs:
	p_male = male/(200)
	p_wm = w_male/(male)
	p_wf = w_female/(female)
	p_hm = h_male/(male)
	p_hf = h_female/(female)

	print p_male, p_wm, p_wf, p_hm, p_hf

	#this log is wrong 
	#improvement = male * log10(p_male) + female * log10(1-p_male) + w_male * log10(p_wm) + w_male * log10(1-p_male) + w_female * log10(p_wf) + w_female * log10(1-p_wf) + h_male * log10(p_hm) + h_male * log10(1- p_hm) + h_female* log10(p_hf) + h_female * log10(1-p_hf)

	#updating for following probs
	g_00_temp = (p_male * p_wm * p_hm )/((p_male * p_wm * p_hm )+((1 - p_male ) * p_wf * p_hf ))

	g_01_temp = (p_male * p_wm * ( 1 - p_hm ))/((p_male * p_wm * ( 1 - p_hm )) +((1 - p_male) * p_wf * (1 - p_hf)))

	g_10_temp = (p_male * (1 - p_wm) * p_hm )/((p_male * (1 - p_wm) * p_hm )+((1 - p_male) * (1 - p_wf) * p_hf))

	g_11_temp = (p_male * (1 - p_wm) * (1 - p_hm))/(p_male * (1 - p_wm) * (1 - p_hm)+((1 - p_male) * (1 - p_wf) * (1 - p_hf)))


	print "P00: ",g_00_temp
	print "P01: ",g_01_temp
	print "P10: ",g_10_temp
	print "P11: ",g_11_temp
	
	print "P(Male): ", p_male
	print "P(W|M): ", p_wm
	print "P(W|F): ", p_wf
	print "P(H|M): ", p_hm
	print "P(H|F): ", p_hf
	print "P(G|H,F)", g_00_temp

	counter+=1

	#max differences between previous g_xx to current g_xx
	improvement = max( abs(g_00[-1] - g_00_temp), abs(g_01[-1] - g_01_temp ), abs(g_10[-1] - g_10_temp), abs(g_11[-1] - g_11_temp) )
	
	#add current g_xx to g_xx list
	g_00.append(g_00_temp)
	g_01.append(g_01_temp)
	g_10.append(g_10_temp)
	g_11.append(g_11_temp)

	print improvement

	#iteration limit check
	if(counter > 100):
		break