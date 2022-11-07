def solution(array, commands):
    answer = []
    for ls in commands:
        sub_ls = array[(ls[0]-1):ls[1]]
        sub_ls.sort()
        answer.append(sub_ls[(ls[2]-1)])
    return answer


def solution(array, commands):
    answer = []
    for command in commands:
        s, e, k = command
        temp = sorted(array[s - 1: e])
        answer.append(temp[k - 1])
    return answer


