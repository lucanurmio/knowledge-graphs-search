# knowledge-graphs-search
Files related to the BSP1 of which the ultimate aim is to retrieve relevant search results from different knowledge graphs.
yagoFactsSearchEngine.py loads Yago facts from a CSV file onto a pandas dataframe, takes a list as query and returns the most relevant rows



#TODO:
##10-Nov-2020

1. Use a part of the benchmark questions and setup an iteration to determine the mean reciprocal rank (MRR).
2. You may randomly choose say 20 questions and manually create triples corresponding to those questions. Give each such triples (in the form of a list) asn input to your ranking algorithm.
3. Find scores corresponding to each question; and then, find the mean of the scores to find the MRR.
4. Now modify/turn your ranking algorithm and see how the MRR changes.

#TODO:
##17-Nov-2020
 
1. Make a note of the observations that you made for getting 0.5 RR score for an arbitary sample query.
2. Modify the search function to return the RR score for a single entity rather than for a triple.
3. Modify the arguments of the search function such that only a single golden answer is passed instead of the entire triple.
4. Manually increase the number of questions in the benchmark question list to a larger number.
5. Think of a new ranking scheme -- consider question statements where the subject and object individually match with multiple triples in the yago data set; and, the best answer is not from any of the retrieved triple which at least a match.
