n = int(input())
ls: list[int] = []
rs: list[int] = []
for i in range(n):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)
def check(lst):
    str_list = "".join([str(element) for element in lst])
    c0 = str_list.count("0")
    c1 = str_list.count("1") 
    if c0 > c1:
        return c1
    else:
        return c0
need_l = check(ls)
need_r = check(rs)
print(need_l+need_r)
