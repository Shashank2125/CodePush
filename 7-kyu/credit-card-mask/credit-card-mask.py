# return masked string
def maskify(cc):
    res=[]
    for i in range(len(cc)):
        if i<len(cc)-4:
            res.append('#')
        else:
            res.append(cc[i])
    return "".join(res)