import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Leetcode226BFS {
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        static List<Integer> levelOrderTraversal(TreeNode root) {
            List<Integer> visited = new ArrayList<>();
            Queue<TreeNode> queue = new LinkedList<>();

            if (root == null) {
                return visited;
            }

            queue.offer(root);
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                visited.add(node.val);

                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }

            return visited;
        }
    }

    static class Solution {
        /**
         * Runtime: 1 ms, faster than 100.00% of Java online submissions for Invert Binary Tree.
         * Memory Usage: 38.7 MB, less than 5.91% of Java online submissions for Invert Binary Tree.
         */
        public TreeNode invertTree(TreeNode root) {
            Queue<TreeNode> queue = new LinkedList<>();

            if (root != null) {
                queue.offer(root);

                while (!queue.isEmpty()) {
                    TreeNode node = queue.poll();

                    if (node.left != null)
                        queue.offer(node.left);
                    if (node.right != null)
                        queue.offer(node.right);

                    TreeNode temp = node.left;
                    node.left = node.right;
                    node.right = temp;
                }
                return root;
            } else {
                return null;
            }
        }
    }
}
