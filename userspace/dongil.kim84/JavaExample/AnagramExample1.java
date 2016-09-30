

import java.util.Arrays;

public class AnagramExample1 {
	public static void main(String args[]){
		String firstTxt = "aAbb";
		String secondTxt = "AaBB";
		boolean result = false;
		
		result = isAnagram(firstTxt, secondTxt);
		System.out.println(result);
		
	}
	
	public static boolean isAnagram(String firstWord, String secondWord) {
		char[] word1 = firstWord.toLowerCase().trim().toCharArray();
		char[] word2 = secondWord.toLowerCase().trim().toCharArray();
		
//		char[] word1 = firstWord.replaceAll("[\\s]", "").toCharArray();
//	    char[] word2 = secondWord.replaceAll("[\\s]", "").toCharArray();
		
	    Arrays.sort(word1);
	    Arrays.sort(word2);
	    return Arrays.equals(word1, word2);
	}
}
