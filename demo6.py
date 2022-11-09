def trim(s):

    if len(s)==0:

        return s

    elif s[0]==' ':

        while s[0]==' ':

            s=s[1:]

            return trim(s)

    elif s[-1]==' ':

        while s[-1]==' ':

            s=s[:-1]

s = ' hello world'
trim(s)