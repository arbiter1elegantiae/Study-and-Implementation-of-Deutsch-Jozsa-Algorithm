#Author:Federico Peconi
#Synopsis: This script can be used to the search for balanced linear Boolean functions.
# The range(that can be adapt on whatever the goal is) on the outer loop, it is meant to find a general structure (at least as many functions as the dimension of it)

# Note: this program, in practice, is not usefull at all since, like explained on chapter 1 of 'thesis' file, every linear B. function
# is also balanced (with the exclusion for constant 0 function).

c = [1,0,1,0]
for i in range(5,6):
    c_i = 1
    n_1 = 0
    n_0 = 0
    
    maxInp = int(pow(2,i))
    for j in range(maxInp):
        
        dimInp = '{0:0%db}'%i
        inp = tuple(map(int,tuple(dimInp.format(j))))
        output = 0
        
        for t in range(i-1):
            output = output + (c[t]*inp[(i-1)-t])
        output = (output + (c_i*inp[0])) % 2

        if output == 0:
            n_0 = n_0 +1
        else:
            n_1 = n_1 +1

    if n_0 == n_1:
        c.append(c_i)
        
    else:
        c.append(0) 

print(c)