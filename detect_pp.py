# Present Perfect Detector
# Written by Pawel Mrozik

import re
import time
from sets import Set

start_time = time.time()
past_participles = []
pronouns = []
has_have = ['has', 'have']
rocky_file = "Rocky Balboa.DVDRip.DiAMOND.en.srt"
grimm_file = "grimm2.txt"
has_sentences = []

#regex
# pronouns
def present_perfect_search():
    counter=0
    with open(grimm_file) as f:
        for line in f:
            matchObj = re.search( r'have|has', line, re.M|re.I)
            if matchObj:
                counter=counter+1
                has_sentences.append(line)
                print "%d. Matched object: %s" %(counter, line),
            else:
                pass
    print "%d matches." % counter
    for line in has_sentences:
        matchObj = re.search( r'(have|has)\s(never)', line, re.M | re.I)
        if matchObj:
            print "PP with never: %s\n\n" % line,
        else:
            pass
                
def read_past_participles():
    print "Reading past participle list...",
    
    with open('past_participle_verbs.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            words = line.split(',')
            for w in words:
                w.strip()
                past_participles.append(w)
    print "done"
    print past_participles


def read_pronouns():
    print "Reading pronoun list...",

    with open('pronouns.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            words = line.split(',')
            for w in words:
                w.strip()
                pronouns.append(w)
    print "done"
    print pronouns
    

read_past_participles()
read_pronouns()
present_perfect_search()

print "Run time: %s seconds" % (time.time() - start_time)
