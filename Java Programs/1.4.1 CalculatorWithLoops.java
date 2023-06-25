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
 # Module 1.4.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class CalculatorWithLoops {

	public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
		String goAgain = "y";
    
    int num1 = 0;
    int num2 = 0;

		while (goAgain.equals("Y")) {
      System.out.println("What is the first number to be used?");
      num1 = scan.nextInt();
      
      System.out.println("What is the second number to be used?");
      num2 = scan.nextInt();
      
      System.out.println("What operation would you like to do?");
      System.out.println("Addition, Subtraction, Multiplication, or Division?");
      String operation = scan.next();
      
      if (operation.equals("Addition")) {
        System.out.println(num1 + num2);
      }
      else if (operation.equals("Subtraction")) {
        System.out.println(num1 - num2);
      }
      else if (operation.equals("Multiplication")) {
        System.out.println(num1 * num2);
      }
      else if (operation.equals("Division")) {
        System.out.println(num1 / num2);
      }
      else {
        System.out.println("Invalid operation entered.");
      }
			
			System.out.println("Input another calculation? (y/n)");
			goAgain = scan.next();
		}
	}
}

/* Challenge:
 - If you believe the student can handle it, consider introducing modulo as an additional
 operation for the calculator.
 */
