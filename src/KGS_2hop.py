import pandas as pd
#pd.options.mode.chained_assignment = None
pd.set_option("display.max_rows", None, "display.max_columns", None, "display.expand_frame_repr", False, "mode.chained_assignment", None)
allPredicates = ['isLeaderOf', 'owns', 'isCitizenOf', 'isLocatedIn', 'hasMusicalRole', 'hasOfficialLanguage', 'edited', 'isConnectedTo', 'actedIn', 'imports', 'participatedIn', 'wasBornIn', 'dealsWith', 'created', 'diedIn', 'isPoliticianOf', 'wroteMusicFor', 'hasNeighbor', 'isMarriedTo', 'hasChild', 'isInterestedIn', 'isAffiliatedTo', 'hasCurrency', 'exports', 'happenedIn', 'hasGender', 'playsFor', 'directed', 'worksAt', 'graduatedFrom', 'hasCapital', 'influences', 'hasWonPrize', 'hasWebsite', 'livesIn', 'hasAcademicAdvisor', 'isKnownFor']
df = pd.read_csv('yagoFactsCleaned.csv')
df.columns = ['Subject', 'Predicate', 'Object']
def search(queryList):
    df2 = df.loc[df['Subject'].isin(queryList) | df['Object'].isin(queryList)]
    tf = df2.merge(right=df2, left_on='Object', right_on='Subject')
    tf['Subject'], tf['Predicate'], tf['Object'] = tf['Subject_x'], tf['Predicate_x']+tf['Predicate_y'], tf['Object_y']
    tf = tf.loc[:, ['Subject', 'Predicate', 'Object']]
    df2 = pd.concat([df2, tf])
    predicateList = df2['Predicate'].tolist()
    predicateListUnique = list(dict.fromkeys(predicateList))
    df2['Relevance'] = 0
    df2.loc[df2['Subject'].isin(queryList), 'Relevance'] += 1
    df2.loc[df2['Object'].isin(queryList), 'Relevance'] += 1
    df2.loc[df2['Predicate'].isin(allPredicates), 'Relevance'] += 0.1
    df2.loc[df2['Subject'] == df2['Object'], 'Relevance'] = 0
    for n in predicateListUnique:
        df2.loc[df2['Predicate'] == n, 'Relevance'] += 1/(predicateList.count(n)*10)
    df2.sort_values(by=['Relevance'], ascending=False, inplace=True)
    print(df2)
while True:
    search(input('Please input the search terms'))