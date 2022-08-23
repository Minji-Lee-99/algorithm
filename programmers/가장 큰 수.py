def comparison(a, b):
    a = str(a)
    b = str(b)
    k = 0
    while(True): # O(3)
        try:
            if a[k] < b[k]:
                return int(b)
            elif a[k] > b[k]:
                return int(a) 
            else:
                k+=1
        except:
            len_a = len(a)
            len_b = len(b)
            if len_a > len_b:
                a_2 = a[len_b: len_a]
                if str(comparison(a_2, b)) == a_2:
                    return int(a)
                else:
                    return int(b)
            elif len_a < len_b:
                b_2 = b[len_a: len_b]
                if str(comparison(a, b_2)) == b_2:
                    return int(b)
                else:
                    return int(a)
            else:
                return int(a)
            
def left(index):
    return (index+index)+1

def right(index):
    return index*2+2

def switch(ls, index1, index2):
    ls[index1], ls[index2] = ls[index2], ls[index1]

def heapify(ls, index):
    l = left(index)
    r = right(index)
    while(l < len(ls)):
        big = l
        if r < len(ls) and comparison(ls[l], ls[r]) == ls[r]:
            big = r
        if comparison(ls[big], ls[index]) == ls[big]:
            switch(ls, index, big)
            index = big
            l = left(index)
            r = right(index)
        else:
            return
    return ls

def solution(numbers):
    answer = ''
    for i in range(len(numbers)//2, -1, -1):
        heapify(numbers, i)
    for i in range(len(numbers)):
        switch(numbers, 0, len(numbers)-1)
        m = numbers.pop()
        answer += str(m)
        heapify(numbers, 0)
    return str(int(answer))





'''def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        m = numbers[0]
        for j in range(1, len(numbers)):
            m = comparison(m, numbers[j])
        numbers.remove(m)
        answer += str(m)
    return answer

def comparison(a, b):
    a = str(a)
    b = str(b)
    k = 0
    while(True): # O(3)
        try:
            if a[k] < b[k]:
                return int(b)
            elif a[k] > b[k]:
                return int(a) 
            else:
                k+=1
        except:
            len_a = len(a)
            len_b = len(b)
            while(True):
                if len_a > len_b:
                    while(k<len_a):
                        if a[k] > b[len_b-1]:
                            return int(a)
                        elif a[k] < b[len_b-1]:
                            return int(b)
                        else:
                            k+=1
                    return int(b)
                elif len_a < len_b:
                    while(k <len_b):
                        if a[len_a-1] < b[k]:
                            return int(b)
                        elif a[len_a-1] > b[k]:
                            return int(a)
                        else:
                            k+=1
                    return int(a)
                else:
                    return int(a)'''


'''def comparison(a, b):
    a = str(a)
    b = str(b)
    k = 0
    while(True):
        try:
            if a[k] < b[k]:
                return int(b)
            elif a[k] > b[k]:
                return int(a) 
            else:
                k+=1
        except:
            if len(a) > len(b):
                if a[k] > b[k-1]:
                    return int(a) 
                else:
                    return int(b)
            elif len(a) < len(b):
                if a[k-1] < b[k]:
                    return int(b)
                else:
                    return int(a)
            else:
                return int(a)'''
