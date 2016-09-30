
import java.util.ArrayList;
import java.util.Collections;

public class PermutationString {
	
	static ArrayList<String> arr = new ArrayList<String>();
	
	public static void main(String[] args) {
		
		boolean check = false;
		permutation("bac");
		
		Collections.sort(arr);
		
		for(int i=0; i<arr.size(); i++){
			if(check)
//				System.out.println(arr.get(i));
			if(arr.get(i).equals("bac"))
				check = true;
		}
	}

	public static void permutation(String str) {
		permutation("", str);
	}

	private static void permutation(String prefix, String str) {
		int n = str.length();
		if (n == 0)
			arr.add(prefix);
		else {
			for (int i = 0; i < n; i++){
				System.out.print(i + " : " + prefix + str.charAt(i) + " : " + str.substring(0, i) + " : " + str.substring(i + 1, n) + " : " + n);
				System.out.println("");
				permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n));
			}
		}
	}
	
}
