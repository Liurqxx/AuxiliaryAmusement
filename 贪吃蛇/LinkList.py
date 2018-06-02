class node:

    def __init__(self,data):

        self.data=data
        self.next_node=None

class linklist:

    def __init__(self):

        self.node_count=0
        self.head_node=None

    def _move_last(self):

        temp_node=self.head_node
        for i in range(self.node_count-1):

            temp_node=temp_node.next_node
        return temp_node

    def AddNewNode(self,new_node):

        if self.node_count==0:
            self.head_node=new_node
        else:
            self._move_last().next_node=new_node

        self.node_count+=1

    def PassList(self):

        temp_node=self.head_node
        for i in range(self.node_count):

            print(temp_node.data)
            temp_node=temp_node.next_node
        
