# 조교의 성적 매기기

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []
    # 입력된 성적을 바로 평균 점수를 내어서 학생 번호와 함께 추가
    for i in range(N):
        score = list(map(int, input().split()))
        scores.append([score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2, i + 1])
    # 평균 성적을 기준으로 정렬 
    scores.sort(reverse=True)
    scores_dict = {}
    per = N // 10
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # key는 학생 번호, value는 grade인 딕셔너리 제작
    for i in range(len(scores)):
        scores_dict[scores[i][1]]= grade[i // per] # 각 성적은 일정한 비율
    print(f'#{test_case} {scores_dict[K]}') 



