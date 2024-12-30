This is a sample and basic search engine for persian language based on news list from
a news website with data size of 12202 news (128 MB) which consists of some NLP steps in 2 phases:

Phase 1:
    - Preprocessing
    - Positional index
    - query answering

Phase 2:
    - tdf-idf weighting of docs
    - calculating cosine similiartiy of docs and query
    - enhancing query processing speed using Champions list

In the preprocessing in phase 1, I use two libraries which handled these parts:
    1. [Hazm](https://github.com/roshan-research/hazm): removing stop words, Normalization and Tokenizing
    2. [Parsivar](https://github.com/ICTRC/Parsivar): stemming

The positional index in the first phase and the base data will be included in the next updates.    