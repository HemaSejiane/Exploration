import sys

def comparefilematching(inputfile1, inputfile2):
    with open(inputfile1,"r") as file1:
        with open(inputfile2,"r") as file2:
            matching= set(file1).intersection(file2)
    matching.discard('\n')

    with open(outputfilematching,"w") as file3:
        for line in matching:
            file3.write(line)


def comparefiledifference(inputfile1,inputfile2):
    with open(inputfile1,"r") as file1:
        with open(inputfile2,"r") as file2:
            difference_data= set(file1).difference(file2)
    difference_data.discard('\n')
    
    with open(outputfiledifference,"w") as file3:
        for line in difference_data:
            file3.write(line)


if __name__ == '__main__':
    inputfile1=sys.argv[1]
    inputfile2=sys.argv[2]
    outputfilematching=sys.argv[3]
    outputfiledifference=sys.argv[4]
    comparefilematching(inputfile1, inputfile2)
    comparefiledifference(inputfile1,inputfile2)


