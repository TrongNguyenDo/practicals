import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 1?
#Answer: I see number 8
# What was the smallest number you could have seen, what was the largest?
#Answer: number 5 is the smallest and 20 is the biggest
# What did you see on line 2?
#Answer: I see number 9
# What was the smallest number you could have seen, what was the largest?
#Answer: the smallest number is 3 , the largest is 9
# Could line 2 have produced a 4?
#Answer: No
# What did you see on line 3?
#Answer: I see 4.608913694268674
# What was the smallest number you could have seen, what was the largest?
#Answer: The smallest number is 2.5,the largest  number is 5.5
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
for i in range(0,100):
  print(random.randint(1, 100))