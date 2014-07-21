#! /usr/bin/python

import json

infile = "data/yelp_academic_dataset_review.json"
outfile = "data/raw_reviews.txt"
fin = open(infile, 'r')
fout = open(outfile, 'w')
i = 0
skipped = 0
for line in fin:
    if i % 100 == 0:
        print "Processing %d" % i
    i += 1
    review = json.loads(line).get('text', '').strip()
    if review:
        try:
            fout.write(review)
            fout.write('\n')
        except:
            skipped += 1
print "skipped %d reviews" % skipped
print "done :)"
