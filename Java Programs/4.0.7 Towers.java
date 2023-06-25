/*
 # - - - - - - - - - - - - - - - - #
 # SummerTech/Coditum Curriculum   #
 # Created by Jared Okun           #
 #                                 #
 # Report any bugs, issues, or     #
 # corrections to:                 #
 # matt@summertech.net             #
 #                                 #
 #                                 #
 # Module 4.0.7                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */


public class Towers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		towers(7, 1, 2, 3);
	}
	
	public static void towers(int disk, int start, int mid, int end) {
    
		if(disk > 0) {
			towers(disk - 1, start, end, mid);
			System.out.println("Move disk " + disk + " from peg " + start + " to peg " + end);
			towers(disk - 1, mid, start, end);
		}
    
	}

}
