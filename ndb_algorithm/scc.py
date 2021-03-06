MAX = 10001

def double_arr(n, a):
    if a == None:
        return [[] for __ in range(n)]
    return [[a for _ in range(n)] for __ in range(n)]

d = [0]*MAX
int_id = 0
finished = [False]*MAX
a = double_arr(MAX, None)

SCC = []
stack = []

def dfs(n, int_id):
    int_id += 1
    d[n] = int_id
    stack.append(n)

    parent = d[n]
    for i in range(len(a[n])):
        y = a[n][i]
        if d[y] == 0:
            parent = min(parent, dfs(y, int_id))
        elif finished[y] == False:
            parent = min(parent, d[y])

    if parent == d[n]:
        tmp_arr = []
        while(1):
            t = stack.pop()
            tmp_arr.append(t)
            finished[t] = True
            if t == n:
                break
        SCC.append(tmp_arr)
    return parent

if __name__=="__main__":
    v = 11
    a[1].append(2)
    a[2].append(3)
    a[3].append(1)
    a[4].append(2)
    a[4].append(5)
    a[5].append(7)
    a[6].append(5)
    a[7].append(6)
    a[8].append(5)
    a[8].append(9)
    a[9].append(10)
    a[10].append(11)
    a[11].append(3)
    a[11].append(8)
    for i in range(1, v+1):
        if(d[i] == 0):
            dfs(i, int_id)
    print(SCC)