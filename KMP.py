# LC 28---

def calLps(st):

    lps=[0]*len(st)
    for idx in range(1,len(st)):

        previdx=lps[idx-1]
        while previdx>0 and st[idx]!=st[previdx]:
            previdx=lps[previdx-1]
        
    
        lps[idx]=(previdx+(1 if st[idx]==st[previdx] else 0))

    return lps

def LPS(hay,needle):

    st=needle+'#'+hay
    # lps=calLps(st)
    # st='abcaabcaab'
    lps=calLps(st)
    print(lps)

    for idx,val in enumerate(lps):

        if val==len(needle):
            ogidx=idx-(2*len(needle))
            return ogidx
    return -1

print(LPS("1001100","0011"))



# similar qsts

# LC 3006,3008

