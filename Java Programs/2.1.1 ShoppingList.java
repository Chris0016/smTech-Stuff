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
 # Module 2.1.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class ShoppingList {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		
		System.out.println("How many items will be on your list?");
		int numItems = scan.nextInt();
		
		String[] shoppingList = new String[numItems];
		
		for (int i = 0; i < shoppingList.length; i++) {
			System.out.println("What would you like to add to your list?");
			String item = scan.next();
			shoppingList[i] = item;
		}
		
		System.out.println("Here is your list!");
		for (int i = 0; i < shoppingList.length; i++) {
			System.out.println(shoppingList[i]);
		}
		System.out.println("Happy shopping!");
	}
}
