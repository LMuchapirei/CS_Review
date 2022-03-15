import java.util.Random;

public class PracticeLinkedList {
    private static class LinkedList{
        Node head=null;
        Node tail=null;
        private int size;
        private class Node {
            int data;
            Node next;
            public Node(int data,Node next){
                this.data=data;
                this.next=next;
            }
        }
        public boolean isEmpty() {
            return size() == 0;
        }
        public int size() {
            return size;
        }
        public void addFirst(int elem) {
            // The linked list us empty
            Node new_node=new Node(elem,null);
            new_node.next=head;
            head=new_node;
            size++;
        }

        public void print(){
            Node tNode=head;
            while(tNode!=null)
            {
                System.out.print(tNode.data+"->");
                tNode=tNode.next;
            }
            System.out.println("NULL");
        }
        
        public void printMiddle(){
            int middle=size/2;
            int i;
            Node trav=null;
            if(middle%2==0){
                //even
                for(i=0,trav=head;i<=middle;i++){
                    if(i==middle){
                        System.out.println(trav.data);
                        System.out.println(trav.next.data);
                    }
                    trav=trav.next;
                }
            }else{
                //odd
                for(i=0,trav=head;i<=middle;i++){
                    if(i==middle){
                        System.out.println(trav.data);
                    }
                    trav=trav.next;
                }

            }
        }
    }

    public static void main(String[] args) {
        PracticeLinkedList.LinkedList list=new PracticeLinkedList.LinkedList();
        for(int i=5;i>0;i--){
            // Random rand=new Random();
            // var ranInt=rand.nextInt(345);
            list.addFirst(i);
        }
        list.print();
        list.printMiddle();
    }
}
