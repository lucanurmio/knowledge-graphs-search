# knowledge-graphs-search
Files related to the BSP1 of which the ultimate aim is to retrieve relevant search results from different knowledge graphs.
yagoFactsSearchEngine.py loads Yago facts from a CSV file onto a pandas dataframe, takes a list as query and returns the most relevant rows



#TODO:
##10-Nov-2020

1. Use a part of the benchmark questions and setup an iteration to determine the mean reciprocal rank (MRR).
2. You may randomly choose say 20 questions and manually create triples corresponding to those questions. Give each such triples (in the form of a list) asn input to your ranking algorithm.
3. Find scores corresponding to each question; and then, find the mean of the scores to find the MRR.
4. Now modify/turn your ranking algorithm and see how the MRR changes.
