import pandas as pd
queryList = []
df3 = pd.DataFrame()
while [] not in queryList:
        queryList.append(input('Please enter your query or press enter: ').split())
queryList.pop()
df = pd.read_csv('yagoFactsCleaned.csv')
df.columns = ['Subject', 'Predicate', 'Object']
for l in range(0, len(queryList)):
        mainIndexList = []
        importance = []
        predicateListFrequencies = []
        for i in range(0, len(queryList[l])):
            mainIndexList.extend(df.index[df.loc[:, "Subject"] == queryList[l][i]].tolist())
            mainIndexList.extend(df.index[df.loc[:, "Predicate"] == queryList[l][i]].tolist())
            mainIndexList.extend(df.index[df.loc[:, "Object"] == queryList[l][i]].tolist())
        mainIndexListUnique = list(dict.fromkeys(mainIndexList))
        for m in mainIndexListUnique:
                importance.append(100**mainIndexList.count(m))
        df2 = df.iloc[mainIndexListUnique]
        df2.loc[:, "Relevance"] = importance
        predicateList = df2.loc[:, 'Predicate'].tolist()
        predicateListUnique = list(dict.fromkeys(predicateList))
        for k in predicateList:
                predicateListFrequencies.append(predicateList.count(k))
        lowestUniquePredicateFrequency = min(predicateListFrequencies)
        for n in predicateListUnique:
                df2.loc[df.loc[:, 'Predicate'] == n, 'Relevance'] = (df2.loc[df.loc[:, 'Predicate'] == n, 'Relevance']/predicateList.count(n)) * lowestUniquePredicateFrequency
        df3 = df3.append(df2)
df3 = df3.sort_values(by=['Relevance'], ascending=False)
print(df3.head(10))
