import re
from collections import Counter
import sys

#print('rado')

# Example Python code
python_code = """
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
a += (a)
b >= $b
print(result)
"""

# Check if at least one command-line argument is provided
if len(sys.argv) > 1:
    first_argument = sys.argv[1]
else:
    #print("missing file name")
    #exit(0)
    first_argument='/mnt/c/Users/rados/Dropbox/box/__engineering/regodox-ez/practice-code.txt.txt'

with open(first_argument, "r") as file:
    file_contents = file.read()

    # Extract punctuation trigrams from Python code
    punctuation_trigrams = re.findall(r'[^\w]{3,}', file_contents)

   # print(punctuation_trigrams)

# Count trigram frequency
trigram_frequency = Counter(punctuation_trigrams)

punctuation_trigrams = []
for trigram, frequency in trigram_frequency.items():
    if len(trigram.replace(" ", "").replace("\n", "")) > 2:
        punctuation_trigrams.append(trigram.strip())

trigram_frequency = Counter(punctuation_trigrams)

for trigram, frequency in trigram_frequency.items():
    print(frequency, trigram.strip())

# Print the trigram frequency
#for trigram, frequency in trigram_frequency.items():
#    if len(trigram.replace(" ", "").replace("\n", "")) > 2:
#        #print("<" +  + '> ' + str(frequency))   
#        print(frequency, trigram.strip())

