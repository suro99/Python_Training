# Reading first N lines of a file
def read_first_n_lines(filename,n): # read the specific first N lines of a file
    with open(filename,'r') as f:
        for i in range(n):
            line = f.readline()
            print(type(line))
            if not line:
                break
            print(line.strip())
read_first_n_lines('/home/kolkata/Python/students.txt',15)

# Writing dictionary to a file
data = { "name":"Surajit", "age": 26, "location":"Purulia" }
with open('/home/kolkata/Python/students.txt','w') as f:
    for key, value in data.items():
        f.write(f"{key}:{value}\n")

# Writing a list to a file
list= ['first','second','Third']
with open('students.txt', 'w') as f:
    f.writelines(list)