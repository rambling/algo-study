

import java.util.Arrays;

public class ReverseArrayList {
	public static void main(String[] args){
		
		int[] n = { 6246, 87, 0, -75, 3531, 1 };

	    // 원본 정수 배열 출력
	    System.out.println(Arrays.toString(n));

	    // 뒤집어진 정수 배열 출력
	    System.out.println(Arrays.toString(reverseArrayInt(n, 3, 5)));
		
	}

	public static int[] reverseArrayInt(int[] n, int start, int end) {

		int left  = start;         		// 맨 좌측 요소의 첨자
	    int right = end;  				// 맨 우측 요소의 첨자

	    while (left < right) {
	      int temp = n[left];
	      n[left]  = n[right];     		// 좌우 요소 교환
	      n[right] = temp;

	      left++; right--;         		// 배열의 중간 부분으로 한칸씩 이동
	    }

	    return n;
	    
	}
}
