###############################################################################
## 25. -- HARD --- Reverse Nodes in k-Group 
###############################################################################
#Given the head of a linked list
#    
#    - reverse the nodes of the list k at a time, 
#        return the modified list.
#
#    - k is a positive integer 
#        less than or equal to the length of the list.
#        
#   If the number of nodes is not a multiple of k then left-out nodes, 
#   in the end, should remain as it is.

#You may not alter the values in the list's nodes,
#only nodes themselves may be changed.

# Definition for singly-linked list.   
class Node:
    """
    A Node in a linked structure
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    """
    A linked list
        - the depth of linkage depends on the Node attributes
        - Extend the Node() Class to change that behavior
    """
    def __init__(self,input_array:list,solution:int):
        self.nodes = []
        self.solution = solution
        if input_array is not None or len(input_array > 0):
            self.input = input_array
            self.list_length  = len(self.input)
            print(f"[+] Input Array is: {self.input}")
            print(f"[+] Input Array Length is : {self.list_length}")
        else:
            raise ValueError("list can not be empty or None")
        #populate the list with Nodes
        self.populate()

    def populate(self):
        """
        Appends nodes to list from input

        List stored in self.nodes
        """
        print("[+] Populating List!")
        for each in self.input:
            #create new node
            # remember, in Zero Based Indexing, +2 gets the integer representing the next element
            newnode = Node(val = each, next = self.input.index(each) + 2)
            #print(f"[+] New Node Created: VALUE: {newnode.val} NEXT: {newnode.next}")
            self.nodes.append(newnode)

                
    def validatelink(self):
        """
        Validates information stored in the Node 
        entity before appending to data structure
        """

    def reverseslice(
                    self, 
                    head:Node=0,
                    slice_size:int=1,
                    pad:bool=True
                    ):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.slice_length = slice_size
        self.output_list = []
        # bounds checking
        if self.slice_length > self.list_length:
            #raise ValueError("List Length smaller than slice length")
            print("[!] List Length smaller than slice length")
            print("[+] Returning the list itself, reversed")
            #return self.input.reverse()
            self.nodes.reverse()
            return self.nodes
        
        # multiple solutions
        if self.solution == 1:
            print("[+] Running Code For Solution One!")            
            results = self.method1(input_list=self.nodes, x_lim = slice_size)
            return results
        elif self.solution == 2:
            print("[+] Running Code For Solution Two!")
            results = self.method2(input_list=self.nodes, x_lim = slice_size)
            return results

    def method1(self,input_list:list, x_lim:int=3):
        """
        Pops x number of items from array starting at index 0
        
        :type input_list: list
        :type x_lim: int
        """
        output_list = []
        intermediary_list = []
        #pop node, and add to list
        for node in input_list:
            # if there are x > x_lim elements to remove
            if len(input_list)> x_lim:
                # until input list == x_lim
                while len(intermediary_list) < x_lim:
                    #pop them out
                    intermediary_list.append(input_list.pop(0))
                # append the sorted data to output container
                intermediary_list.reverse()
                output_list.extend(intermediary_list)
                # clear temporary container for next itteration
                intermediary_list = []
            
            # if the input list is smaller than or equal to slice width
            # reverse ordering and append
            if len(input_list) <= x_lim:
                input_list.reverse()
                output_list.extend(input_list)
                break

        return output_list
    
    def method2(self, input_list:list, x_lim:int=3):
        output_list = []
        intermediary_list = []
        while len(input_list) > 0:
        # indexes start at 0, adjust x_lim to reference by index
            for x in range(0,x_lim -1):
                # if list is smaller than or equal to x_lim
                if len(input_list) <= x_lim:
                    # append the reversed remainder
                    input_list.reverse()
                    intermediary_list.extend(input_list)
                # if input list is larger than x_lim
                elif len(input_list) > x_lim:
                    # pop the first element
                    nodeitem = input_list.pop(0)
                    #self.validatelink()
                    intermediary_list.append(nodeitem)
                intermediary_list.reverse()
                output_list.extend(intermediary_list)
                intermediary_list = []
            return output_list

class ScanList:
    def __init__(self,data_input:list,slice_length:int):
        self.processedlist = []
        #create the list
        self.newlist = LinkedList(input_array=data_input,solution=1)
        #create new list with reversed slices
        self.modifiedlist = self.newlist.reverseslice(slice_size=slice_length)

if __name__ == "__main__":
    input_list = [1,2,3,4,5,6,7,8,9,10]
    input_list_test =   [[1,2,3,4,5,6,7,8,9,10],
                        [10,9,8,7,6,5,4,3,2,1],
                        [1,2,3,6,5,4,7,8,9],
                        [1,2,3,4,5,10],
                        [1,2,4,5,6,8,9,10]]
    slice_length = 3
    for item in input_list_test:
        newscan = ScanList(item,slice_length)
        print([val.val for val in newscan.modifiedlist])

    newscan = ScanList(input_list,slice_length)
    print([val.val for val in newscan.modifiedlist])
    exit(0)
