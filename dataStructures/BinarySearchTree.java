


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

    //remove a value from this binary tree, if it exiists
    public boolean remove(T elem){
        // Make sure the node we want to remove
        // actually exists before we remove it
        if(contains(elem)){
            root = remove(root,elem);
            return true;
        }
        return false;
    }
    private Node remove(Node node,T elem){
        if(node==null) return null;
        int cmp = elem.compareTo(node.data);
        // Dig into left subtree, the value we're looking 
        // for is greater than the current value
        if(cmp < 0){
            node.left = remove(node.left, elem);

        // Dig into right subtree, the value we're looking 
        // for is greater than the current value
        } else if(cmp > 0){
            node.right = remove(node.right, elem);
        // Found the node we wish to remove
        } else{
            // This is the case with only a right subtree or
            // no subtree at all. In this situation just swap the node we wish to remove with its right child
            if(node.left==null){
                Node rightChild = node.right;
                node.data = null;
                node = null;
                return rightChild;

                //This is the case with only a left subtree or no subtree at all.
                // In this situation just swap the node we wish to remove with its left child
            } else if(node.right == null){
                Node leftChild = node.left;
                node.data = null;
                node =null;
                return leftChild;

               // When removing a node from a binary tree with two links the successor of the node being
               // removed can either be the largest value in the left subtree or the smallest value in the right subtree.
               // In this implementation l have decided to find the smallest value in the right subtree which can be found by traversing as fart left as possible in the right subtree 
            } else {
                // Find the leftmost node in the right subtree
                Node tmp = digLeft(node.right);

                // Swap the data
                node.data = tmp.data;
                // Go into the right subtree and remove the leftmost node we found
                // and swapped data with. This prevents us from having two nodes in our tree with the same value
                node.right = remove(node.right, tmp.data);

                // If instead we wanted to find the largest node in the left subtree as opposed to smallest node in the irhgt subtree
                // he is what we would do
                // Node tmp = digRight(node.left);
                // node.data = tmp.data;
                // node.left = remove(node.left,tmp.data);
            }
        }

        return node;

    }

}