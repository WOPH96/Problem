def solution(id_list, report, k):
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


#solution(["muzi", "frodo", "apeach", "neo"]	,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	,2)	#[2,1,1,0])
#solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"]	,3)#	[0,0]