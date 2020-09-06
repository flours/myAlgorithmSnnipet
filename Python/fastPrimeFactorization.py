
def gen_factorization(N):
    tables=[-1]*(N+1)
    for i in range(2,N):
        if tables[i]!=-1:continue
        tmp=i
        while tmp<=N:
            tables[tmp]=i
            tmp+=i
    def fuctorization(n):
        if n==1:return {}
        elif n<0:n=abs(n)
        elif n>N:return "error"
        ans={}
        while n!=1:
            tmp=tables[n]
            #debug print
            #print(tmp,n)
            ans.setdefault(tmp,0)
            ans[tmp]+=1
            n//=tmp
        return ans
    return fuctorization

if __name__=='__main__':
    f=gen_factorization(10**6)
    print(f(12))
    print(f(12345))
    print(f(10**6))
    print(f(13234))
    print(f(9999))
