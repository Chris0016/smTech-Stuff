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
 # Module 1.4.3                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		Random rand = new Random();
    
		String playAgain = "y";
    int playerChoice = -1;
    int cpuChoice = 0;

		while(playAgain.equals("y")){

			while(playerChoice < 0 || playerChoice > 2) {
				System.out.println("What is your choice? (0 for rock, 1 for paper, 2 for scissors)");
				playerChoice = scan.nextInt();
				if(playerChoice < 0 || playerChoice > 2) {
					System.out.println("Invalid choice. Try again.");
				}
			}

      /* Rock <=> 0, Paper <=> 1, Scissors <=> 2 */
			cpuChoice = rand.nextInt(3);
      
      
			System.out.print("The computer chose: ");
			if(cpuChoice == 0) {
				System.out.println("Rock");
			}
			else if(cpuChoice == 1) {
				System.out.println("Paper");
			}
			else {
				System.out.println("Scissors");
			}
			
			if(playerChoice == cpuChoice) {
				System.out.println("It's a tie!");
			}
			else if(playerChoice == 0) {
				if(cpuChoice == 1) {
					System.out.println("The computer wins!");
				}
				else {
					System.out.println("You win!");
				}
			}
			else if(playerChoice == 1) {
				if(cpuChoice == 2) {
					System.out.println("The computer wins!");
				}
				else {
					System.out.println("You win!");
				}
			}
			else {
				if(cpuChoice == 0) {
					System.out.println("The computer wins!");
				}
				else {
					System.out.println("You win!");
				}
			}
			
			System.out.print("Play again? (y/n): ");
			playAgain = scan.next();
		}
	}
}
