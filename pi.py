# Pi digits downloaded from: http://www.angio.net/pi/digits.html
from scipy import stats

# 100.txt points to a file holding 100 digits of pi
file_name = "100000.txt"

# Boring file opening operations
print("Opening file")
file = open(file_name)
data = file.readlines()

print("File opened successfully")
string = data[0]

# To remove the decimal point from pi use this:
    # (assuming pi only has 1 decimal point)
pi = string.replace(".", "")

# Now we can get to some analysis

# Create an empty array to hold the digit counts
digit_count = [0]*10

# Iterate through each digit of pi, and tally the counts in the array:
#   "digit_count"

for digit_of_pi in xrange(0, len(pi)):
    digit_count[int(pi[digit_of_pi])] += 1

# Create the array of expected values
expected_count = len(pi)/10.0
expected_array = [expected_count]*10

result = stats.chisquare(digit_count, expected_array)

p_value = result[1]
print(digit_count)
print("For %s digits of pi, we received a p-value of %r" % (len(pi), p_value))
