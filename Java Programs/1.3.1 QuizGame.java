/*
 # - - - - - - - - - - - - - - - - #
 # SummerTech/Coditum Curriculum   #
 # Created by Sam Perlman          #
 #                                 #
 # Report any bugs, issues, or     #
 # corrections to:                 #
 # matt@summertech.net             #
 #                                 #
 #                                 #
 # Module 1.3.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class QuizGame {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		
		int points = 0;
		int totalQuestions = 5;
		
		System.out.println("What is the answer to Life, the Universe, and Everything?");
		String answer = scan.next();
		if (answer.equals("42")) {
			System.out.println("Correct!");
			points++;
		}
		else {
			System.out.println("Incorrect. It was 42.");
		}
		
		System.out.println("What is the third triangle number?");
		int answer2 = scan.nextInt();
		if (answer2 == 6) {
			System.out.println("Correct!");
			points++;
		}
		else {
			System.out.println("Incorrect. It was 6.");
		}
		
		System.out.println("What is the last name of the Pokemon Professor from Sinnoh?");
		answer = scan.next();
		if (answer.equals("Rowan")) {
			System.out.println("Correct!");
			points++;
		}
		else {
			System.out.println("Incorrect. It was Rowan.");
		}
		
		System.out.println("What is the name of Mario's brother?");
		answer = scan.next();
		if (answer.equals("Luigi")) {
			System.out.println("Correct!");
			points++;
		}
		else {
			System.out.println("Incorrect. It was Luigi.");
		}
		
		System.out.println("What is the capital of New York?");
		answer = scan.next();
		if (answer.equals("Albany")) {
			System.out.println("Correct!");
			points++;
		}
		else {
			System.out.println("Incorrect. It was Albany.");
		}
		
		System.out.println("You got " + points + " out of " + totalQuestions + " correct!");
	}
}
