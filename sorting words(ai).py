
gven_str = "Hello this is btechgeeks"
# Split the given string into list of words using the split() function and store
# it in another variable say "wrd_lst".
wrd_lst = gven_str.split()
# Sort the above obtained word list using the sort() method.
wrd_lst.sort()
# Loop in the above list "wrd_lst" using the for loop.
print("The all sorted words of given sentence in Alphabetic order :")
for wrd in wrd_lst:
  # Print the iterator value to sort all words in a given sentence in alphabetic order.
    print(wrd)
