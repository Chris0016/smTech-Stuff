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
 # Module 2.0.3                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class RightTriangle {

	public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
		System.out.println("What is the height of the right triangle?");
		int height = scan.nextInt();
		
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < i + 1; j++) {
				System.out.print("* ");
			}
			System.out.println();
		}
	}
}
