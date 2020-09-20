/**
https://leetcode.com/problems/minimum-time-visiting-all-points/
 */
package leetcode;

public class lc1266_MinTimeVisitAllPoints {
    public int minTimeToVisitAllPoints(int[][] points) {
        int totTime = 0;
        for(int i=1; i < points.length; i++) {
            int dx = Math.abs(points[i][0] - points[i-1][0]);
            int dy = Math.abs(points[i][1] - points[i-1][1]);
            totTime += Math.max(dx,dy);
        }
        return totTime;
    }

    public void test1() {
        int[][] points = {{1,1},{3,4},{-1,0}}; // expected: 7
        int res = minTimeToVisitAllPoints(points);
        System.out.println("res: " + res);
    }

    public static void main(String[] args) {
        lc1266_MinTimeVisitAllPoints prob = new lc1266_MinTimeVisitAllPoints();
        prob.test1();
    }
}