'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
''' 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class P3():
    
    def __init__(self):
        pass
         
    '''
    root is a tree object
    '''
    def serialize(self, root):
        print("serialize: root obj: {},  root val: {}".format(root, root.val))
        ser_str = self.serialize_helper(root, "")
        return ser_str[0:-1] # remove last comma
    
    def serialize_helper(self, root, ser_str):
        ser_str += (str(root.val) + ",")
        print("serialize_helper: root.val: {},  ser_str: {}".format(root.val, ser_str))
        
        if root.left is not None:
            print("    root left: {},  ser_str: {}".format(root.left.val, ser_str))
            ser_str = self.serialize_helper(root.left, ser_str)
        if root.right is not None:
            print("    root right: {},  ser_str: {}".format(root.right.val, ser_str))
            ser_str = self.serialize_helper(root.right, ser_str)
            
        return ser_str
        
    '''
    root is a tree string
    '''
    def deserialize(self, root):
        print("deserialize: root: " + root)
        node_list = root.split(",")
        print("deserialize: node_list: {}".format(node_list))
        if(len(node_list) == 0):
            return None
        
        # first get root
        node_str = node_list.pop(0)
        print("deserialize: node_str: {}".format(node_str))
        root_obj = self.deserialize_node_list(node_list, Node(node_str))
        return root_obj
    
    
    def deserialize_node_list(self, node_list, node_obj):
        print("========= top of deserialize_node_list =========")
        print("deserialize_node_list: initial node_list: {},  node_obj: {}".format(node_list, node_obj.val));
        if not node_list:
            return node_obj
         
        node_str = node_list.pop(0)
        print("deserialize_node_list: item_str: {}".format(node_str))
        
        # create children
        if(node_str == "left"):
            print("deserialize_node_list: Creating a left node")
            node_obj.left = Node("left")
        if(node_str == "right"):
            node_obj.right = Node("right")
            print("deserialize_node_list: Creating a right node")
        
        # see if there are subnodes    
        if("." in node_str):
            print("deserialize_node_list: subnode exists node_str: {}".format(node_str))
            sub_node_list = node_str.split(".")
            print("deserialize_node_list: sub_node_list: {}".format(sub_node_list))
            sub_node_str = sub_node_list.pop(0)
            if(sub_node_str == "left"):
                node_obj.left = self.deserialize_sub_node_list(sub_node_list, node_obj.left, "left")
            if(sub_node_str == "right"):
                node_obj.right = self.deserialize_sub_node_list(sub_node_list, node_obj.right, "right")

        return self.deserialize_node_list(node_list, node_obj)
        
        
    def deserialize_sub_node_list(self, sub_node_list, node_obj, node_val):
        print("--- top of deserialize_sub_node_list ---")
        print("deserialize_node_list: initial sub_node_list: {},  node_obj: {},  node_val: {}".format(sub_node_list, node_obj.val, node_val));
        if not sub_node_list:
            return node_obj
    
        sub_node_str = sub_node_list.pop(0)
        print("deserialize_sub_node_list: item_str: {}".format(sub_node_str))
        
        # create children
        node_val += ("." + sub_node_str)
        if(sub_node_str == "left"):
            print("deserialize_sub_node_list: Creating a left node. node_val: {}".format(node_val))
            node_obj.left = Node(node_val)
        if(sub_node_str == "right"):
            print("deserialize_sub_node_list: Creating a right node. node_val: {}".format(node_val))
            node_obj.right = Node(node_val)
    
        return self.deserialize_sub_node_list(sub_node_list, node_obj, node_val)
            
    def test_serialize(self, node):
        serialized_str = self.serialize(node)
        print("test_serialize: serialized_str: {}".format(serialized_str))
        print("test_serialize: output type: {}".format(type(serialized_str)))
    
    def test_deserialize(self):
        print("test_deserialize")
        node_list = ['root', 'left', 'left.left', 'right']
        node_obj = Node(node_list.pop(0))
        a = self.deserialize_node_list(node_list, node_obj)
        print("test_deserialize: node_obj after deserialize: {}".format(a))
        b = self.serialize(a)
        print("test_deserialize: serialize again: {}".format(b))
    
    def test_serialize_then_deserialize(self, node):
        serialized_str = self.serialize(node)
        print("** test_serialize_then_deserialize: serialized_str: {}".format(serialized_str))
        deserialized = self.deserialize(serialized_str)
        print("** test_serialize_then_deserialize: deserialized: {}".format(deserialized))
        print("** test_serialize_then_deserialize: first deser val: {}".format(deserialized.val))
        reserialized = self.serialize(deserialized)
        print("** test_serialize_then_deserialize: reserialized: {}".format(reserialized))
    
    def test_assert(self, node):
        assert self.deserialize(self.serialize(node)).left.left.val == 'left.left'
    
def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    
    p3 = P3()
    #p3.test_serialize(node)
    #p3.test_deserialize()
    #p3.test_serialize_then_deserialize(node)
    p3.test_assert(node)
    
if __name__ == "__main__":
    main()