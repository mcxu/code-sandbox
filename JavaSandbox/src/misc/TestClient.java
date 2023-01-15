package misc;

class TestClient
{
    public Test t = null;

    public TestClient() {
        t = new Test();
    }

    public static void main(String[] args) {
        TestClient tc = new TestClient();
        tc.t.test();
        tc.t.var = 20;
        Test.var = 30;
        tc.t.test2();
        

        System.out.println("tc2 ------------");
        TestClient tc2 = new TestClient();
        tc2.t.test();
        tc2.t.test2();
        Test.var = 40;
        tc2.t.test();
        tc.t.test2();
        
    }
}