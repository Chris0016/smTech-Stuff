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
 # Module 2.0.2                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class Square {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the square's side length.");
		int side = scan.nextInt();
		
		for (int i = 0; i < side; i++) {
			for (int j = 0; j < side; j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
}
