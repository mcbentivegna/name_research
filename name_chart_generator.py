import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def import_state_df(state_name):
	state_df = pd.read_csv('C:\\Users\\Michelle\\Documents\\namesbystate\\'+state_name+'.txt', names = ['sex','year','name','name_count'])
	return state_df

#return a dataframe of a particular name and sex in a particular state (i.e F, 1910, Mary, 500; F, 1910, Sarah, 450 etc.)
def name_search(sex_to_search, name_to_search, state_df):
	name_dataframe = state_df[np.logical_and(state_df['sex'] == sex_to_search, state_df['name'] == name_to_search)]  
	return name_dataframe

#find the largest name count from a set of names. The purpose of this function is to help you know what the y-axis max should be on your graph.
#For example, if you're comparing Caroline and Julia, and Caroline's peak popularity was 400 in 2000, and Julia's was 500 in 1990, you would want the max of your y-axis to be 500.
def most_popular_name_count(names, state_df):
	most_popular_all_var= state_df[state_df['name'].isin(names)].max()
	most_popular_count =most_popular_all_var['name_count']
	return most_popular_count

def sex_of_name_dataframe(sex):
	if sex.max() == sex.min():
		return sex.max()
	else:
		return 'MIX'

#Build a plot of a set of names
def name_plot(name_dataframe, my_color):
	plt.fill_between(
		name_dataframe['year'], 
		name_dataframe['name_count'], 
		np.zeros(len(name_dataframe['year'])),
		color = my_color
		)
	plt.title(name_dataframe.iloc[0,2])


def name_comparison_graph_v2(names_and_sex, state_name):
	
	state_df = import_state_df(state_name);
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
	max_name_count = most_popular_name_count(names_and_sex['name'], state_df)*1.1


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
		plt.style.use('seaborn')
		ax1 = plt.subplot(subplot_col, 3, label+1)
		name_plot(name_search(row['sex'],row['name'], state_df), plot_colors[label])
		ax1.set_ylim(0,max_name_count)
		ax1.set_xlim(1911,2017)

	ax2 = plt.subplot(subplot_col,3,num_names+1)

	for label, row in names_and_sex.iterrows():
		name_plot(name_search(row['sex'],row['name'], state_df), plot_colors[label])
		plt.title('Comparison')
		ax2.set_ylim(0,max_name_count)

	plt.suptitle('Frequency of Given Names by Year of Birth in ' + state_name)


	plt.show()
	plt.close()



girls_name_dict = {
	'name':['Mary','Jennifer','Jessica','Emily','Emma'],
	'sex':['F','F','F', 'F','F']
	}

girls_name_df = pd.DataFrame(girls_name_dict)

boys_name_dict = {

	'name':['Vincent','Anthony','Joseph','Nicholas','Dominic'],
	'sex':['M','M','M','M','M']
}

boys_name_df = pd.DataFrame(boys_name_dict)

name_comparison_graph_v2(girls_name_df, 'WI')


