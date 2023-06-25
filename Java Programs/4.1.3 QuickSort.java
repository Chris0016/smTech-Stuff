/*
# - - - - - - - - - - - - - - - - #
# SummerTech/Coditum Curriculum   #
# Created by Jonah Wolmark        #
#                                 #
# Report any bugs, issues, or     #
# corrections to:                 #
# matt@summertech.net             #
#                                 #
#                                 #
# Module 4.1.3                    #
# - - - - - - - - - - - - - - - - #
 
SUMMERTECH CONFIDENTIAL
COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
*/


import java.util.ArrayList;

public class QuickSort {
  
	public static void main(String[] args) {
    
		ArrayList<Integer> ls = new ArrayList<Integer>();
    
		for(int i = 0; i < 10; i++) {
			ls.add((int)(Math.random() * 100));
		}
    
		System.out.println(ls);
		System.out.println(sort(ls));
    
	}
	
	public static ArrayList<Integer> sort(ArrayList<Integer> list) {
		
		//Base case
		if(list.size() <= 1) {
			return list;
		}
		
		//Last element becomes the pivot
		int indexOfPivot = list.size() - 1;
		int pivot = list.get(indexOfPivot);
		
		//Take everything that is greater than (not equal to!) the pivot and move it to the end
		for(int i = 0; i < indexOfPivot; i++) {
			if(list.get(i) > pivot) {
				list.add(list.remove(i));
				i--;
				indexOfPivot--;
			}
		}
		
		//Create sublists
		//Everything before the pivot
		ArrayList<Integer> sub1 = new ArrayList<Integer>();
		for(int i = 0; i < indexOfPivot; i++) {
			sub1.add(list.get(i));
		}
		//Everything after the pivot
		ArrayList<Integer> sub2 = new ArrayList<Integer>();
		for(int i = indexOfPivot + 1; i < list.size(); i++) {
			sub2.add(list.get(i));
		}
		
		//Out with the old
		list.clear();
		
		//In with the new
		list.addAll(sort(sub1));
		list.add(pivot);
		list.addAll(sort(sub2));
		
		return list;
    
	}
  
}
