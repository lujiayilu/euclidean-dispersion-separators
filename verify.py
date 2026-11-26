"""Exact rational witnesses for the separation identity, standard Python 3."""
from itertools import combinations
from fractions import Fraction as F

def determinant(a):
    if not a:
        return 1
    return sum((-1)**j*x*determinant([r[:j]+r[j+1:] for r in a[1:]])
               for j,x in enumerate(a[0]) if x)

def bases(n, blocks):
    for support in combinations(blocks,n):
        rows=[[int(bool(b & (1<<i))) for i in range(n)] for b in support]
        det=determinant(rows)
        if not det:
            continue
        # inverse of the matrix with block incidence rows
        inv=[[F((-1)**(i+j)*determinant([row[:i]+row[i+1:]
              for k,row in enumerate(rows) if k!=j]),det)
              for j in range(n)] for i in range(n)]
        weights=[sum(row[j] for row in inv) for j in range(n)]
        if min(weights)>=0:
            yield support,inv,weights

def check(n,p,edges,eta,blocks,options):
    full=(1<<n)-1
    delta=F(1,10)
    e=[sum((u & b)==b for b in edges) for u in range(full+1)]
    cut=[sum(0<(u & b)<b for b in edges) for u in range(full+1)]
    rhs={b:delta*e[b]-eta/2 for b in blocks}
    def price(pr,b):
        return sum(x for i,x in enumerate(pr) if b>>i&1)
    for support,inv,weights in options:
        t=[sum(x*rhs[b] for x,b in zip(row,support)) for row in inv]
        if all(price(t,b)>=rhs[b] for b in blocks):
            break
    else:
        raise AssertionError('No complementary witnesses')
    certificate=sum(y*(delta*cut[b]+eta) for y,b in zip(weights,support))
    rewards=[t[i]-delta*cut[1<<i] for i in range(n)]+[-x for x in t]
    def score(s):
        value=sum(rewards[i] for i in s)
        for i,j in combinations(s,2):
            bonus=i//n==j//n and (1<<(i%n) | 1<<(j%n)) in edges
            value+=1+delta*bonus
        return value
    left=score(range(n))
    right=score(range(n,2*n))
    assert right-left==certificate
    for s in combinations(range(2*n),n):
        f=score(s)
        assert f<=right
        if sum(i>=n for i in s)<=p:
            assert f-left<=eta
    return 1

if __name__=='__main__':
    cases=0
    for n in range(2,5):
        all_edges=[(1<<i)|(1<<j) for i,j in combinations(range(n),2)]
        for p in range(1,n+1):
            blocks=[b for b in range(1,1<<n) if b.bit_count()<=p]
            options=list(bases(n,blocks))
            for mask in range(1<<len(all_edges)):
                edges={b for j,b in enumerate(all_edges) if mask>>j&1}
                for eta in [F(0),F(1,5)]:
                    cases+=check(n,p,edges,eta,blocks,options)
    print(cases,'exact rational instances passed')

