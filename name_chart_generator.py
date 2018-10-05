import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#import df for a particular state.
def import_state_df(state_name):
	state_df = pd.read_csv('namesbystate\\'+state_name+'.txt', names = ['sex','year','name','name_count'])
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

def sex_of_name_dataframe(sex_df):
	if sex_df.max() == sex_df.min():
		return sex_df.max()
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

def sex_color_scheme(sex_df):
	sex = sex_of_name_dataframe(sex_df)
	
	colors_dict ={
		'F': ['salmon','orange','gold','lightgreen', 'mediumaquamarine', 'LightSkyBlue', 'plum'],
		'M': ['CornflowerBlue','MediumSeaGreen','MediumTurquoise','SlateGray','Wheat', 'Sienna','Silver'],
		'MIX': ['MediumSeaGreen', 'Wheat','IndianRed','CornflowerBlue','Silver', 'Gold','MediumPurple']
	}
	plot_colors = colors_dict[sex]
	return plot_colors


def name_comparison_graph_v2(names_and_sex_dict, state_name):
	#conver the dictionary to a dataframe
	names_and_sex = pd.DataFrame(names_and_sex_dict)

	#import the state's name dataframe	
	state_df = import_state_df(state_name);

	#graphing decisions	
	#start by figuring out how many names are in the dataset. This will impact the size of the figure you build, so we'll handle both in the same bit of code. 
	num_names = len(names_and_sex)
	fig_height = 4
	subplot_col = 1

	if num_names>7:
		print('Error - do not submit more than 5 names')
	elif num_names+1>4:
		fig_height = fig_height*2
		subplot_col = subplot_col*2

	#figure out the right color scheme for the sex mix of name's you're looking at.
	plot_colors = sex_color_scheme(names_and_sex['sex'])

	#figure out total max names, so you know what the upper bound of the x-axis should be. multiply by 1.1 so the top value does not hit the top of the graph
	max_name_count = most_popular_name_count(names_and_sex['name'], state_df)*1.1

	#build your plots for each name
	for label, row in names_and_sex.iterrows():
		plt.figure(1, figsize=(12,fig_height))
		plt.style.use('seaborn')
		ax1 = plt.subplot(subplot_col, 4, label+1)
		name_plot(name_search(row['sex'],row['name'], state_df), plot_colors[label])
		ax1.set_ylim(0,max_name_count)
		ax1.set_xlim(1911,2017)

	#build stacked plot for comparing all names
	ax2 = plt.subplot(subplot_col,4,num_names+1)
	for label, row in names_and_sex.iterrows():
		name_plot(name_search(row['sex'],row['name'], state_df), plot_colors[label])
		plt.title('Comparison')
		ax2.set_ylim(0,max_name_count)

	#title
	plt.suptitle("Comparison of Popularity of Names in " + state_name)

	#If you want a subtitle under the graph, you have to get creative with annotate
	#plt.annotate(
	#	'The names listed here were all ranked #1 at some point 1910-2017 in MA. Note that as time goes on, the #1 name becomes comparatively less popular. \n Parents in 2018 should not worry too much about giving their child a name that is "too popular".', 
	#	xy=(1480, -1000), xycoords='data', annotation_clip=False, fontstyle = 'italic')
	
	#show and then close your plot, for good housekeeping
	plt.show()
	plt.close()


#dict of girl names, which I convert to a dataframe. 
girls_name_dict = {
	'name':['Mary','Jennifer','Linda','Lisa','Jessica','Emily','Emma'],
	'sex':['F','F','F', 'F','F','F','F']
	}

boys_name_dict = {
	'name':['Joseph','Nicholas','Peter','Anthony','Vincent','Francis','Dominic'],
	'sex':['M','M','M', 'M','M','M','M']
	}

theresa_name_dict = {
	'name':['Theresa','Therese'],
	'sex':['F','F']
}

#call the function to build the comparison chart. 
name_comparison_graph_v2(theresa_name_dict, 'MA')


