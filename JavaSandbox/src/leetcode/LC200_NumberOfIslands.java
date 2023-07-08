package leetcode;
//https://leetcode.com/problems/number-of-islands/description/

import java.util.Arrays;

public class LC200_NumberOfIslands {
    public int numIslands(char[][] grid) {
        Boolean[][] visited = new Boolean[grid.length][grid[0].length];
        for(Boolean[] row: visited) {
            Arrays.fill(row, false);
        }

        int numIslands = 0;

        for(int r=0; r < grid.length; r++) {
            for(int c=0; c < grid[0].length; c++) {
                Boolean beenVisited = visited[r][c];
                if(grid[r][c]=='1' && !beenVisited) {
                    coverIsland(grid, r, c, visited);
                    visited[r][c] = true;
                    numIslands += 1;
                }
            }
        }

        return numIslands;
    }

    public void coverIsland(char[][] grid, int r, int c, Boolean[][] visited) {
        if(r < 0 || r > grid.length-1 || c < 0 || c > grid[0].length-1) {
            return;
        }

        if(visited[r][c] == true || grid[r][c] == '0') {
            return;
        }

        visited[r][c] = true;

        coverIsland(grid, r-1, c, visited);
        coverIsland(grid, r, c-1, visited);
        coverIsland(grid, r+1, c, visited);
        coverIsland(grid, r, c+1, visited);
    }
}
