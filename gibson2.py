# Code to measure AT/GC content of primers
# and return calculated melting temperature 
# for Gibson homology cloning 

def stringcount(string):
    #count ATs and GCs
    AT = (string.count("A") 
          + string.count("a") 
          + string.count("T") 
          + string.count("t"))

    GC = (string.count("G") 
          + string.count("g") 
          + string.count("C") 
          + string.count("c"))
    print "sequence is " + string 
    
    length = AT + GC
    print "length is " + str(length)

    #calculate Tm
    tm = (AT * 2) + (GC * 4)
    print "Tm is " + str(tm)
    print
    return


# input primer sequences here
stringcount("acatcctccaggatgataaacg")
stringcount("tCTAGAGGATCAGAAAATTATCGCC")
stringcount("gatttaacAAAGCGACTATAAGTCAG")
stringcount("tCTAGAGGATCAGAAAATTATCGCC")