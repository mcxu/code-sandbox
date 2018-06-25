package ctci5th.util.list;

//Node class for linked list
public class Node 
{
  public Node next = null;
  public Object data;
  
  public Node(Object data)
  {
      this.data = data;
  }

  
  public void appendToTail(Object d)
  {
      Node end = new Node(d);
      Node n = this;
      while(n.next != null)
      {
          n = n.next;
      }
      n.next = end;
  }
}