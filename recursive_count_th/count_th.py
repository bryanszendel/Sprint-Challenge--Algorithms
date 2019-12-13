'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  normalized = list(word.lower())
  print(normalized, len(normalized))
  cache = 0
  n = len(normalized)
  def cache_inner(word):
    nonlocal cache
    nonlocal normalized
    if len(word) == 0: 
      return 0
    if len(word) == 1: 
      return 1
    # print('NORM TOP', normalized)
    # print('WORD TOP', word)
    subString = word[0:2]
    # ''.join(subString)
    print('SUB', word)
    if word[0] == 't' and word[1] == 'h':
      cache += 1
      newNormal = word[1:len(word)]
      print('NORM', newNormal)
      print('CACHE', cache)
      cache_inner(newNormal)
    else:
      newNormal = word[1:len(word)]
      cache_inner(newNormal)
    return cache
  return cache_inner(normalized)

print(count_th('THtHThth'))