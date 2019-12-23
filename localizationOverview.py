"""
Localization overview
"""
#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
# sensor accuracies on Hit and Miss
pHit = 0.6
pMiss = 0.2

#inaccurate movement probabilities
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
"""
in the limit, the above inaccuracy results in a uniform distribution of q since the 0.8 becomes
diluted, ie. to 0.64 and so on
Take the example of being in pos 4 or x4 at time t, which corresponds to position at time t-1
If U=3, then 0.8*x2, 0.1*x3 and 0.1*x1 and these multiplied by uniform distribution of 0.2 for x1 to x5
is also equal to 0.2.  Thus, it is the only solution in the limit
"""

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    """
    return the new location probs q after moving by U.
    param p: the old probabilities of location
    """
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)

    return q