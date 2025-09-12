
import java.util.ArrayList;
// 순서 고려하지 않고 3개 뽑아서  출력하는 거

public class quiz {
    ArrayList<Integer> arr2 = new ArrayList<Integer>();
    ArrayList<Integer> arr4 = new ArrayList<Integer>();

    static int[] arr = {1,3, 4, 7, 9, 12};
    int[][] arr3 = {{1, 3, 4}, {5, 7, 8}, {10, 11, 14}};
    // 2차원 행렬에서 순서 고려하지 않고 2개 뽑아서 출력하는 거
    public static void main(String[] args) {
        
    }

    public void func(int value) {
        if (arr2.size() == 3) {
            for (int i = 0; i < 3; i++) {
                System.out.println(arr2.get(i) + " ");
                return;
            }
        }
        for (int i = value; i < arr.length; i++) {
            arr2.add(arr[i]);
            func(i + 1);
            arr2.remove(i);
            
        }

    }

    public void func2(int value) {
        if (arr4.size() == 2) {
            for (int i = 0; i < 2; i++) {
                System.out.println(arr4.get(i) + " ");
                return;
            }
        }
        for (int i = value; i < arr3.length; i++) {
            for (int j = )
        }
    }
    
    

}




