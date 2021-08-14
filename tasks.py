# x = 123
# result = 0
#
# while x > 0:
#     rem = x % 10
#     result *= 10
#     result += rem
#     x //= 10
#
# print(result)
# a = 123 % 10
# b = 0 * a
# print(a)
# a = "11111"
# if len(set(a)) == 1:
#     print("same")
# else:
#     print("not same")
# word = "friend"
# sentence = "Hello darkness my old friend friend"
# i = 0
# while i < len(sentence):
#     j = 0
#     while j < len(word):
#         if word[j] == sentence[i]:
#             i += 1
#             j += 1
#     else:
#         break
# else:
#     i += 1
lst_1 = [1, 2, 3]
print(lst_1[::-1])