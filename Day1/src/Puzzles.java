import java.util.Scanner;
import java.util.ArrayList;

public class Puzzles {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		ArrayList<String> rawValues = new ArrayList<String>();
		
		String value = scanner.next();
		
		while(value.charAt(0) != "*".charAt(0)) {
			rawValues.add(value);
			value = scanner.next();
		}		
		
		int puzzleNum = scanner.nextInt();
		int answer = 0;
		
		if (puzzleNum == 1) { answer = puzzle1(rawValues, answer); }
		else if (puzzleNum == 2) { answer = puzzle2(rawValues); }
		
		System.out.println("\nYour answer is...");
		System.out.println(answer);
		scanner.close();
	}
	
	public static int puzzle1(ArrayList<String> rawValues, int answer) {
		//Does the summation of all values given.
		for(int x = 0; x < rawValues.size(); x++) {	answer += parserInt(rawValues.get(x)); }
		return answer;
	}
	
	public static int puzzle2(ArrayList<String> rawValues) {
		ArrayList<Integer> noDuplicateResult = new ArrayList<Integer>();
		int answer = 0;
		int fin = 0;
		boolean done = false;
		int x = 0;
		
		noDuplicateResult.add(answer);
		
		while(done == false) {
			//Parses the value.
			int result = parserInt(rawValues.get(x));
			
			answer += result; //Adds to summation
			
			/*
			 * If the result is contained in the arraylist, return it and end loop.
			 * Else if end of arraylist, loop again. It's good for the soul. (Also adds summation to the arraylist)
			 * Else, add to x and add the summation to the arraylist.
			 */
			if(noDuplicateResult.contains(answer)) { fin = answer; done = true;}
			else if (x + 1 == rawValues.size()) { x = 0; noDuplicateResult.add(answer); }
			else { x++; noDuplicateResult.add(answer); }
		}
				
		return fin;
	}
	
	public static int parserInt(String value) {
		int result;
		
		//If + at front, value is positive
		//Else, value is negative.
		if(value.charAt(0) == "+".charAt(0)) { result = Integer.parseInt(value.substring(1)); } 
		else { result = -1 * Integer.parseInt(value.substring(1)); }
		
		return result;
	}
}
