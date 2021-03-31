from ps3 import *

#
# Test code
#

# def test_get_word_score():
#     """
#     Unit test for get_word_score
#     """
#     failure=False
#     # dictionary of words and scores
#     words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
#               ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
#               ("fork", 7):209, ("FORK", 4):308}
#     for (word, n) in words.keys():
#         score = get_word_score(word, n)
#         if score != words[(word, n)]:
#             print("FAILURE: test_get_word_score()")
#             print("\tExpected", words[(word, n)], "points but got '" + \
#                   str(score) + "' for word '" + word + "', n=" + str(n))
#             failure=True
#     if not failure:
#         print("SUCCESS: test_get_word_score()")

# # end of test_get_word_score

# word_list = load_words()
# print("----------------------------------------------------------------------")
# print("Testing get_word_score...")
# test_get_word_score()

# def test_wildcard(word_list):
#     """
#     Unit test for is_valid_word
#     """
#     failure=False
    
#     # test 3
#     hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
#     word = "h*ney"

#     if not is_valid_word(word, hand, word_list):
#         print("FAILURE: test_is_valid_word() with wildcards")
#         print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

#         failure = True
        
#     if not failure:
#         print("SUCCESS: test_wildcard()")

word_list = load_words()
# print("Testing wildcards...")
# test_wildcard(word_list)
* o u w h y e
hand = {"o":1,"u":1,"w":1,"h":1,"*":1,"y":1,"e":1}
play_hand(hand, word_list)