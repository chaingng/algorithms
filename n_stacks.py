class NStacks(object):
    # stack_abs_index = stack_num * stack_size + stack_pointer
    def __init__(self, stack_size=10, stack_num=5):
        self.stack_size = stack_size
        self.stack_pointer = [-1] * stack_num
        self.stack_array = [None] * stack_num * self.stack_size

    def push(self, stack_num, value):
        if self.stack_pointer[stack_num] == self.stack_size - 1:
            raise Exception('stack is full')
        self.stack_pointer[stack_num] += 1
        index = stack_num * self.stack_size + self.stack_pointer[stack_num]
        self.stack_array[index] = value

    def pop(self, stack_num):
        if self.stack_pointer[stack_num] == -1:
            raise Exception('stack is empty')
        index = stack_num * self.stack_size + self.stack_pointer[stack_num]
        value = self.stack_array[index]
        self.stack_pointer[stack_num] -= 1
        return value


stacks = NStacks()
stacks.push(0, 1)
stacks.push(0, 2)
stacks.push(1, 3)
stacks.push(2, 4)
print(stacks.pop(0))
print(stacks.pop(0))
print(stacks.pop(1))
print(stacks.pop(2))
