# Enter your code here. Read input from STDIN. Print output to STDOUT

def read_command(com):
    values = com.split(' ')
    if(len(values) == 1):
        return [int(values[0]),0]
    else:
        return values

def main():
    string_list = []
    history = []
    his_index = -1
    num_commands = int(input().strip())
    for i in range(num_commands):
        command = input()
        values = read_command(command)
        action = int(values[0])
        if(action == 1):
            history.append(''.join(string_list))
            his_index += 1
            string_new = list(values[1].strip(" "))
            string_list.extend(string_new)
        elif(action == 2):
            history.append(''.join(string_list))
            his_index += 1
            k = int(values[1])
            for i in range(k):
                string_list.pop()
        elif(action == 3):
            k = int(values[1])
            print(string_list[k-1])
        elif(action == 4):
            string_list.clear()
            string_new = list(history[his_index].strip(" "))
            string_list.extend(string_new)
            his_index -= 1
            history.pop()
        
if __name__ == '__main__':
    main()
