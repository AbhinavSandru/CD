#!/usr/bin/env python
# coding: utf-8

# In[13]:


from collections import defaultdict
keywords=['printf','int','return',]
specialsymbols=['{','}',';']
operators=['+','-','/','*','%']
file=open("test.txt")
text=file.readlines()
print(text)
line=0
token=-1
for i in text:
    print(i)
    line+=1
    i=i.strip()
    if i[0]=="#":
        token+=1
        print(line,"\t",token,"\t","Directive","\t",i)
    elif i[0]=="/" and (i[1]=="/" or i[1]=="*"):
        token+=1
        print(line,"\t",token,"\t","Comment","\t",i)
    else:
        i=i.split()
        for j in i:
            j=j.strip()
            print(j)
            st=[]
            for m in j:
                if m in operators:
                    token+=1
                    print(line,"\t",token,"\t","operator",m)
                elif m.isalpha() or m==",":
                    st.append(m)
                elif m=="(":
                    st.append(m)
                elif m==")":
                    temp=""
                    while st[-1]!="(":
                        temp+=st.pop()
                    temp=temp[::-1]
                    token+=1
                    if temp in keywords:
                        print(line,"\t",token,"\t","keyword","\t",temp)
                    else:
                        print(line,"\t",token,"\t","identifier","\t",temp)
                    st.pop()
                    temp=""
                elif m in specialsymbols:
                    token+=1
                    print(line,"\t",token,"\t","specialsymbols","\t",m)
            if st!=[]:
                temp=""
                while st!=[]:
                    temp+=st.pop()
                temp=temp[::-1]
                token+=1
                if temp in keywords:
                        print(line,"\t",token,"\t","keyword","\t",temp)
                else:
                    print(line,"\t",token,"\t","identifier","\t",temp)
                temp=""
            


# In[ ]:




