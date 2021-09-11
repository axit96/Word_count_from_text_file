def freqcount(filepath, N=3):
    f = open(filepath,'r',encoding='utf8')
    data = f.read()
    temp = list(data)
    for i in range(len(temp)):
        if ((temp[i]>='a' and temp[i]<='z') or (temp[i]>='A' and temp[i]<='Z') or temp[i]==" "):
            continue
        else:
            temp[i] = str(' ')
    data = "".join(temp)
    wordlist = data.split()
    mydict= {}
    for i in range(len(wordlist)):
        mydict[wordlist[i]] = wordlist.count(wordlist[i])
    print("Most frequent:")
    print(dict(sorted(mydict.items(),key=lambda x:x[1])[-int(N):]))
    print("Least frequent:")
    print(dict(sorted(mydict.items(),key=lambda x:x[1])[:int(N)]))

def main():
    N = input("Enter how many words you want to see: ")
    freqcount("word_freq_input1.txt",N)

if __name__ == "__main__":
    main()