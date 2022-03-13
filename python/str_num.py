def solution(s):
    answer = 0
    
    dic = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
    }
    for word in dic.keys():
        while True:
            idx = s.find(word)
            if idx == -1: break
            s = s[:idx]+str(dic[word])+s[idx+len(word):]
    answer = int(s)        
    return answer