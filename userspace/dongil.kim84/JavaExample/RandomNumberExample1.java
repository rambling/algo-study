package java_example;

import java.util.Arrays;
import java.util.Random;

public class RandomNumberExample1 {
	
	public static void main(String args[]){
		int randomNum[] = new int[10];
		Random r = new Random();
		
		for(int i=0; i<randomNum.length; i++){
			randomNum[i] = r.nextInt(50) + 1;
			for(int j=0; j<i; j++){
				if(randomNum[i] == randomNum[j])
					i--;
			}
		}
		
		Arrays.sort(randomNum);
		System.out.println(Arrays.toString(randomNum));
		
	}
	
}
	
