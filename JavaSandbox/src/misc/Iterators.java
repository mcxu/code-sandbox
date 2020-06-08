package misc;

import java.util.ArrayList;
import java.util.Iterator;

public class Iterators 
{
    class MyIter implements Iterator<ArrayList<Integer>> 
    {
        ArrayList<ArrayList<Integer>> al = new ArrayList<ArrayList<Integer>>();
        int delta = 0;

        public MyIter(ArrayList<ArrayList<Integer>> arrOfArr, int delta) {
            for(ArrayList<Integer> arr: arrOfArr) {
                al.add(0, arr);
            }
            this.delta = delta;
        }

        @Override
        public boolean hasNext() {
            if(al.isEmpty()) {
                return false;
            }
            return true;
        }

        @Override
        public ArrayList<Integer> next() {
            ArrayList<Integer> currArrList = al.remove(al.size()-1);
            for(int i=0; i<currArrList.size(); i++) {
                currArrList.set(i, currArrList.get(i)+delta);
            }
            return currArrList;
        }
    }

    public MyIter getMyIterInstance(ArrayList<ArrayList<Integer>> arrOfArr, int delta) {
        return new MyIter(arrOfArr, delta);
    }

    public static void main(String[] args) {
        Iterators it = new Iterators();
        ArrayList<ArrayList<Integer>> arrOfArr = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> inner = new ArrayList<>();
        for(int i=1; i<=64; i++) {
            if(i%8 == 0) {
                inner.add(i);
                arrOfArr.add(inner);
                inner = new ArrayList<>();
            } else {
                inner.add(i);
            }
        }
        
        MyIter mi = it.getMyIterInstance(arrOfArr, 10);

        while(mi.hasNext()) {
            System.out.println(mi.next());
        }

    }
}