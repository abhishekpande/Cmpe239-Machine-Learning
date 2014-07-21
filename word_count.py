#! /usr/bin/python

infile = 'data/raw_reviews.txt'
outfile = 'data/word_count.txt'
fin = open(infile, 'r')
try:
    i = 0
    skipped = 0
    word_dict = {}
    for line in fin:
        if i % 10000 == 0:
            print "processing %d" % i
        i += 1
        words = line.split(' ')
        for word in words:
            if not word.strip():
                continue
            try:
                if word_dict.has_key(word.strip()):
                    word_dict[word.strip()] += 1
                else:
                    word_dict[word.strip()] = 1
            except:
                skipped += 1
    print "skipped %d" % skipped
    i = 0
    fout = open(outfile, 'w')
    for key in word_dict:
        if i % 10000 == 0:
            print "processing %d" % i
        i += 1
        fout.write('%d %s\n' % (word_dict[key], key))
    fout.close()
finally:
    fin.close()
