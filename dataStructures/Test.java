/**
 * Test
 */
public class Test {

    public static void main(String[] args) {
        ArrayDynamic<Integer> arr=new ArrayDynamic<Integer>();

        for (int i = 0; i < 10; i++) {
            arr.add(i);
        }
        System.out.println(arr.size());
        System.out.println(arr);
        arr.removeAt(4);
        System.out.println(arr);

    }
   static  class ArrayDynamic<T> implements Iterable<T> {
        private int len;
        private int capacity;
        private T[] arr;

        public ArrayDynamic() {
            this(16);
        }

        public ArrayDynamic(int capacity) {
            if (capacity < 0) throw new IllegalArgumentException("Invalid length to start with");
            this.capacity = capacity;
            arr = (T[]) new Object[capacity];
        }

        public int size() {
            return len;
        }

        public boolean isEmpty() {
            return len == 0;
        }
        public T get(int index){
            return arr[index];
        }
        public void set(int index,T elem){
            arr[index]=elem;
        }
        public void add(T elem) {
            if (len + 1 > capacity) {
                if (capacity == 0)
                    capacity += 1;
                else
                    capacity *= 2;
                T[] new_arr = (T[]) new Object[capacity];
                for (int i = 0; i < arr.length; i++) {
                    new_arr[i] = arr[i];
                }
                arr = new_arr;
            }
            arr[len++] = elem;
        }

        void clear(){
            for (int i = 0; i < arr.length; i++) {
                arr[i]=null;
            }
        }
        T removeAt(int rm_index){
            if(rm_index>=len && rm_index<0) throw new IndexOutOfBoundsException();
            T data=arr[rm_index];
            T[] new_arr=(T[]) new Object[len-1];
            for (int i = 0,j=0; i < new_arr.length; i++,j++) {
                if(rm_index==i) j--;
                else new_arr[j]=arr[i];
            }
            arr=new_arr;
            capacity=--len;
            return data;
        }

        boolean remove(T elem){
            for (int i = 0; i < arr.length; i++) {
                if(arr[i].equals(elem)){
                    return true;
                }
            }
            return false;
        }

        int indexOf(T elem){
            for (int i = 0; i < arr.length; i++) {
                if(arr[i].equals(elem)){
                    return i;
                }
            }
            return -1;
        }
        boolean contains(T elem){
            return indexOf(elem)!=-1;
        }

        @Override public java.util.Iterator <T> iterator(){
            return new java.util.Iterator <T> (){
                int index=0;
                public boolean hasNext(){ return index<len;}
                public T next(){ return arr[index++];}
            };
        }
    
        @Override public String toString(){
            if(len==0) return "[]";
            else {
                StringBuilder sb=new StringBuilder(len).append("[");
                for (int i = 0; i < len-1; i++) {
                    sb.append(arr[i]+", ");
                }
                return sb.append(arr[len-1]+"]").toString();
            }
        }
    }

}