y = input("")
def most_frequent(x):
  dict={}

  for i in x:
    keys =dict.keys()
    if i not in keys:
      dict[i]=1
      
    else :
      dict[i]=dict[i]+1
  return dict
   

dictionary = most_frequent(y)

sorted_dict = {}
sorted_keys = reversed(sorted(dictionary, key=dictionary.get))  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dictionary[w]

g =sorted_dict

print("Input : Please Enter a string :",y)
print("Output : {}".format(g))
