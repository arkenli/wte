import pandas as pd
import numpy as np

df_u=pd.read_csv('data/food-com-recipes-and-user-interactions/RAW_interactions.csv')

def get_user_rates(user_id):
    return df_u[df_u['user_id']==user_id]

def get_recipe_rates(recipe_id):
    return df_u[df_u['recipe_id'] == recipe_id]