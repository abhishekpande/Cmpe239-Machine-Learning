#! /usr/bin/python

import sqlite3

infile = 'data/sorted_word_count.txt'
dbfile = 'data/word_count.db'
fin = open(infile, 'r')
conn = sqlite3.connect(dbfile)
try:
    c = conn.cursor()
    c.execute("create table words (word text, frequency integer)")
    i = 0
    for line in fin:
        i += 1
        if (i == 50000):
            break
        if i % 1000 == 0:
            print "processing %d" % i
        frequency, word = line.strip().split(' ')
        c.execute("insert into words (word, frequency) values (?, ?)", (word, frequency))
        conn.commit()
    print "done :)"
finally:
    fin.close()
    conn.close()
