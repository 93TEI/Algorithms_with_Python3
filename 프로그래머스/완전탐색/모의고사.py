# 모의고사

def solution(answers):
    answer = []
    # 1,2,3번 수포자를 for문으로 미리 만들어서 비교할 생각
    n1 = []
    n2 = []
    n3 = []
    temp = 0
    n1_cnt = 0
    n2_cnt = 0
    n3_cnt = 0
    
    # n1 리스트 만들기
    for i in range(len(answers)) :
        if (i+1)%5 == 0 :
            temp += 1
        n1.append(i+1-(temp*5))
    
    temp = 1
    # n2 리스트 만들기
    for i in range(len(answers)):
        if (i+1)%2 == 1 :
            n2.append(2)
        else :
            if temp == 6 :
                temp = 1
            n2.append(temp)
            temp += 1
    
    # n3 리스트 만들기
    for i in range(len(answers)) :
        if (i+1)%10 == 1 or (i+1)%10 == 2 :
            n3.append(3)
        elif (i+1)%10 == 3 or (i+1)%10 == 4 :
            n3.append(1)
        elif (i+1)%10 == 5 or (i+1)%10 == 6 :
            n3.append(2)
        elif (i+1)%10 == 7 or (i+1)%10 == 8 :
            n3.append(4)
        else :
            n3.append(5)
    
    # 각각 수포자들이 몇개 맞았는지 확인
    for i in range(len(answers)) :
        if answers[i] == n1[i] :
            n1_cnt += n1_cnt + 1
        if answers[i] == n2[i] :
            n2_cnt += n2_cnt + 1
        if answers[i] == n3[i] :
            n3_cnt += n3_cnt + 1
    
    # 리스트화 시키고 max를 뽑아냄    
    n_cnt = [n1_cnt, n2_cnt, n3_cnt]
    max_cnt = max(n_cnt)
    
    # max와 같은 값을 가진 수포자를 answer 리스트에 append
    for i in range(3) :
        if max_cnt == n_cnt[i] :
            answer.append(i+1)
    
    # 2명 이상일 경우 오름차순 정렬
    if len(answer) >1 :
        answer.sort()
    return answer