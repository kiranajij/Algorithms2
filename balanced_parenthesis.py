def check_balance(string):
    pars = []
    l = len(string)
    for i in range(l):

        try:
            if string[i] == '(':
                pars.append(i)
            if string[i] == ')':
                pars.pop()
        except:
            pars.append(i)
            return pars
    if len(pars) == 0:
        return True
    else:
        return pars


def main():
    while True:
        s = input()
        res = check_balance(s)
        print(res)



main()
