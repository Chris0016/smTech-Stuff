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
 # Module 2.0.6                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class HollowDiamond {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		System.out.println("What is the side length of the "
				+ "diamond?");
		int height = scan.nextInt();
		
    /* Top half (Equilateral Triangle) */
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < height - i; j++) {
        System.out.print(" ");
      }
      for (int k = 0; k < i + 1; k++) {
        if (k == 0 || k == i - 1) {
          System.out.print("* ");
        }
        else {
          System.out.print(" ");
        }
      }
    }
    
    /* Bottom half (Upside-down Equilateral Triangle) */
    for (int i = 1; i < height; i++) {
      for (int j = 0; j < i + 1; j++) {
        System.out.print(" ");
      }
      for (int k = 0; k < height - i; k++) {
        if (k == 0 || k == i - 1) {
          System.out.print("* ");
        }
        else {
          System.out.print(" ");
        }

      }
    }
  }
}
