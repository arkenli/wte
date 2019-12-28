'''
推荐系统：
1.卡路里总值
2.protein
3.糖，脂肪量不能过多
4.主要材料相同
5。categories(标签)

'''
import tools
import pandas as pd
import numpy as np
import json


df_r = pd.read_csv('data/food-com-recipes-and-user-interactions/RAW_recipes.csv')


def segmentation():
    dict={}
    all_ingredients=[]
    for i in range(len(df_r)):
        ingredient=df_r['ingredients'][i]
        s=ingredient[2:-2].replace(' ','')
        s = "'" + s + "'"
        s=s.split(',')
        elements=[]
        for element in s:
            elements.append(element[1:-1])
            if element[1:-1] in all_ingredients:
                continue
            else:
                all_ingredients.append(element[1:-1])
        dict[df_r['name'][i]]=elements
    res=json.dumps(dict)
    tools.wirte_result(res,'ingredients.json')
    np.save('all_ingredients',all_ingredients)
    return dict,all_ingredients

