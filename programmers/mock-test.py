"""
name: Lee Minji
date :2022.06.02
problem: programmers brute Force mock test
explain: 모든 문제에 대해서 각 학생들의 답을 확인하는 방식으로 진행하였습니다.
<<<<<<< HEAD
주어진 답의 길이가 n이라고 했을 때, O(n)이라고 볼 수 있습니다. 
=======
주어진 답의 길이가 n이라고 했을 때, O(n)이라고 볼 수 있습니다.
>>>>>>> 31375eb35b47fc5bec0a210766f26f4dd1da1965
"""

def solution(answers):
    len_ans = len(answers)
    student1 = [1, 2, 3, 4, 5]  # 각 학생들의 정답 패턴
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [[1, 0], [2, 0], [3, 0]]
<<<<<<< HEAD

=======
    
>>>>>>> 31375eb35b47fc5bec0a210766f26f4dd1da1965
    #정답확인
    for i in range(len_ans):
        if student1[i % 5] == answers[i]:
            count[0][1] += 1
        if student2[i % 8] == answers[i]:
            count[1][1] += 1
        if student3[i % 10] == answers[i]:
            count[2][1] += 1
    
    #순서정렬
    count.sort(reverse=True, key=lambda x: x[1])
    answer = []
    
    #가장 많이 맞힌 학생 추출
    answer.append(count[0][0])
    for i in range(2):
        if count[i][1] == count[i + 1][1]:
            answer.append(count[i + 1][0])
        else:
            break
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
