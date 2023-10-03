############## Bonus Uygulama - List Comprehension ###########################

#1 Write a list comprehension that generates a list of all possible substrings of a given string.
string = "myth"
# ['m', 'my', 'myt', 'myth', 'y', 'yt', 'yth', 't', 'th', 'h']
len(string)



sub_string =[]
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
       sub_string.append(string[i:j])