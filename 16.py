# если прога не оч долго считает
from functools import *

@lru_cache(None)
def main(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n - 1) + main(n - 1) + main(n - 2)
    
for i in range(2,2023):
    main(i)

print(main(2023) - main(2021) + 2 * main(2020) - main(2019))