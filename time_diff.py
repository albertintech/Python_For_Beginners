# You will get the values for two moments in time of the same day: when Megan went for a walk, and when it started to rain. It is known that the first event happened earlier than the second one. Find out how many seconds passed between them.

# The program gets the input of six integers, each on a separate line. The first three integers represent hours, minutes, and seconds of the first event, and the rest three integers define similarly the second event. Print the number of seconds between these two moments of time.


first_h = 1
first_m = 1
first_s = 1

second_h = 2
second_m = 2
second_s = 2

h_diff = second_h - first_h
m_diff = second_m - first_m
s_diff = second_s - first_s

h_result = h_diff * 60 * 60
m_result = m_diff * 60
s_result = s_diff

total_seconds = h_result + m_result + s_result

print(total_seconds)
