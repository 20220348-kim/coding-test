def solution(n):
    answer = str(n)
    
    result = list(answer)
    
    lens =len(result)
    
    score = 0 
    
    for i in range(lens) :
        score +=int(result[i])
    
    return score