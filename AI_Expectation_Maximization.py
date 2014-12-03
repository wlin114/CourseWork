from __future__ import division
from math import log10
a = open("hw2dataset_70.txt")
b = []
for x in a:
	if len(x) == 7:
		b.append((x[0], x[2], x[4]))

counter, improvement = 1, float('inf')
#P(G), P(W | G), P(H | G)
#p_male ,p_wm, p_hm, p_wf, p_hf = 0.6,0.7,0.6,0.5,0.4
#p_male ,p_wm, p_hm, p_wf, p_hf = 0.99,0.99,0.99,0.01,0.01
#p_male ,p_wm, p_hm, p_wf, p_hf = 0.01,0.01,0.01,0.99,0.99
p_male ,p_wm, p_hm, p_wf, p_hf = 0.7,0.8,0.7,0.4,0.3

g_00 = (p_male * p_wm * p_hm )/((p_male * p_wm * p_hm )+((1 - p_male ) * p_wf * p_hf ))

g_01 = (p_male * p_wm * ( 1 - p_hm ))/((p_male * p_wm * ( 1 - p_hm )) +((1 - p_male) * p_wf * (1 - p_hf)))

g_10 = (p_male * (1 - p_wm) * p_hm )/((p_male * (1 - p_wm) * p_hm )+((1 - p_male) * (1 - p_wf) * p_hf))

g_11 = (p_male * (1 - p_wm) * (1 - p_hm))/(p_male * (1 - p_wm) * (1 - p_hm)+((1 - p_male) * (1 - p_wf) * (1 - p_hf)))

#Counters
#male: number of male
#w_male: number of (weight, gender | weight)
#h_male: same to above
male, w_male, w_female, h_male, h_female = 200 * p_male, 0, 0, 0, 0

likelihood = 0

while(improvement > 0.0001):
	print counter
	counter+=1

	pre_m = male
	#inititalize
	male, w_male, w_female, h_male, h_female = 0,0,0,0,0
	n_w_m = (p_wm * p_male) / ((p_wm * p_male) + (p_wf * (1-p_male)))
	n_h_m = (p_hm * p_male) / ((p_hm * p_male) + (p_hf * (1-p_male)))
	n_w_f = (p_wf * (1-p_male)) / (p_wf * (1-p_male) + p_wm * p_male)
	n_h_f = (p_hf * (1-p_male)) / (p_hf * (1-p_male) + p_hm * p_male)
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
					#male is #(counter for 000)
					male += g_00
					#w_male is #(counter for x00) 
					w_male += n_w_m
					h_male += n_h_m
					w_female += n_w_f
					h_female += n_h_f

				else:
					male += g_01
					w_male += n_w_m
					w_female += n_w_f
			else:
				if i[2] == '0':
					male += g_10
					h_male += n_h_m
					h_female += n_h_f
				else:
					male += g_11

	female = 200 - male
	#updating for following probs:
	p_male = male/(200)
	p_wm = w_male/(male)
	p_wf = w_female/(female)
	p_hm = h_male/(male)
	p_hf = h_female/(female)

	temp = likelihood
	likelihood = log10(male)*log10(female)+log10(p_wm*male)*log10((1-p_wm)*male)+log10(p_wf*female)*log10((1-p_wf)*female)+log10(p_hm*male)*log10((1-p_hm)*male)+log10(p_hf*female)*log10((1-p_hf)*female) 
	#updating for following probs
	g_00 = (p_male * p_wm * p_hm )/((p_male * p_wm * p_hm )+((1 - p_male ) * p_wf * p_hf ))

	g_01 = (p_male * p_wm * ( 1 - p_hm ))/((p_male * p_wm * ( 1 - p_hm )) +((1 - p_male) * p_wf * (1 - p_hf)))

	g_10 = (p_male * (1 - p_wm) * p_hm )/((p_male * (1 - p_wm) * p_hm )+((1 - p_male) * (1 - p_wf) * p_hf))

	g_11 = (p_male * (1 - p_wm) * (1 - p_hm))/(p_male * (1 - p_wm) * (1 - p_hm)+((1 - p_male) * (1 - p_wf) * (1 - p_hf)))

	improvement = abs(temp - likelihood)

	#print  male, female, w_male, h_male, w_female, h_female
	#print p_male, p_wm, p_wf, p_hm, p_hf
	print "P00: ",g_00
	print "P01: ",g_01
	print "P10: ",g_10
	print "P11: ",g_11
	print "P(Male): ", p_male
	print "P(W|M): ", p_wm
	print "P(H|M): ", p_hm
	print "P(W|F): ", p_wf
	print "P(H|F): ", p_hf
	print "likelihood:", likelihood
	print "Difference: ",improvement

	#iteration limit check
	if(counter > 10000):
		break