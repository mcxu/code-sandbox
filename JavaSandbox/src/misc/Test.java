package misc;

public class Test
{   
    public static int var;
    public Test() {
        var = 10;
    }

    public void test() {
        System.out.println("Test.test() called. var: " + var);
    }

    public static void test2() {
        System.out.println("Test.test2() called. var: " + var);
    }

    class NestedTest {
        int var = Test.var + 22;

        public void test() {
            System.out.println("NestedTest.test() called. var: " + this.var);
        }
    
        public void test2() {
            System.out.println("NestedTest.test2() called. var: " + var);
        }
    
    }

    public static void main(String[] args) {
        Test t = new Test();
        t.test();

        Test.NestedTest nt = t.new NestedTest();
        nt.test();
        nt.test2();

    }
}