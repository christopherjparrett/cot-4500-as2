
#nevilles method
def nevilles(inputed,w):
    neville = [[0 for _ in range(len(inputed[0]))] for _ in range(len(inputed[0]))]
    #inputed[0] = x array
    #inputed[1] =  val array
    for i in range(0,len(inputed[0])):
        neville[i][0] = inputed[1][i]
    for i in range(0,len(inputed[0])):
        for j in range(1,i+1):
            term1 = (w-inputed[0][i-j]) * neville[i][j-1]
            term2 = (w-inputed[0][i]) * neville[i-1][j-1]
            neville[i][j] = (term1-term2)/(inputed[0][i]-inputed[0][i-j])
    # for i in range(0,len(inputed[0])):
    #     for j in range(i+1):
    #         print(f"{neville[i][j]} ",end="")
    #     print()
    print(neville[len(inputed[0])-1][len(inputed[0])-1])

def NewtonForward(inputed):
    lim  = len(inputed[0])
    diffs = [[0 for _ in range(lim)] for _ in range(lim)]
    for i in range(lim):
        diffs[i][0] = inputed[1][i]
    for i in range(1,lim):
        for j in range(1,i+1):
            diffs[i][j] = (diffs[i][j-1] - diffs[i-1][j-1])/(inputed[0][i]-inputed[0][i-j])

    # for i in range(lim):
    #     for j in range(i+1):
    #         if(diffs[i][j] >=0):
    #             print(" ",end="")
    #         print(f"{diffs[i][j]:.7f} ", end="")
    #     print()
    returnTable = [0 for _ in range(lim)]
    for i in range(1,lim):
        print(f"{diffs[i][i]}")
        returnTable[i] = diffs[i][i]
    return(returnTable)
    

def dividedDiff(inputed,d):
    x=inputed[0]
    f=inputed[1]
    f_prime = inputed[2]
    n = len(x)
    dn = n*2
    # Create a table for divided differences, initializing with zeroes
    table = [[0] * (2 * n+1) for _ in range(2 * n+1)]
    #fill in first row of table
    for i in range(n):
        table[2*i][0] = x[i]
        table[2*i+1][0] = x[i]
        table[2*i][1] = f[i]
        table[2*i+1][1] = f[i]
        table[2*i+1][2] = f_prime[i]
        if(i!=0):
            # print(f"doing  324: ({table[2*i][1]} - {table[2*i-1][1]})/({table[2*i][0]} - {table[2*i-1][0]})")
            table[2*i][2] = (table[2*i][1] - table[2*i-1][1])/(table[2*i][0] - table[2*i-1][0])

    # print(dn)
    for i in range(3,dn+1):
        # print(f"i:{i}")
        for j in range(dn-i+1):
            # print(f"j:{j}")
            tempTable = [[0] for _ in range(i)]
            for z in range(j,i+j):
                tempTable[z-j] = table[z][0]
            #print(f"doing : ({table[j+i-1][i-1]}-{table[j+i-2][i-1]})/({table[j+i-1][i-2]}-{table[j+i-2][0]})")
            table[j+i-1][i] = (table[j+i-1][i-1]-table[j+i-2][i-1])/(max(tempTable) - min(tempTable))
    

    #print table
    for i in range(n*2):
        print("[",end="")
        for x in range(d+2):
            print(f" {table[i][x]:.8e}",end="")
        print("]")
    

def CubicSpline(inputed):
    x= inputed[0]
    f = inputed[1]
    n = len(x)
    h = [0 for _ in range(n)]
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
    array = [[0 for _ in range(n)] for _ in range(n)]

    #first row is 1,0,0,0, etc
    array[0][0]=1
    array[n-1][n-1] = 1

    for i in range(1,n-1):
        array[i][i-1] = h[i-1]
        array[i][i] = 2*(h[i-1]+h[i])
        array[i][i+1] = h[i]
    
    for i in range(n):
        print("[",end="")
        for j in range(n):
            print(f" {array[i][j]}.",end="")
        print("]")
    #now we make b
    b = [0 for _ in range(n)]
    for i in range(1,n-1):
        b[i] = (3/h[i])*(f[i+1]-f[i+0]) - (3/h[i-1])*(f[i]-f[i-1])
    print(b)
    mu = [0 for _ in range(n)]
    l= [0 for _ in range(n)]
    l[0] = 1
    z = [0 for _ in range(n)]
    c=[0 for _ in range(n)]
    d=[0 for _ in range(n)]
    for i in range(1,n-1):
        l[i] = 2*(x[i+1]-x[i-1])-(h[i-1]*mu[i-1])
        mu[i] = h[i]/l[i]
        z[i] = (b[i]-h[i-1]*z[i-1])/l[i]
    l[n-1] =1
    z[n-1] =0
    c[n-1] =0
    for temp in range(n-2,-1,-1):
        c[temp] = z[temp] - (mu[temp]*c[temp+1])
        b[temp] = (f[temp+1]-f[temp])/h[temp]-h[temp]*(c[temp+1]+2*c[temp])/3
        d[temp] = (c[temp+1]-c[temp])/(3*h[temp])
    print("[",end="")
    for i in range(n):
        print(f" {c[i]:.8f}",end="")
    print("]")




#run functions

#nevilles 
nevillesInputFromFiles = [[1,1.3,1.6,1.9,2.2],[.7651977,.6200860,.4554022,.2818186,.1103623]]
# nevilles(nevillesInputFromFiles,1.5)
#newton
# NewtonForward(nevillesInputFromFiles)

nevilleInput = [[3.6,3.8,3.9],[1.675,1.436,1.318]]
nevilles(nevilleInput,3.7)
print()
NewtonInput = [[7.2,7.4,7.5,7.6],[23.5492,25.3913,26.8224,27.4589]]
output = NewtonForward(NewtonInput)
print()
#3
firstterm = 23.5492
secondterm = (7.3-7.2)*output[1]
thirdterm = (7.3-7.2)*(7.3-7.4)*output[2]
fourthterm = (7.3-7.2)*(7.3-7.4)*(7.3-7.5)*output[3]
print(firstterm+secondterm+thirdterm+fourthterm)
print()

dividedDiffInput = [[3.6,3.8,3.9],[1.675,1.436,1.318],[-1.195,-1.188,-1.182]]
# dividedDiffInput = [[1.3,1.6,1.9],[.6200860,.4554022,.2818186],[-.5220232,-.5698959,-.5811571]]
dividedDiff(dividedDiffInput,3)
print()

#cubicSpline
cubicInput = [[2,5,8,10],[3,5,7,9]]
CubicSpline(cubicInput)