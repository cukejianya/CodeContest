def stringPractice(str):
    for elm in list("![,?.\_\'@+]"):
        str = str.split(elm)
        str = " ".join(str)
    str = str.split()
    print len(str)
    print "\n".join(str)

stringPractice(raw_input());
