#
# Filter (most) plurals from a list of words
# NOTE: not 100% accurate! In particular, some plural words
# ending with -i or -u may not be filtered out.
# (taxis, delis, gurus)
# Some plural words may also be erroneously filtered out,
# but haven't bothered to check them myself.
# 

import re

# Words ending with -s should generally be plural.
# However, many singular words may also end with -s
# -is, -ss and -us are particular suspects
# (aegis, basis, dress, truss, fetus, genus)
pattern = re.compile(r"(?<!i|s|u)s$")
with open("sgb-words.txt", "r") as input:
    words = [word for word in input.read().splitlines() if not re.search(pattern, word)]

with open("sgb-words-singular.txt", "w") as output:
    output.write("\n".join(words))





