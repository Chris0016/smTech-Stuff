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
 # Module 1.2.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Scanner;

public class MadLibs {

	public static void main(String[] args) {
    
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Please enter a name.");
		String name = scan.nextLine();
		
		System.out.println("Please enter a noun.");
		String noun1 = scan.nextLine();
		
		System.out.println("Please enter another noun.");
		String noun2 = scan.nextLine();
		
		System.out.println("Please enter an adjective.");
		String adj1 = scan.nextLine();

		System.out.println("Did you ever hear the tragedy of Darth " + name + " The " + adj1 + "?");
		System.out.println("I thought not. It’s not a " + noun1 + " the Jedi would tell you.");
		System.out.println("Ironic.");
		System.out.println("He could save others from " + noun2 + ", but not himself.");
	}

}
