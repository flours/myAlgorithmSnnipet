# ここでfの最小値を求めるものとする
def TemarySearch(f,L,R):
    while R-L>0.1:
        c1=(L*2+R)/3
        c2=(L+R*2)/3
        if f(c1)>f(c2):
            L=c1
        else:
            R=c2
    return R/2+L/2


def ABC279D():
    A,B=map(int,input().split())

    import math
    def f(g):
        ret=g*B-B
        ret+=A/math.sqrt(g)
        return ret

    ret=int(TemarySearch(f, 1, 10**18))
    print(min(f(ret),f(max(ret-1,1)),f(ret+1)))
