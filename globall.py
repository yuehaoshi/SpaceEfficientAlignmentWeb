def calc_fix(v, w, delta):
    len1 = len(v)
    len2 = len(w)
    dp = [[0 for j in range(len1 + 1)] for i in range(2)]
    curr = 0
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i == 0 and j == 0:
                dp[curr][j] = 0
            elif i > 0 and j == 0:
                dp[curr][j] = dp[1 - curr][j] + delta['-'][w[i - 1]]
            elif i == 0 and j > 0:
                dp[curr][j] = dp[curr][j - 1] + delta[v[j - 1]]['-']
            else:
                l = dp[1 - curr][j] + delta['-'][w[i - 1]]
                u = dp[curr][j] = dp[curr][j - 1] + delta[v[j - 1]]['-']
                tl = dp[1 - curr][j - 1] + delta[w[i - 1]][v[j - 1]]
                dp[curr][j] = max(l, max(u, tl))
        curr = 1 - curr
    return dp[1 - curr]

def helper(v, w, delta, i0, j0, i1, j1, report):
    if j1 - j0 > 1:
        mid = int(j0 + (j1 - j0) / 2)
        prefix = calc_fix(v[i0:i1:], w[j0:mid:], delta)
        suffix = calc_fix(v[i0:i1:][::-1], w[mid:j1:][::-1], delta)
        istar = -1
        big = -1919810
        for i in range(len(prefix)):
           wt = prefix[i] + suffix[-1 - i]
           if big <= wt:
               big = wt
               istar = i
        report.append((istar + i0, mid))
        helper(v, w, delta, i0, j0, istar + i0, mid, report)
        helper(v, w, delta, istar + i0, mid, i1, j1, report)
    elif j1 - j0 == 1:
        report.append((i0, j0))
        report.append((i1, j1))
        return
    else:
        return

def global_dp(v, w, i0, j0, i1, j1, delta):
    s1 = v[max(0, i0 - 1):i1:]
    s2 = w[max(j0 - 1, 0):j1:]
    M = [[-1919810 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    pointers = [[(0, 0) for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1) + 1):
      for j in range(len(s2) + 1):
        if (i == 0 and j == 0):
          M[i][j] = 0
        if (i > 0):
          if M[i - 1][j] + delta['-'][s1[i - 1]] > M[i][j]:
            M[i][j] = M[i - 1][j] + + delta['-'][s1[i - 1]]
            pointers[i][j] = (i - 1, j)
        if (j > 0):
          if M[i][j - 1] + delta[s2[j - 1]]['-'] > M[i][j]:
            M[i][j] = M[i][j - 1] + delta[s2[j - 1]]['-']
            pointers[i][j] = (i, j - 1)
        if (i > 0 and j > 0):
          temp = delta[s1[i - 1]][s2[j - 1]] # 1 if (v[i - 1] == w[j - 1]) else -1
          if M[i - 1][j - 1] + temp > M[i][j]:
            M[i][j] = M[i - 1][j - 1] + temp
            pointers[i][j] = (i - 1, j - 1)
    ret = []
    x = len(s1)
    y = len(s2)
    while not pointers[x][y] == (x, y):
        if max(0, i0 - 1) + x >= 0 and max(0, j0 - 1) + y >= 0:
            ret.append((max(0, i0 - 1) + x, max(0, j0 - 1) + y))
        (temp1, temp2) = pointers[x][y]
        x = temp1
        y = temp2
    ret.append((i0, j0))
    return ret

def traceback_hirschberg(v, w, delta, report):
    path = []
    for i in range(len(report)):
        path.append(report[i])
        if i > 0 and report[i][0] - report[i - 1][0] > 1:
            temp = global_dp(v, w, report[i - 1][0], report[i - 1][1], report[i][0], report[i][1], delta)
            for vertex in temp:
                path.append(vertex)
    path = list(set(path))
    path.sort(key = lambda x: (x[0], x[1]))
    return path
                    

def hirschberg(v, w, delta):
    report = []
    helper(v, w, delta, 0, 0, len(v), len(w), report)
    report = list(set(report))
    report.sort(key = lambda x: (x[0], x[1]))
    # print(report)
    return traceback_hirschberg(v, w, delta, report)

def get_alignment(v, w, report):
    va = ""
    wa = ""
    for i in range(len(report)):
        (x, y) = report[i]
        if x > 0 or y > 0:
            (xp, yp) = report[i - 1]
            if x == xp + 1 and y == yp + 1:
                va += v[x - 1]
                wa += w[y - 1]
            elif y == yp + 1:
                va += '-'
                wa += w[y - 1]
            else:
                va += v[x - 1]
                wa += '-'
    return (va, wa)

keys = ['A', 'C', 'T', 'G', '-']
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}

v = "TTCA"
w = "T"
temp = hirschberg(v, w, delta)
"""
print(temp)
print(get_alignment(v, w, temp))
"""

def main(v, w, delta):
    h = hirschberg(v, w, delta)
    a1, a2 = get_alignment(v, w, h)
    return a1, a2, h