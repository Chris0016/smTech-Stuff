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
# Module 4.1.2                    #
# - - - - - - - - - - - - - - - - #
 
SUMMERTECH CONFIDENTIAL
COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
*/


import java.util.ArrayList;

public class MergeSort {
  
	public static void main(String[] args) {
    
		ArrayList<Integer> ls = new ArrayList<Integer>();
    
		for(int i = 0; i < 10; i++) {
			ls.add((int)(Math.random()*100));
		}
    
		System.out.println(ls);
		System.out.println(sort(ls));
    
	}

	private static ArrayList<Integer> sort(ArrayList<Integer> list) {
    
		//Base case
		if(list.size() <= 1) {
			return list;
		}
		
		//Splits list in half and puts it into sublists
		ArrayList<Integer> sub1 = new ArrayList<Integer>();
		ArrayList<Integer> sub2 = new ArrayList<Integer>();
    
		for(int i = 0; i < list.size(); i++) {
			if(i < (list.size() / 2)) {
				sub1.add(list.get(i));
			}
			else {
				sub2.add(list.get(i));
			}
		}
		
		//Recursively splits lists down until they're size 1
		sub1 = sort(sub1);
		sub2 = sort(sub2);
		
		//Recombines sublists
		return merge(sub1, sub2);
    
	}

	private static ArrayList<Integer> merge(ArrayList<Integer> sub1, ArrayList<Integer> sub2) {
		
		ArrayList<Integer> result = new ArrayList<Integer>();
		
    int i = 0;
    int j = 0;
    
		while((i < sub1.size()) && (j < sub2.size())) {
			if(sub1.get(i) <= sub2.get(j)) {
				result.add(sub1.get(i));
        i++;
			}
			else {
				result.add(sub2.get(j));
        j++;
			}
		}
		
		while(i < sub1.size()) {
			result.add(sub1.get(i));
      i++;
		}
		while(j < sub2.size()) {
			result.add(sub2.get(j));
      j++;
		}
		
		return result;
    
	}
	
}
