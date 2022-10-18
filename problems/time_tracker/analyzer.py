

file_name = 'tracker_log_sample.txt'
with open(file_name, 'r') as log_file:
    log_dump = log_file.read()

log_lines = log_dump.split('\n\n')
entry = log_lines[0].split('\n')
print(entry)
print(type(log_lines))
print(type(log_lines[0]))
print(log_lines[0])

# for index in range(10):
#     print(log_lines[index])
