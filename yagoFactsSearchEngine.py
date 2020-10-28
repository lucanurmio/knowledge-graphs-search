import pandas as pd
queryList = []
mainIndexList = []
importance = []
predicateListFrequencies = []
#                       Get search terms
while "" not in queryList:
        queryList.append(input('Please add an element to your query or just hit enter: '))
queryList.pop()
#                       Create pandas dataframe
df = pd.read_csv('yagoFactsCleaned.csv')
df.columns = ['Subject', 'Predicate', 'Object']
#                       Get matching indices (as opposed to the rows themselves along with their information)
for i in range(0, len(queryList)):
    mainIndexList.extend(df.index[df.loc[:, "Subject"] == queryList[i]].tolist())
    mainIndexList.extend(df.index[df.loc[:, "Predicate"] == queryList[i]].tolist())
    mainIndexList.extend(df.index[df.loc[:, "Object"] == queryList[i]].tolist())
mainIndexListUnique = list(dict.fromkeys(mainIndexList))
#                       Get match occurences (importance/relevance) per index
for m in mainIndexListUnique:
        importance.append(100**mainIndexList.count(m))
#                       Create new table from matching indices
df2 = df.iloc[mainIndexListUnique]
#                       Create new column in new table for matching indices and their match occurence score (i.e. mainIndexListUnique and importance)
df2.loc[:, "Relevance"] = importance
#                       Count frequency of rarest predicate in new table
predicateList = df2.loc[:, 'Predicate'].tolist()
predicateListUnique = list(dict.fromkeys(predicateList))
for k in predicateList:
        predicateListFrequencies.append(predicateList.count(k))
lowestUniquePredicateFrequency = min(predicateListFrequencies)
#                       For the new table: Divide importance/relevance score of rows by frequency of their respective predicates, then multiply it by frequency of the rarest predicate
for n in predicateListUnique:
        df2.loc[df.loc[:, 'Predicate'] == n, 'Relevance'] = (df2.loc[df.loc[:, 'Predicate'] == n, 'Relevance']/predicateList.count(n)) * lowestUniquePredicateFrequency
#                       Print the sorted new table
df2 = df2.sort_values(by=['Relevance'], ascending=False)
print(df2.head(10))
