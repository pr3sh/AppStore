import pandas as pd
import numpy as np
import re




def countLangs(x):
    try:
        return len(x.split(","))
    except:
        return 0


def value_to_float(x):
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return x
   





def clean(in_df):
	df = in_df.copy(deep=True)
	
	df['num_languages'] = df['languages'].apply(countLangs) #created new column that had the number of languages the app offered
	
	df['boolean_rank'] = df['rank'].notna() #create a new column of booleans indicating whether an app was raned or unranked
	
	df['age_rating'] = df['age_rating'].apply(lambda x: re.search("\d+",x)[0])

	df['app_rating'] = df['app_rating'].replace(np.nan,0)
	df['size'] = df['size'].apply(lambda x: re.match("\d+(\.)?\d*",x)[0])
	df['size'].astype(float) #convert the app size column from string to float object

	df.assign(free_boolean =df['price']=='Free',inplace=True)  #Free or not
	df['rating_count']=df['rating_count'][:].str.split(' ',n=1,expand = True)
	df['rating_count'].fillna("0",inplace=True)

	df['rating_count'] = df['rating_count'].apply(value_to_float) 
	df['rating_count']=df['rating_count'].astype(float)

	df['free_or_not']=df['price']!='Free' #boolean column for free or not



	return df





