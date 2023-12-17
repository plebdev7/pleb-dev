import math


def dispnum(num: float) -> float:
    millnames = ['','k','M','B','T']
    
    n = float(num)
    clean_log = 0 if n == 0 else math.log10(abs(n))
    millidx = max(0, min(len(millnames)-1, int(math.floor(clean_log/3))))

    num_val = n / 10**(3 * millidx)
    num_digits = 0 if millidx == 0 else 3 - math.floor(clean_log) % 3
    num_name = millnames[millidx]
    return f'{num_val:.{num_digits}f}{num_name}'
