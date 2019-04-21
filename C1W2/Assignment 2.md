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
