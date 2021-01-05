# knowledge-graphs-search
Files related to the BSP1 of which the ultimate aim is to retrieve relevant search results from different knowledge graphs for question answering purposes.

The results can be reproduced only using a cleaned version of the 'yagoFacts' file (see https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/downloads) which has the csv file type. The sample yagoFactsCleaned.csv provided here represents a small subset of the file used and is not sufficient to reproduce the same results.

For the time being, the full yagoFactsCleaned.csv file used in this project can be downloaded under https://www.dropbox.com/s/zd5hqqit1kmwd05/yagoFactsCleaned.csv?dl=0.


## Benchmark details

## References
[1]     Xiaolu Lu, Soumajit Pramanik, Rishiraj Saha Roy, Abdalghani Abujabal, Yafang Wang, Gerhard Weikum:
Answering Complex Questions by Joining Multi-Document Evidence with Quasi Knowledge Graphs. SIGIR 2019: 105-114
[2]     Gjergji Kasneci, Fabian M. Suchanek, Georgiana Ifrim, Maya Ramanath, Gerhard Weikum:
NAGA: Searching and Ranking Knowledge. 
[3] Report from Dagstuhl Seminar 18371 Knowledge Graphs: New Directions for Knowledge Representation on the Semantic Web

## Introduction

#Refer to Dagstuhl seminar[3]

Today, the World Wide Web is evolving in terms of the Knowledge content at an unimaginable rate. 
Despite of this so many approaches developed in the past decades make the assumption that knowledge on the web, or elsewhere, 
is just a static thing. New methods, technologies and standards
that we produce, or propose, need to start from the assumption that everything is
dynamic, and build on that, rather than ignoring it and then potentially trying to cover it by
add-ons at the end. 

Knowledge Graphs have an important role in organizing and making information more broadly
available to people and machines. Although there are more and more efforts to build knowledge graphs 
that complement the “mainstream” KGs such as DBpedia and Wikidata, and a plethora of work that try to improve
those knowledge graphs in various directions (e.g., adding missing pieces of information, or
flagging incorrect axioms), there is a growing need to define the standards for an evaluation, and most importantly how to periodically update. For instance, Yuqing Gao from Microsoft pointed out their challenge of having a real-time knowledge graph, but with archiving, which
is still a research challenge at Microsoft. Jamie Taylor of Google also acknowledged the long
term evolution of the Google Knowledge Graph as one of their main challenges. The IBM
Watson group is also struggling with similar challenges, although they claim to take a more
dynamic approach, not focusing on one global knowledge graph, but a framework for building
domain specific knowledge graphs, including knowledge discovery and analysis of change
effects. Thus, their main struggles include modelling and analysing changing information
and incrementally updating global knowledge on horizontally scaled storage solutions.

Studying how knowledge graphs (KG) may capture the evolutionary nature of knowledge is a
critical need that the community must address. In this report, we detail a motivating
use-case which shows how importance it is to constantly evolve the KGs to address the 
modern requirements.

The rest of the chapter is organized as follows. Section xx briefly explores related
work that we may use as as starting points for further studying evolving knowledge graphs.
Section xx describes our use-cases for showing how important it is to evolve the knowledge graphs, as identified during this
Dagstuhl seminar[3]. Section xx presents the experiments that we counducted during the course of this project. Finally, in Section xx, we summarize and conclude.


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

