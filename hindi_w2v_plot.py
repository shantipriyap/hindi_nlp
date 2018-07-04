# -*- coding: utf-8 -*-

#########################################################
# By: Shantipriya Parida    
#########################################################

##########################################################
# Program: hindi_w2v_plot.py
# Description:Python script to plot Hindi word embedding
#             using PCA
#
# Usage:   python hindi_w2v_plot.py
##########################################################

##########################################################
# Declaration Part
#
##########################################################

import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.decomposition import PCA


#List of Hindi Word for embedding

hi_word_list =['इमारतें', 'इमारतों', 'भवन', 'बिल्डिंग', 'सड़कें', 'इमारत', 'भवनों', 'ईमारते', 'सड़क', 'निर्माण', 'खिड़की', 'कारों', 'ईमारते', 'विमान', 'दीवारों',]

def Plot_w2v(hi_word_list):
	model = Word2Vec(hi_word_list, min_count=1)
	X = model[model.wv.vocab]
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)
	# create a scatter plot of the projection
	plt.scatter(result[:, 0], result[:, 1])
	words = list(model.wv.vocab)
	for i, word in enumerate(words):
		plt.rc('font', family='Lohit Devanagari',size=25)
		plt.annotate(word, xy=(result[i, 0], result[i, 1]))
	plt.show()

#Main

#Define model with Hindi word list
model = Word2Vec(hi_word_list, min_count=1)

#Plot hindi embedding
Plot_w2v([hi_word_list])

##################################################
# Program End
##################################################
