def read_command(msg):
    values = msg.split(" ")
    if(len(values) == 2):
        return [int(values[0]),int(values[1])]
    else:
        return [int(values[0]),0]

class stack:
    def __init__(self):
        self.stack_l = []
        self.top_val = -1
    
    def pop(self):
        self.top_val -= 1
        return self.stack_l.pop()
    
    def push(self,value):
        self.top_val += 1
        self.stack_l.append(value)
    
    def top(self):
        return self.top_val
    
class queue:
    def __init__(self):
        self.stack_front = stack()
        self.stack_back = stack()
        front_value = None
        
    def enqueue(self,value):
        self.stack_back.push(value)
        
    def dequeue(self):
        self.update_stack_front()
        return self.stack_front.pop()
    
    def next_dequeue(self):
        self.update_stack_front()
        next_deq = self.stack_front.pop()
        self.stack_front.push(next_deq)
        return next_deq
    
    def update_stack_front(self):
        if(self.stack_front.top() == -1):
            while(self.stack_back.top() != -1):
                self.stack_front.push(self.stack_back.pop())

def main():
    queue_data = queue()
    num_command = int(input())
    for i in range(num_command):
        msg = input()
        action,value = read_command(msg)
        if(action == 1):
            queue_data.enqueue(value)
        elif(action == 2):
            queue_data.dequeue()
        elif(action == 3):
            print(queue_data.next_dequeue())
if __name__ == '__main__':
    main()
