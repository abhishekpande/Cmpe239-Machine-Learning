#! /usr/bin/python

import json

from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob

infile = "data/yelp_academic_dataset_review.json"

# read the first 1000 reviews
i = 0
fin = open(infile, 'r')
data = []
for line in fin:
    review = json.loads(line)
    data.append((review['text'], float(review['stars'])))
    if i == 1000:
        break
    i += 1
fin.close()

k = 500
training_set, test_set = data[:k], data[k:]
print "building classifier"
cl = NaiveBayesClassifier(training_set)
print "built classifier"

# Compute accuracy
print "computing accuracy"
print("Accuracy: {0}".format(cl.accuracy(test_set)))
print "computed accuracy"
 
# Show 5 most informative features
print "showing features"
cl.show_informative_features(5)
print "done :)"
