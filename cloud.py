#!/usr/bin/env python3
import os
from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(os.path.join(d, "dril.txt")).read()

# adding stopwords
stopwords = set(STOPWORDS)
stopwords.add("one")
stopwords.add("will")
stopwords.add("co")
stopwords.add("im")


wc = WordCloud(stopwords=stopwords)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(os.path.join(d, "dril_cloud.png"))
