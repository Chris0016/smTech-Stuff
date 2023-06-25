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
 # Module 1.4.2                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Random;
import java.util.Scanner;

public class GuessingGame {

	public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
		Random rand = new Random();
		
		int target = rand.nextInt(100) + 1;
		int guess = -1;
		
		int numGuesses = 0;
		
		while (guess != target) {
			System.out.println("Guess a number between 1 and 100 inclusive!");
			guess = scan.nextInt();
			numGuesses++;
			
			if (guess > target) {
				System.out.println("Whoops. Too high!");
			}
			else if (guess < target) {
				System.out.println("Too bad. You guessed too low!");
			}
		}
    
		System.out.println("You guessed it! It only took you " + numGuesses + " tries!");
	}
}

/* Challenge: 
    - Have the student make the game stop after a certain number of guesses
      by adding to the condition of the while loop.
*/
