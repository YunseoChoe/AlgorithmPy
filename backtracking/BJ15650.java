import java.util.Scanner;

public class BJ15650 {
    public static int n, m;
    public static int[] arr;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        arr = new int[m];

        fun(0, 1);
    }

    public static void fun(int depth, int val) { // 1부터 n까지의 숫자를 담을 수 있음
        if (depth == m) {
            for (int num : arr) { // for num in arr 
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }
        for (int num = val; num <= n; num++) {
            arr[depth] = num;
            fun(depth + 1, num);
        }
    }
}

// javac BJ15650.java
// java BJ15650
// BJ15650.n

