import sys
import re
import os

def search(directory, matches, fancy):
    if fancy:
        print "Searching for: %s" % matches
    num = 0
    for root, dirs, files in os.walk(directory):
        path = root.split('/')
        for file in files:
            matched = True
            with open(root + "/" + file, 'r') as f:
                data = f.read()
                for m in matches:
                    if data.find(m) == -1:
                        matched = False
                        break

            if matched:
                num +=1
                if fancy:
                    print("\t" + root + "/" + file + ": matches")
                else:
                    print(root + "/" + file + ": matches")

    return num

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ("Invalid arguments")
        exit()

    # Check for TTY
    fancy = True
    if not os.isatty(1):
        fancy = False

    # directory and search terms
    num = search(sys.argv[1], sys.argv[2:], fancy)

    if fancy:
        print("TOTAL: %s match(es)" % num)
