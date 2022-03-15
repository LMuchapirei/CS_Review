

public class Stack<T> implements Iterable<T> {
    private java.util.LinkedList<T> list=new java.util.LinkedList<T>();


    // create an empty stack
    public Stack() {
        
    }

    // create a stack with an inittal element
    public Stack(T firstElem) {
        push(firstElem);
    }

    public int size(){
        return list.size();
    }
    //Check if the stack is empty
    public boolean isEmpty(){
        return size()==0;
    }

    // Push an element on the stack
    public void push(T elem){
        list.addLast(elem);
    }

    // Pop element on top of the stack
    public T pop() throws Exception{
        if(isEmpty())
            throw new Exception("Empty stack");
        return list.removeLast();
    }

    public T peek() throws Exception{
        if(isEmpty())
            throw new Exception("Empty stack");
        return list.peekLast();
    }

    @Override
     public java.util.Iterator<T> iterator(){
         return list.iterator();
     }
}