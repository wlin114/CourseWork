from __future__ import division
from math import log10
a = open("hw2dataset_100.txt")
b = []
for x in a:
	if len(x) == 7:
		b.append((x[0], x[2], x[4]))

counter, improvement, improvement1 = 1, float('inf'), float('inf')
g_00, g_01, g_10, g_11 = [0.9158878505], [0.6666666667], [0.6447368421], [0.25]
p_male ,p_wm, p_hm, p_wf, p_hf = 0.7, 0.8, 0.7, 0.4, 0.3

while(improvement > 0.001):
	print counter
	male, female, w_male, w_female, h_male, h_female = 0, 0, 0, 0, 0, 0
#	w1m, w1f, h1m, h1f = 0,0,0,0 
#	v00, v01, v10, v11 = 0, 0, 0, 0
	weight = 0
	for i in b:
		if i[0] == '0':
			male += 1
			if i[1] == '0':
				w_male += 1
			if i[2] == '0':
				h_male += 1
		elif i[0] == '1':
			female += 1
			if i[1] == '0':
				w_female += 1
			if i[2] == '0':
				h_female += 1
		else:
			if i[1] == '0':
				weight+=1
				if i[2] == '0':
					male += g_00[-1]
#					v00+=1
					female += 1 - g_00[-1]
					w_male += p_wm* p_male
					h_male += p_hm* p_male
					w_female += p_wf * (1-p_male)
					h_female += p_hf * (1-p_male)
				else:
					male += g_01[-1]
#					v01+=1
#					h1m +=1
#					h1f +=1
					female += 1 - g_01[-1]
					w_male += p_wm * p_male
					w_female += p_wf * (1 - p_male)
					#h_male += 1-p_hm
					#h_female += 1-p_hf
			else:
				if i[2] == '0':
					male += g_10[-1]
#					v10+=1
#					w1m+=1
#					w1f+=1
					female += 1 - g_10[-1]
					h_male += p_hm * p_male
					h_female += p_hf *(1-p_male)
					#w_male += 1 - p_wm
					#w_female += 1 - p_wf
				else:
					male += g_11[-1]
#					w1m+=1
#					w1f+=1
#					h1m+=1
#					h1f+=1
#					v11+=1
					#h_male += 1-p_hm
					#h_female += 1-p_hf
					#w_male += 1 - p_wm
					#w_female += 1 - p_wf
					female += 1 - g_11[-1]
	
#	print weight
#	print male, female
	print w_male, h_male, w_female, h_female, male, female
#	print w1m, w1f, h1m, h1f

#	print v00, v01, v10, v11
	p_male = male/(200)
	p_wm = w_male/(male)
	p_wf = w_female/(female)
	p_hm = h_male/(male)
	p_hf = h_female/(female)

	print male, p_male, p_wm, p_wf, p_hm, p_hf

	#imporvement = male * log10(p_male) + female * log10(1-p_male) + w_male * log10(p_wm) + w_male * log10(1-p_male) + w_female * log10(p_wf) + w_female * log10(1-p_wf) + h_male * log10(p_hm) + h_male * log10(1- p_hm) + h_female* log10(p_hf) + h_female * log10(1-p_hf)


	

	g_00_temp = (p_male * p_wm * p_hm )/((p_male * p_wm * p_hm )+((1 - p_male ) * p_wf * p_hf ))

	g_01_temp = (p_male * p_wm * ( 1 - p_hm ))/((p_male * p_wm * ( 1 - p_hm )) +((1 - p_male) * p_wf * (1 - p_hf)))

	g_10_temp = (p_male * (1 - p_wm) * p_hm )/((p_male * (1 - p_wm) * p_hm )+((1 - p_male) * (1 - p_wf) * p_hf))

	g_11_temp = (p_male * (1 - p_wm) * (1 - p_hm))/(p_male * (1 - p_wm) * (1 - p_hm)+((1 - p_male) * (1 - p_wf) * (1 - p_hf)))


	print g_00_temp
	print g_01_temp
	print g_10_temp
	print g_11_temp
	
#	print male, female
	print "P(Male): ", p_male
	print "P(W|M): ", p_wm
	print "P(W|F): ", p_wf
	print "P(H|M): ", p_hm
	print "P(H|F): ", p_hf
	print "P(G|H,F)", g_00_temp
	counter+=1

	improvement = max( abs(g_00[-1] - g_00_temp), abs(g_01[-1] - g_01_temp ), abs(g_10[-1] - g_10_temp), abs(g_11[-1] - g_11_temp) )
	#improvement1 = max(abs(1 - g_00[-1]/g_00_temp), abs(1 - g_01[-1]/g_01_temp ), abs(1 - g_10[-1]/g_10_temp), abs(1 - g_11[-1]/g_11_temp))
	#print log10(improvement1)
	g_00.append(g_00_temp)
	g_01.append(g_01_temp)
	g_10.append(g_10_temp)
	g_11.append(g_11_temp)
	#print improvement
	#print improvement1

	if(counter > 100):
		break
