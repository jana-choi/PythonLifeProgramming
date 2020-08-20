e = "Chandler: All right Joey, be nice.  So does he have a hump? A hump and a hairpiece? Phoebe: Wait, does he eat chalk? Phoebe: Just, 'cause, I don't want her to go through what I went through with Carl- oh!"

import re

m = re.findall("[A-Za-z]+:", e)
print(m)

M = list(set(m))
print(M)