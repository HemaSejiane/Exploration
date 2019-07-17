Write a function that returns the elements on odd positions (0based) in a list
 
def oddlist(inputlist):
                return [ y for x,y in enumerate(inputlist) if x%2 ==1]
               
def solution2(input):
    return [input[i] for i in range(len(input)) if i % 2 != 0]
               
Write a function that returns the cumulative sum of elements in a list
 
def cumsum(inputlist):
                sum=0
                output=[]
                for i in inputlist:
                                sum +=i
                                output.append(sum)
                return output
               
Write a function that takes a number and returns a list of its digits
 
def convertlist(inputvalue):
                output=[]
                x = str(inputvalue)
                for i in x:
                                output.append(int(i))
                return output
 
Write a function that takes list and returns element that that occurs more than once
 
def checkdups(input):
                d = {}
                for elem in input:
                                if elem in d:
                                                d[elem] += 1
                                else:
                                                d[elem] = 1
                return [key for key,value in d.items() if value > 1]
 
def solution2(input):
    seen = set()
    dups = set()
    for i in input:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)
    return list(dups)
               
Given a non-negative integer, add the digits until it become a one digit integer
 
#No appropriate solution found
 
Given a sorted list if integers, remove any duplicates that occur more than twice.
 
def removedups(input):
                cnt=0
                for i in input:
                                if
