# creating function
def score_words(words:list) -> int:
    
    # create internal list of vowels
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    
    # initialize score
    score = len(words)
    
    for w in words:
        # filter the vowels in the word
        vowels_in_w = list(filter(lambda x: x in VOWELS, w)) 
        
        # add +1 score for words with even nr. of vowels
        if len(vowels_in_w) % 2 == 0:
            score += 1 
    
    return score

    
# read inputs
n = int(input())
words= input().split()

# compute and print score
score = score_words(words)
print(score)
