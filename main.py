from random import randint

def d(a=20, p='='):
    if p == '+':
        return max(randint(1, a), randint(1, a))
    elif p == '-':
        return min(randint(1, a), randint(1, a))
    return randint(1, a)

def shoot(kd, kz, ap, dmgList, mod=0, otdMod=0, adv='=', hrup=1):
    D = 0
    dd = d(20, adv)
    r = dd+mod-otdMod
    if dd <= hrup:
        return D

    elif  r >= kd or dd == 20:

        sn = 0
        if dd != 20:
            sn = max(2.5*(kz-ap+1), 0)

        damage = sum([(k+1)/2 for k in dmgList])
        if dd == 20:
            D += damage*2
        elif r == kd:
            D += max(damage//2-sn, 0)
        elif r > kd:
            D += max(damage-sn, 0)
    
    return D


def getSrDamage(kd, kz, ap, dmgList, mod=0, otd=0, auto=0, od=1, adv='=', N=100000, hrup=1):

    a = []
    for _ in range(N):
            
        a.append(0)
        n = 0
        cl = 0
        if otd >= 1:
            for j in range(auto+1):
                d = shoot(kd, kz, ap, dmgList, mod, otd*j, adv, hrup)
                if d == 0:
                    cl += 1
                    break
                a[-1] += d
            for j in range(od-1-cl):
                d = shoot(kd, kz, ap, dmgList, mod, 0, adv, hrup)
                if d == 0:
                    cl += 1
                    continue
                a[-1] += d
        else:
            n = od*(auto+1)
            for j in range(n):
                d = shoot(kd, kz, ap, dmgList, mod, otd*j, adv, hrup)
                if d == 0:
                    cl += 1
                    break
                a[-1] += d
            
    return round(sum(a)/len(a), 3)


targetKD = 16
targetKZ = 3
OD = 3

print("Калаш               :  ", getSrDamage(targetKD, targetKZ, 2, [8, 8]      , 7 , 3, 2, OD))
