

import java.util.ArrayList;
import java.util.Scanner;

public class ShiftArrayList {
	
	public static void main(String[] args){
		
		int[] n = { 6246, 87, 0, -75, 3531, 1 };

		ArrayList<Integer> arr = new ArrayList<Integer>();
		for(int num : n)
			arr.add(num);
		ArrayList<Integer> arr1 = (ArrayList<Integer>) arr.clone();
		ArrayList<Integer> arr2 = (ArrayList<Integer>) arr.clone();
		
		System.out.println(arr);
		System.out.println(arr1);
		System.out.println(arr2);
		
		Scanner scan = new Scanner(System.in);
		System.out.println("몇 칸 이동할지 정하세요 : ");
		
		int shiftNum = scan.nextInt();
		
		for (int i = 0; i < shiftNum; i++) {
			arr1.add(arr1.get(0));
			arr1.remove(0);
		}
		System.out.println("좌측으로 " + shiftNum + "칸 이동 : " + arr1);
		
		for (int i = 0; i < shiftNum; i++) {
			arr2.add(0, arr2.get(arr2.size()-1));
			arr2.remove(arr2.size()-1);
		}
		System.out.println("우측으로 " + shiftNum + "칸 이동 : " + arr2);
	}
}
