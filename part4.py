import time

def trialdivision(num):
    i = 1
    while(i<=num):
        k=0
        if(num%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                print(i)
        i=i+1

def main():
    start_time = time.time()
    userinput = 23216544
    trialdivision(userinput)


if __name__ == '__main__':
    main()
