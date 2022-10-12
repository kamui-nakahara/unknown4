from math import *
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def line_hit(x,y,x1,y1,x2,y2,size):
    a=atan2(y2-y1,x2-x1)
    b=atan2(y-y1,x-x1)
    c=a-b
    d=distance(x1,y1,x,y)
    e=sin(c)*d
    f=cos(c)*d
    g=cos(a)*f+x1
    h=sin(a)*f+y1
    return (abs(e)<=size and (x1<=g<=x2 or x2<=g<=x1) and (y1<=h<=y2 or y2<=h<=y1))
