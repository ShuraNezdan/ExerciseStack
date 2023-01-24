var1 = '(((([{}]))))'
var2 = '[([])((([[[]]])))]{()}'
var3 = '{{[()]}}'

var4 = '}{}'
var5 = '{{[(])]}}'
var6 = '[[{())}]'


class Stack:
    
    def __init__(self, input_skob):
        self.input_skob = list(input_skob)
    
    def isEmpty(self):
        return bool(self.input_skob)
    
    def push(self, new_element):
        self.input_skob.append(new_element)
    
    def pop(self):
        return self.input_skob.pop()
    
    def peek(self):
        return self.input_skob[-1]
    
    def size(self):
        return len(self.input_skob)
    
    
    
def balans(skob):
    stack_new = Stack('')
    is_True = True
    
    st_old = Stack(skob)
    
    for element in range(st_old.size()):
        element_stack = st_old.pop()
        
        if element_stack in ')]}':
            stack_new.push(element_stack)
        
        elif element_stack in '([{':
            
            if not stack_new.isEmpty():
                is_True = False
                break
            
            open_stack = stack_new.pop()
            if open_stack == ')' and element_stack == '(':
                continue
            if open_stack == ']' and element_stack == '[':
                continue
            if open_stack == '}' and element_stack == '{':
                continue
            
            is_True = False
            break
        
    if is_True and stack_new.size() == 0: 
        print('yes')
        
    else:
        print('No')






if __name__ == '__main__':
    balans(var1)