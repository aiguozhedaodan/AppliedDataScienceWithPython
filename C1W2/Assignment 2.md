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

```html
def answer_four():
    df['point']=df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']
    return df['point']
```
Out[]:
Afghanistan                            2
Algeria                               27
Argentina                            130
Armenia                               16
Australasia                           22
Australia                            923
Austria                              569
Azerbaijan                            43
Bahamas                               24
Bahrain                                1
Barbados                               1
Belarus                              154
Belgium                              276
Bermuda                                1
Bohemia                                5
Botswana                               2
Brazil                               184
British West Indies                    2
Bulgaria                             411
Burundi                                3
Cameroon                              12
Canada                               846
Chile                                 24
China                               1120
Colombia                              29
Costa Rica                             7
Ivory Coast                            2
Croatia                               67
Cuba                                 420
Cyprus                                 2

Spain                                268
Sri Lanka                              4
Sudan                                  2
Suriname                               4
Sweden                              1217
Switzerland                          630
Syria                                  6
Chinese Taipei                        32
Tajikistan                             4
Tanzania                               4
Thailand                              44
Togo                                   1
Tonga                                  2
Trinidad and Tobago                   27
Tunisia                               19
Turkey                               191
Uganda                                14
Ukraine                              220
United Arab Emirates                   3
United States                       5684
Uruguay                               16
Uzbekistan                            38
Venezuela                             18
Vietnam                                4
Virgin Islands                         2
Yugoslavia                           171
Independent Olympic Participants       4
Zambia                                 3
Zimbabwe                              18
Mixed team                            38
Name: point, Length: 146, dtype: int64
## Part 2
For the next set of questions, we will be using census data from the [United States Census Bureau](http://www.census.gov). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. [See this document](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2015/co-est2015-alldata.pdf) for a description of the variable names.

The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.

### Question 5
Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)

*This function should return a single string value.*

```html
def answer_five():
    census_df2=census_df[census_df['SUMLEV']==50]
    return census_df2['STNAME'].value_counts().index[0]]
```
Out[]: 'Texas'
### Question 6
**Only looking at the three most populous counties for each state**, what are the three most populous states (in order of highest population to lowest population)? Use `CENSUS2010POP`.

*This function should return a list of string values.*
```html
def answer_six():
    census_df2=census_df[census_df['SUMLEV']==50]
    df3=census_df2[['STNAME','CTYNAME','CENSUS2010POP']].sort_values('CENSUS2010POP',ascending=False).groupby(by='STNAME').head(3)
    df4=df3.groupby(by='STNAME').sum().sort_values('CENSUS2010POP',ascending=False)[0:3]
    return list(df4.index)
```
Out[]: ['California', 'Texas', 'Illinois']
### Question 7
Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)

e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.

*This function should return a single string value.*
```html
def answer_seven():
    census_df2=census_df[census_df['SUMLEV']==50]
    pop=census_df2[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015','CTYNAME']].set_index('CTYNAME')
    pop['minus']=pop.T.max()-pop.T.min()
    return pop.sort_values('minus').index.values[-1]
```
Out[]: 'Harris County'
### Question 8
In this datafile, the United States is broken up into four regions using the "REGION" column.

Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.

*This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*

```html
def answer_eight():
    census_df2=census_df[census_df['SUMLEV']==50]
    region=census_df2[(census_df2['REGION']==1) | (census_df2['REGION']==2)].loc[:,['REGION','CTYNAME','STNAME','POPESTIMATE2015','POPESTIMATE2014']]
    region['name']=region['CTYNAME'].str.startswith('Washington')
    return region.loc[(region['name']==1) & (region['POPESTIMATE2015']> region['POPESTIMATE2014']),['STNAME','CTYNAME']].sort_index()
```
Out[]:

||            STNAME |           CTYNAME|
| --- | --- | --- |
|896|           Iowa|  Washington County|
|1419|     Minnesota|  Washington County|
|2345|  Pennsylvania|  Washington County|
|2355|  Rhode Island|  Washington County|
|3163|     Wisconsin|  Washington County|

## My Notes
### Q1  
df=DataFrame([{‘A’:’11’,’B’:’12’},{‘A’:’111’,’B’:’121’},{‘A’:’1111’,’B’:’1211’}])  
print df.columns.size#列数 2  
print df.iloc[:,0].size#行数 3  
print df.ix[[0]].index.values[0]#索引值 0  
print df.ix[[0]].values[0][0]#第一行第一列的值 11  
print df.ix[[1]].values[0][1]#第二行第二列的值 121  
### Question 5
SUMLEV的值为40的行是州（STATE）的观测资料，SUMLEV的值为50的行是郡（COUNTY）的观测资料
### Question 6
df3=census_df2[['STNAME','CTYNAME','CENSUS2010POP']].sort_values('CENSUS2010POP',ascending=False).groupby(by='STNAME').head(3) # One STATE only have three most population country in df3 在df3中一个州只有三个人数最多的郡，groupby后执行的指令是按照group分组执行。同理groupby(by='STNAME').sum()，求和也是分组进行。
### Question 8
The return of 'str.startswith('Washington')' is boolean. Ture means 1 and False means 0.
