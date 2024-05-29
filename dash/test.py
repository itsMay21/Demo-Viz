import pandas as pd
import plotly.express as px

df_w_fact=pd.read_csv('./Data_files/'+'gdp_current_updated'+'.csv')

count_list=['India', 'China', 'Japan', 'United States']

df_w_fact_t=df_w_fact.transpose()
new_header = df_w_fact_t.iloc[0] 
df_w_fact_t = df_w_fact_t[4:]
df_w_fact_t.columns = new_header
df_w_fact_t.index.name = 'year'
df_w_fact_t.to_csv('update.csv')
df_w_fact_t = pd.read_csv('update.csv')

df1=pd.melt(df_w_fact_t, id_vars=['year'], value_vars=count_list)

df1.to_csv('test.csv')

fig = px.line(df1, x="year", y="value", color='variable')

fig.show()