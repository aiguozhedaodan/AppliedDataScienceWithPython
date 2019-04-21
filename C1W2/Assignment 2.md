# Assignment 2 - Pandas Introduction
All questions are weighted the same in this assignment.
## Part 1
The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning.

The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.
```html
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
```


| |# Summer|	Gold|	Silver|	Bronze|	Total|#Winter|Gold.1|Silver.1|Bronze.1|Total.1|# Games|Gold.2|Silver.2| Bronze.2|Combined|total|ID|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|Afghanistan|	13|	0|	0|	2|	2	|0	|0|	0|	0|	0|	13|	0	|0|	2|	2|AFG|
|Algeria|	12|	5|	2|	8	|15|	3	|0	|0	|0	|0	|15|	5	|2	|8	|15|	ALG|
|Argentina	|23|	18|	24	|28	|70	|18	|0|	0	|0|	0|41|	18|24|28|70|	ARG|
|Armenia	|5	|1	|2	|9	|12|	6	|0	|0	|0	|0	|11	|1	|2|	9	|12|	ARM|
### Question 0 (Example)

What is the first country in df?

*This function should return a Series.*
```html
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero()
```
```html
Out[2]:
# Summer           13
Gold                0
Silver              0
Bronze              2
Total               2
# Winter            0
Gold.1              0
Silver.1            0
Bronze.1            0
Total.1             0
# Games            13
Gold.2              0
Silver.2            0
Bronze.2            2
Combined total      2
ID                AFG
Name: Afghanistan, dtype: object
```
### Question 1
Which country has won the most gold medals in summer games?

*This function should return a single string value.*
```html
def answer_one():
    return df.sort_values(by='Gold',ascending=False).index.values[0]
```
OUT:'United States'
### Question 2
Which country had the biggest difference between their summer and winter gold medal counts?

*This function should return a single string value.*
```html
def answer_two():
    df['minus']=df['Gold']-df['Gold.1']
    return df.sort_values(by='minus',ascending=False).index.values[0]
```
Out: 'United States'
### Question 3
Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
$$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$

Only include countries that have won at least 1 gold in both summer and winter.

*This function should return a single string value.*

```html
def answer_three():
    df['percent']=(df['Gold']-df['Gold.1'])/df['Gold.2']
    return df[(df['Gold'] > 0) & (df['Gold.1'] > 0)].sort_values(by='percent',ascending=False).index.values[0]
```
Out[]: 'Bulgaria'
### Question 4
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (`Gold.2`) counts for 3 points, silver medals (`Silver.2`) for 2 points, and bronze medals (`Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.

*This function should return a Series named `Points` of length 146*

## My Notes
### Q1  
df=DataFrame([{‘A’:’11’,’B’:’12’},{‘A’:’111’,’B’:’121’},{‘A’:’1111’,’B’:’1211’}])  
print df.columns.size#列数 2  
print df.iloc[:,0].size#行数 3  
print df.ix[[0]].index.values[0]#索引值 0  
print df.ix[[0]].values[0][0]#第一行第一列的值 11  
print df.ix[[1]].values[0][1]#第二行第二列的值 121  
