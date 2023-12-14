import math


def dispnum(num: float) -> float:
    millnames = ['','k','M','B','T']
    
    n = float(num)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return f'{n / 10**(3 * millidx):.3f}{millnames[millidx]}'.format(, )
