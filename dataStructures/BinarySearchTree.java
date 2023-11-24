


// we need things that are comparable so that we can rank them, and pick if they can go right or left
public class BinarySearchTree<T extends Comparable<T>> {
    // Tracks the number of nodes in the BST
    private int nodeCount = 0;

    // This BST is a rooted tree so we maintain a handle on the root node
    private Node root = null;

    // Internal node containing node references
    // and the actual node data
    private class Node {
        T data;
        Node left,right;
        public Node(Node left,Node right,T elem){
            this.data=elem;
            this.left=left;
            this.right=right;
        }
    }

    // Check if this binary tree is empty
    public boolean isEmpty(){
        return size()==0;
    }

    // Get the number of nodes in this binary tree
    public int size(){
        return nodeCount;
    }

    // Add an element to this binary tree. Return true if we have successfully perform an insertion
    public boolean add(T elem){
        // Check if the value already exists in this binary tee , if it does ignore it
        if(contains(elem)){
            return false;
        // otherwise add this element to the binary tree
        }else{
            root = add(root,elem);
            nodeCount++;
            return true;
        }
    }

    // Method to recursively add a value in the binary tree
    private Node add(Node node, T elem){
        // Base case: found a leaf node
        if(node==null){
            node=new Node(null,null,elem);
        }else{
          // place lower elements values in left subtree
          if(elem.compareTo(node.data) < 0){
            node.left = add(node.left,elem);
          }else{
            node.right = add(node.right,elem);
          }
        }
        return node;
    }

    
    

}