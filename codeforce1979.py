from itertools import groupby

def sumcheck(n,k,lst):
    sm = sum(lst)
    if n == k and (sum(lst) == 0 or sum(lst) == n):
        return 1
    if (n/k)%2 == 0:
        if sm != n/2:
            return 0
    if (n/k)%2 == 1:
        if (sm == int((n/(2*k))+0.5)) or (sm == int((n/(2*k))-0.5)):
            return 1
        else:
            return 0
    else:
        return 1
    
def grpch(k,lst):
    res = [list(y) for x, y in groupby(lst)]
    if lst[0] == lst[-1]:
        res[-1]=res[-1]+res[0]
        res.pop(0)
    list_len = [len(i) for i in res]
    if min(list_len) < k or max(list_len) > k:
        return 0
    else: 
        return 1
    
    #NEED TO CHECK FOR IF GROUPS OF 0 are size k 
    #12 3
    #111000100011 passes because 0 groups are size k

def psplit(p,lst):
    a = lst[:p]
    b= lst[p:]
    a.reverse()
    c = b+a
    return c

def setup(cases):
    lists = []
    for i in range(cases):
        lists.append([])
    return lists

def div_chk(k, lst):
    for i in range(0, len(lst), k):  
        yield lst[i:i + k] 

def check(lst, k, n):
    if (n/2)%2:
        z = list(div_chk(2,lst))
        if z[0] != z[1]:
            return 0
    x = list(div_chk(k,lst))
    for c in x:
        if sum(c) == k or sum(c) == 0:
            continue
        else:
            return 0
    for i in range(int((n/k)-1)):
        if sum(x[i]) == sum(x[i+1]):
            return 0
    return 1
        

cases = int(input())
lists = setup(cases)

for i in range(cases):
    st = str(input())
    st2 = str(input())
    lst = [int(x) for x in st.split()]
    binstr = [int(x) for x in list(st2)]
    lists[i].append(lst)
    lists[i].append(binstr)

for i in range(cases):
    n = lists[i][0][0]
    k = lists[i][0][1]
    lst = lists[i][1]
    if grpch(k,psplit(lst)) == 0:
        print(-1)
    else:
        for j in range(len(lst)):
            lst2 = psplit(j, lst)
            res = check(lst2,k,n)
            if res == 1:
                if j == 0:
                    print(n)
                else:
                    print(j)
                break
            elif j+1 == len(lst):
                print(-1)