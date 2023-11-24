



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
}