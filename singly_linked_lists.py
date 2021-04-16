class SLNode:
    def __init__(self, val=None) :
        self.value = val
        self.next = None


class SList:
    def __init__(self, head=None) :
        self.head = head


    def add_to_front(self, val) :
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self


    def print_values(self) :
        if self.head != None :
            runner = self.head
            while (runner != None) :
                print(runner.value)
                runner = runner.next
        else :
            print("No nodes to print")
        return self


    def add_to_back(self, val) :
        if self.head == None :
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None) :
            runner = runner.next
        runner.next = new_node
        return self


    def remove_from_head(self) :
        runner = self.head
        self.head = runner.next
        return runner.value


    def remove_from_back(self) :
        print("Remove from back")
        runner = self.head
        while (runner.next.next != None) :
            runner = runner.next
        value = runner.next.value
        runner.next = None
        return value

    
    def remove_val(self, val) :
        print("Remove val: ", val)
        runner = self.head
        #if first element
        if runner.value == val:
            self.remove_from_head
        #if middle or last element
        while runner.next.value != val:
            runner = runner.next
        temp = runner.next.next
        runner.next = None
        runner.next = temp
        return self


    def insert_at(self, val, n) :
        print("Insert value: ",val," at position: ",n)
        if n == 0 :
            self.add_to_front(val)
        else:
            runner = self.head
            index = 1
            while index < n:
                runner = runner.next
                index += 1
            temp = runner.next
            new_node = SLNode(val)
            runner.next = new_node
            new_node.next = temp
        return self


    def __str__(self) :
        result = ""
        runner = self.head
        while runner:
            result += str(runner.value) + ", "
            runner = runner.next
        result = result.strip(", ")
        if len(result):
            return "[" + result + "]"
        else:
            return "[]"


if __name__ == "__main__" :
    my_list = SList()
    my_list.add_to_front(2).add_to_front(1).add_to_back(3)
    my_list.add_to_back(4).add_to_back(5).add_to_back(6).add_to_back(7)
    my_list.add_to_back(8).add_to_back(9).add_to_back(10).add_to_back(11)
    print(my_list)
    print(f"Remove from head: {my_list.remove_from_head()}")
    print(my_list)
    print(f"Remove from back: {my_list.remove_from_head()}")
    print(my_list)
    my_list.remove_val(5)
    print(my_list)
    my_list.insert_at(15,3)
    print(my_list)
