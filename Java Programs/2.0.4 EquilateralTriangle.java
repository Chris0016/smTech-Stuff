/*
 # - - - - - - - - - - - - - - - - #
 # SummerTech/Coditum Curriculum   #
 # Created by Sam Perlman and      #
 #            Matt Baptist         #
 #                                 #
 # Report any bugs, issues, or     #
 # corrections to:                 #
 # matt@summertech.net             #
 #                                 #
 #                                 #
 # Module 2.0.4                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class EquilateralTriangle {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("What is the side length of the "
				+ "equilateral triangle?");
		int height = scan.nextInt();
	
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < height - i; j++) {
        System.out.print(" ");
      }
      for (int k = 0; k < i + 1; k++) {
        System.out.print("* ");
      }
    }		
  }
}
