def solution(triangle, x=0, y=0, note = {}):
    if (x, y) in note:
        return note[(x, y)]
    target = triangle[x][y]
    if x+1 == len(triangle):
        return target
    num1 = target + solution(triangle, x+1, y, note)
    num2 = target + solution(triangle, x+1, y+1, note)
    if num1 >= num2:
        answer = num1
    else:
        answer = num2
    note[(x, y)] = answer
    return answer
    
    
    
    
#def solution(triangle, note = {}):    
    #if  in note:
    #    return note[(len(triangle), triangle[0][0]+triangle[-1][0]+triangle[-1][-1])]
    #target = triangle[0][0]
    #if len(triangle) == 1:
    #    return triangle[0][0]
    #L = left(triangle)
    #R = right(triangle)
    #num1 = target + solution(L)
    #num2 = target + solution(R)
    #if num1 >= num2:
    #    answer = num1
    #else:
    #    answer = num2
    #note[] = answer
    #return answer

#def left(triangle):
#    triangle = triangle[1:]
#    for i in range(len(triangle)):
#        triangle[i] = triangle[i][:-1]
#    return triangle
#def right(triangle):
#    triangle = triangle[1:]
#    for i in range(len(triangle)):
#        triangle[i] = triangle[i][1:]
#    return triangle
