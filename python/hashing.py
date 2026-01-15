freq = {}
# or
from collections import defaultdict
freq = defaultdict(int)

#simplest
# check if array has duplicates
# x in seen -> O(1)
#sets don't store duplicates
#order does not matter
# -> Complexity
#   Time: O(n)
#   Space: O(n)
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

#First repeated character in a string
def first_repeat(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

#Manual map
#freq = {}
#for x in nums:
#    if x in freq:
#        freq[x] += 1 
#    else: 
#        freq[x] = 1

#clean (preferred)
#from collections import defaultdict
#freq = defaultdict(int)
#for x in nums:
#    freq[x] += 1

#Rule of Thumb
# If I write: `if key in dict:`
# should be using defaultdict(int)

#Example 3: most frequent element
def most_frequent(nums):
    from collections import defaultdict
    freq = defaultdict(int)

    for x in nums:
        freq[x] += 1

    best = nums[0]
    for x in freq:
        if freq[x] > freq[best]:
            best = x

    return best

#example 4: valid anagram
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    from collections import defaultdict
    freq = defaultdict(int)

    for ch in s:
        freq[ch] += 1

    for ch in t:
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True
#This works because:
# same letters -> counts cancel to zero
# early exit if something goes negative.

#Counter (shortcut)
from collections import Counter
Counter("anagram") == Counter("nagaram")

#Practic
def firstUnique(s: str) -> int:
    #return index of first non repeating character, or -1
   seen = set()
   for ch in s:
        if ch in seen:
            return int