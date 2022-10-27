import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Students' performance in exams")
df = pd.read_csv('StudentsPerformance.csv')
df['total_score'] = df['math_score'] + df['reading_score'] + df['writing_score']

st.subheader('The effect of gender')
df.pivot_table(values=['math_score', 'reading_score', 'writing_score'], index='gender').reset_index()
fig, axes=plt.subplots(1, 3,sharey=True, figsize=(13,7))
sns.barplot(ax=axes[0], x='gender', y='math_score', data=df,  ci=None)
sns.barplot(ax=axes[1], x='gender', y='reading_score', data=df, ci=None)
sns.barplot(ax=axes[2], x='gender', y='writing_score', data=df, ci=None)
plt.tight_layout(pad=4.0)
fig.suptitle('average score in exams by gender', fontsize=20)
st.pyplot(fig)

st.subheader('The effect of parental level of education')
df1 = df[['parental_level_of_education','total_score']].groupby('parental_level_of_education').mean()
df2 = df1.sort_values(by='total_score',ascending=False)
fig6, ax6 = plt.subplots(figsize = (20,6))
df2.plot.bar(ax = ax6)
st.pyplot(fig6)

st.subheader('The effect of economic level of the family')
df.pivot_table(values=['math_score', 'reading_score', 'writing_score'], index='lunch').reset_index()
fig4, ax4=plt.subplots(1, 3,sharey=True, figsize=(13,7))
sns.barplot(ax=ax4[0], x='lunch', y='math_score', data=df,  ci=None)
sns.barplot(ax=ax4[1], x='lunch', y='reading_score', data=df, ci=None)
sns.barplot(ax=ax4[2], x='lunch', y='writing_score', data=df, ci=None)
plt.tight_layout(pad=4.0)
fig4.suptitle('average score in exams by economic level of the family', fontsize=20)
st.pyplot(fig4)

st.subheader('The effect of preparation level')
df.pivot_table(values=['math_score', 'reading_score', 'writing_score'], index='test-preparation-course').reset_index()
fig5, ax5=plt.subplots(1, 3,sharey=True, figsize=(13,7))
sns.barplot(ax=ax5[0], x='test-preparation-course', y='math_score', data=df,  ci=None)
sns.barplot(ax=ax5[1], x='test-preparation-course', y='reading_score', data=df, ci=None)
sns.barplot(ax=ax5[2], x='test-preparation-course', y='writing_score', data=df, ci=None)
plt.tight_layout(pad=4.0)
fig4.suptitle('average score in exams by preparation level', fontsize=20)
st.pyplot(fig5)

st.subheader('Correlation analysis of these scores')
fig1, ax1 = plt.subplots(1,3,figsize=(36,12))
df.plot.scatter(x='writing_score',y='math_score',ax=ax1[0])
df.plot.scatter(x='writing_score',y='reading_score',ax=ax1[1])
df.plot.scatter(x='reading_score',y='math_score',ax=ax1[2])
st.pyplot(fig1)

test_filter =  st.sidebar.selectbox(
    'Chosse their test type',
    ('math score','reading score','writing score'),
)
if test_filter == 'math score':
    dfm = df[['group','math_score']]
elif test_filter == 'reading score':
    dfm = df[['group','reading_score']]
elif test_filter == 'writing score':
    dfm = df[['group','writing_score']]

group_filter = st.sidebar.radio(
    'Choose the group you want to know',
    ('A','B','C','D','E')
)
if group_filter == 'A':
    dfm = dfm[dfm.group == 'group A']
elif group_filter == 'B':
    dfm = dfm[dfm.group == 'group B']
elif group_filter == 'C':
    dfm = dfm[dfm.group == 'group C']
elif group_filter == 'D':
    dfm = dfm[dfm.group == 'group D']
elif group_filter == 'E':
    dfm = dfm[dfm.group == 'group E']

fig2, ax2 = plt.subplots()
st.subheader('Histogram of their score of each group')
dfm.plot.hist(ax=ax2)
ax2.set_xlabel('score')
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
st.subheader('Line Plot of their score of each group')
dfm.plot(ax=ax3)
st.pyplot(fig3)