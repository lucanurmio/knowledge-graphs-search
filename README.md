# knowledge-graphs-search
Files related to the BSP1 of which the ultimate aim is to retrieve relevant search results from different knowledge graphs.
yagoFactsSearchEngine.py loads Yago facts from a CSV file onto a pandas dataframe, takes a list as query and returns the most relevant rows.


## Benchmark details

## References
[1]     Xiaolu Lu, Soumajit Pramanik, Rishiraj Saha Roy, Abdalghani Abujabal, Yafang Wang, Gerhard Weikum:
Answering Complex Questions by Joining Multi-Document Evidence with Quasi Knowledge Graphs. SIGIR 2019: 105-114




### TODO:
#### 10-Nov-2020

1. Use a part of the benchmark questions and setup an iteration to determine the mean reciprocal rank (MRR).
2. You may randomly choose say 20 questions and manually create triples corresponding to those questions. Give each such triples (in the form of a list) asn input to your ranking algorithm.
3. Find scores corresponding to each question; and then, find the mean of the scores to find the MRR.
4. Now modify/turn your ranking algorithm and see how the MRR changes.

### TODO:
#### 17-Nov-2020
 
1. Make a note of the observations that you made for getting 0.5 RR score for an arbitary sample query.
2. Modify the search function to return the RR score for a single entity rather than for a triple.
3. Modify the arguments of the search function such that only a single golden answer is passed instead of the entire triple.
4. Manually increase the number of questions in the benchmark question list to a larger number.
5. Think of a new ranking scheme -- consider question statements where the subject and object individually match with multiple triples in the yago data set; and, the best answer is not from any of the retrieved triple which at least a match.


### TODO
#### 15-Dec-2020


## Work Done

Bench

## Future Work
Tried random 20 queries from the benchmark, for 1 hop and 2 hop. Improvement in performance?

Use advanced graph analytics frameworks: NetworkX, Spark GraphX libraries

## Conclusions

Tired out 80 queries from the XX bechmark queries, and the following are our results:

Accuracy values:

                      hop1   hop2   hop3 
benchmark-10 queries  xx         xx          xx
benchmark-20 queries  xx         xx          xx
benchmark-40 queries  xx         xx          xx
benchmark-80 queries  xx         xx          xx

All are randomly picked queries from the XX benchmarks.


Avg Runtime:

                      hop1   hop2   hop3 
benchmark-10 queries  xx         xx          xx
benchmark-20 queries  xx         xx          xx
benchmark-40 queries  xx         xx          xx
benchmark-80 queries  xx         xx          xx


==> Report if there are any trade-offs (Accuracy Vs Runtime)

Explain the ranking function that you used and how did you come up with this function? Detail the intuitions.

Use networkX and visualize a couple of examples. Mention the steps involved in ploting the graph using networkX.

And, what did you feel about using networkX instead of dataframe?

Also, can networkX be used if the graph is massive? Do we need bigdata tools such as Spark GraphX for such case? -- future works.


Do you think google trends queries could be answered using the current static KGs? Cite some examples from the
google trend queries.. what we should do to overcome this? can we try augmenting the current KG with new edges and nodes based on
the google news and other social media sources?

