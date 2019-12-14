import fileinput
def strip(infile,outfile,removes):
     
    with open(infile) as oldfile, open(outfile, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in removes):
                newfile.write(line)
              
def main(inf,outf,strs):
    strip(inf,outf,strs)

if __name__ == "__main__":
    argCount = len(sys.argv)-1;
    if argCount > 2:
        main(sys.argv[1],sys.argv[2],sys.argv[3:])
    else:
        print("need to supply the file name,outfile, and strings to search for")



