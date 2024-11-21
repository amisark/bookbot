def count_words(booktext):
    words = booktext.split()
    print(len(words), "words found in the document")
    return

def count_chars(booktext):
    lc_alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphadict = {}
    for c in lc_alpha :
        alphadict[c] = 0
    others = 0
    words = booktext.lower().split()
    for lword in words :
        for wchar in lword :
            if wchar in alphadict :
                alphadict[wchar] += 1
            else :
                others += 1

#    for achar in alphadict :
#        print(achar, alphadict[achar])
    
    nchars = {}
    for achar in alphadict :
        nchars[alphadict[achar]] = achar

    for nchar in sorted(nchars.keys(), reverse=True) :
        print("The", nchars[nchar], "character was found", nchar, "times")
    print("Others", others)
    
    return


def main(path_to_file):
    print("--- Begin report of", path_to_file, "---")
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        count_words(file_contents)
        count_chars(file_contents)

    print("--- End Report ---")

if __name__ == "__main__" :
    path_to_file = "books/frankenstein.txt"
    main(path_to_file)
