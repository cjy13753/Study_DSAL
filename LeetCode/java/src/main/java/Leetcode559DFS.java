import java.util.ArrayList;
import java.util.List;

/**
 * Comment:
 * In the actual Leetcode test case, it gives us the root that a link to its children which, each of which
 * has its own link to respective children.
 * I misunderstood the problem, thinking that I need to parse the Integer array to make a node tree out of it.
 * All I needed to implement was just the recursive method to find the depth of the tree,
 * which is like the calculateMaxDepth() method below.
 * Nonetheless, it was a good exercise to parse an Integer array with a specific pattern.
 */


public class Leetcode559DFS {
    // Definition for a Node.
    static class Node {
        public int val;
        public List<Node> children;

        public Node() {}

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, List<Node> children) {
            this.val = val;
            this.children = children;
        }

            public void setChildren(List<Node> children) {
                this.children = children;
            }

        @Override
        public String toString() {
            return "Node{" +
                    "val=" + val +
                    '}';
        }
    };

    static class Solution {

        List<Node> nodeList = new ArrayList<>();

        Solution() {
        }

        Solution(Integer[] input) {
            for (Integer integer : input) {
                if (integer == null) {
                    nodeList.add(null);
                } else {
                    nodeList.add(new Node(integer));
                }
            }
        }

        /**
         * Runtime: 11 ms, faster than 6.10% of Java online submissions for Maximum Depth of N-ary Tree.
         * Memory Usage: 44.8 MB, less than 5.18% of Java online submissions for Maximum Depth of N-ary Tree.
         *
         * Self-feedback:
         * Needlessly applied sorting algorithm in .max(Integer::compareTo), which must have slowed down the process.
         */
        private int calculateMaxDepth(Node root) {
            if (root == null) {
                return 0;
            } else if (root.children == null) {
                return 1;
            } else {
                return 1 + root.children.stream()
                        .map(this::calculateMaxDepth)
                        .max(Integer::compareTo)
                        .orElse(0);
            }

        }

        public int maxDepth(Node root) {
            /* Create node list out of integer array */
            List<List<Node>> container = new ArrayList<>();
            int index = 0;
            container.add(new ArrayList<>());
            for (Node node : nodeList) {
                if (node != null) {
                    container.get(index).add(node);
                } else {
                    ++index;
                    container.add(new ArrayList<>());
                }
            }

            /* Create node tree */

            if (container.size() == 0) {
                return 0;
            } else if (container.size() == 1) {
                return 1;
            } else {
                root.children = container.get(1);
                int s = 1;
                int e = 1;
                int n;
                int counter = 1;
                while (counter != 0) {
                    counter = 0;
                    n = e + 1;
                    for (int pointer = s; pointer <= e; pointer++) {
                        if (pointer <= container.size() - 1) {
                            for (Node node : container.get(pointer)) {
                                counter += 1;
                                if (n <= container.size() - 1) {
                                    if (container.get(n).size() != 0) {
                                        node.children = container.get(n);
                                    }
                                }
                                n++;
                            }
                        }
                    }
                    s = e + 1;
                    e += counter;
                }
            }

            return calculateMaxDepth(root);
        }



        public int maxDepthMyWay(Integer[] input) {
            List<List<Integer>> container = new ArrayList<>();
            int index = 0;
            container.add(new ArrayList<>());
            for (Integer i : input) {
                if (i != null) {
                    container.get(index).add(i);
                } else {
                    ++index;
                    container.add(new ArrayList<>());
                }
            }

            if (container.size() == 0) {
                return 0;
            } else if (container.size() == 1) {
                return 1;
            } else {
                int depth = 1;
                int prevLastIndex = 0;
                int currLastIndex = 1;
                int counter;
                while (currLastIndex <= container.size() - 1) {
                    counter = 0;
                    for (int i = prevLastIndex + 1; i <= currLastIndex; i++) {
                        counter += container.get(i).size();
                    }
                    prevLastIndex = currLastIndex;
                    currLastIndex += counter;
                    if (counter == 0) {
                        break;
                    }
                    depth += 1;
                }

                if (container.size() - 1 > prevLastIndex) {
                    depth += 1;
                }

                return depth;
            }

        }
    }
}

