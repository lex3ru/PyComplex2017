import math


def Hello():
    print ("Hello world!!!!!!")

def GenTime(StartT,N,fs)
    return np.linspace(StartT, (StartT+(N-1)/fs), N)

def ImpulsGen(ImpName,time,**argIn):
    print(time)
    if ImpName == 'Puzirev':
        ImpFun= lambda t: argIn['A']*math.exp(-(argIn['B']*t)**2)*math.cos(2*math.pi*argIn['f']*(t+argIn['Phi']))
    elif ImpName == 'Berlage':
        ImpFun=lambda t: argIn['A']*(t**argIn['n'])*math.exp(-argIn['B']*t)*math.cos(2*math.pi*argIn['f']*t+math.pi/2)
    elif ImpName == 'Gauss':
        ImpY=argIn['A']*math.exp(-argIn['B']*t**2)*math.sin(2*math.pi*argIn['f']*t)
    return [ImpFun(t) for t in time]