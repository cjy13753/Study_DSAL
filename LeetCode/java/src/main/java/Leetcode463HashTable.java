import java.util.Arrays;

public class Leetcode463HashTable {
    public static void main(String[] args) {
        int[][] grid1 = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        int[][] grid2 = {{1}};
        int[][] grid3 = {{1, 0}};

        System.out.println(islandPerimeter(grid1));
        System.out.println(islandPerimeter(grid2));
        System.out.println(islandPerimeter(grid3));

    }

    // Runtime: 13 ms, faster than 7.90% of Java online submissions for Island Perimeter.
    // Memory Usage: 40.4 MB, less than 28.00% of Java online submissions for Island Perimeter.
    public static int islandPerimeter(int[][] grid) {
        int countLand = 0;
        for (int[] arr : grid) {
            countLand += Arrays.stream(arr).sum();
        }

        int countAdjacent = 0;
        for (int[] row : grid) {
            for (int col = 0; col < grid[0].length - 1; col++) {
                if (row[col] == 1 && row[col + 1] == 1) {
                    countAdjacent++;
                }
            }
        }
        for (int col = 0; col < grid[0].length; col++) {
            for (int row = 0; row < grid.length - 1; row++) {
                if (grid[row][col] == 1 && grid[row + 1][col] == 1) {
                    countAdjacent++;
                }
            }
        }

        return countLand * 4 - countAdjacent * 2;
    }

    // Runtime: 5 ms, faster than 99.30% of Java online submissions for Island Perimeter.
    // Memory Usage: 39.7 MB, less than 95.89% of Java online submissions for Island Perimeter.
    public static int islandPerimeterDiscuss(int[][] grid) {
        int islands = 0, neighbours = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++; // count islands
                    if (i < grid.length - 1 && grid[i + 1][j] == 1) neighbours++; // count down neighbours
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbours++; // count right neighbours
                }
            }
        }

        return islands * 4 - neighbours * 2;
    }

}
