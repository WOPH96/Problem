def solution_pre(id_list, report, k):
    answer = []
    ban_list_temp= []
    for_mail = []
    ban_list= []
    count=0

    for id in id_list:
        st = set()
        for people in report:
            reporter, reported = people.split(" ")
            if id == reporter:
                st.add(reported)
            
        ban_list_temp.extend(st)
        for_mail.append(st)

    #print(for_mail)#,for_mail)

    for id in id_list:
        for ban in ban_list_temp:
            if id == ban :
                count +=1
            if count == k:
                ban_list.append(id)
                count+=1
                #print(id)
        count=0
    #print("BAN = ",ban_list)


    #ban_list 멤버가 For_mail list안에 몇개가 있는지 answer에 저장
    
    for direction in for_mail:
        for ban in ban_list:
            if ban in direction:
                count += 1
        answer.append(count)
        count =0
        
    #print(answer)
            
        
        
    
    return answer

# 딕셔너리 사용 후 최대 2441
def solution(id_list,report,k):
    answer =[]
    reporting = []
    banned = []

    dic = {}
    for i in range(len(id_list)):
        dic[id_list[i]] = i
    #print(dic)

    for i in range(len(id_list)):
        reporting.append([])
        banned.append(0)
    # print(reporting)
    # reporting[0].append('frodo')
    ban_list=[]

    for repo in report :
        speaker, target = repo.split(" ")
        #dictuionary 사용가능
        idx = dic[speaker]
        if target not in reporting[idx] : 
            reporting[idx].append(target)

    #print(reporting)

    for bans in reporting :
        for ban in bans:
            idx = dic[ban]
            banned[idx]+=1
    for i in range(len(banned)):
        if banned[i]>=k:
            ban_list.append(i)

    for repo in reporting:
        #print(repo)
        cnt=0
        for bl in ban_list:
            #print(bl)
            if id_list[bl] in repo:
                cnt+=1
        answer.append(cnt)
    #print(answer)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	,2))	#[2,1,1,0])
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"]	,3))#	[0,0]


# **** dictionary 사용 안했을 때 => 최대 6441ms 

# def solution(id_list,report,k):
#     answer =[]
#     reporting = []
#     banned = []
#     for i in range(len(id_list)):
#         reporting.append([])
#         banned.append(0)
#     # print(reporting)
#     # reporting[0].append('frodo')
#     ban_list=[]

#     for repo in report :
#         speaker, target = repo.split(" ")
#         #dictuionary 사용가능
#         idx = id_list.index(speaker)
#         if target not in reporting[idx] : 
#             reporting[idx].append(target)

#     #print(reporting)

#     for bans in reporting :
#         for ban in bans:
#             idx = id_list.index(ban)
#             banned[idx]+=1
#     for i in range(len(banned)):
#         if banned[i]>=k:
#             ban_list.append(i)

#     for repo in reporting:
#         #print(repo)
#         cnt=0
#         for bl in ban_list:
#             #print(bl)
#             if id_list[bl] in repo:
#                 cnt+=1
#         answer.append(cnt)
#     #print(answer)
#     return answer