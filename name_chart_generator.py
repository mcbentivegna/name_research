import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from cycler import cycler

MA = pd.read_csv('C:\\Users\\Michelle\\Documents\\namesbystate\\MA.txt', names = ['sex','year','name','name_count'])

def name_search(sex_to_search, name_to_search):
	name_dataframe = MA[np.logical_and(MA['sex'] == sex_to_search, MA['name'] == name_to_search)]  
	return name_dataframe

def most_popular_name_count(names):
	most_popular_all_var= MA[MA['name'].isin(names)].max()
	most_popular_count =most_popular_all_var['name_count']
	return most_popular_count

def sex_of_name_dataframe(sex):
	if sex.max() == sex.min():
		return sex.max()
	else:
		return 'MIX'

def name_plot(name_dataframe, my_color):
	plt.fill_between(
		name_dataframe['year'], 
		name_dataframe['name_count'], 
		np.zeros(len(name_dataframe['year'])),
		color = my_color
		)
	plt.title(name_dataframe.iloc[0,2])


def name_comparison_graph_v2(names_and_sex):
	num_names = len(names_and_sex)

	#colors scheme based on sex of names
	colors_dict ={
		'F': ['salmon','orange','gold','lightgreen', 'mediumaquamarine', 'plum'],
		'M': ['CornflowerBlue','MediumSeaGreen','MediumTurquoise','SlateGray','Wheat'],
		'MIX': ['MediumSeaGreen', 'Wheat','IndianRed','CornflowerBlue','Silver']
	}

	plot_colors = colors_dict[sex_of_name_dataframe(names_and_sex['sex'])]


	fig_height = 4
	subplot_col = 1

	#multiply by 1.1 so the top value does not hit the top of the graph
	max_name_count = most_popular_name_count(names_and_sex['name'])*1.1


	if num_names>5:
		return'Error - do not submit more than 5 names'
	elif num_names+1>3:
		fig_height = fig_height*2
		subplot_col = subplot_col*2
	elif num_names+1>6:
		fig_height = fig_height*3
		subplot_col = subplot_col*3
	
	for label, row in names_and_sex.iterrows():
		plt.figure(1, figsize=(10,fig_height))
		#plt.style.use('seaborn')
		ax1 = plt.subplot(subplot_col, 3, label+1)
		name_plot(name_search(row['sex'],row['name']), plot_colors[label])
		ax1.set_ylim(0,max_name_count)
		ax1.set_xlim(1911,2017)

	ax2 = plt.subplot(subplot_col,3,num_names+1)

	for label, row in names_and_sex.iterrows():
		name_plot(name_search(row['sex'],row['name']), plot_colors[label])
		plt.title('Comparison')
		ax2.set_ylim(0,max_name_count)

	plt.suptitle('Frequency of Given Names by Year of Birth in Massachusetts')


	plt.show()
	plt.close()



name_dict = {
	'name':['Carol','Caroline','Carolyn'],
	'sex':['F','F','F']
	}

name_df = pd.DataFrame(name_dict)

boys_name_dict = {

	'name':['Vincent','Anthony','Joseph','Nicholas','Dominic'],
	'sex':['M','M','M','M','M']
}

boys_name_df = pd.DataFrame(boys_name_dict)

name_comparison_graph_v2(name_df)


