/*
 # - - - - - - - - - - - - - - - - #
 # SummerTech/Coditum Curriculum   #
 # Created by Gabe Ehrlich         #
 #                                 #
 # Report any bugs, issues, or     #
 # corrections to:                 #
 # matt@summertech.net             #
 #                                 #
 #                                 #
 # Module 4.1.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Random;

public class BubbleSort {
  
  //Will sort 10 random numbers.
  public static void main(String[] args) {
    
    int[] nums = new int[10];
    Random rand = new Random();
    
    //Randomizes and prints the unsorted array
    System.out.println("Unsorted:");
    for(int i = 0; i < nums.length; i++) {
      nums[i] = rand.nextInt(100);
      System.out.print(nums[i] + ", ");
    }
    System.out.println();
    
    //Sorts the array
    nums = bubbleSort(nums);
    
    //Prints the sorted array
    System.out.println("Sorted:");
    for(int i = 0; i < nums.length; i++) {
      System.out.print(nums[i] + ", ");
    }
    System.out.println();
  }
  
  public static int[] bubbleSort(int[] nums) {
    
    for(int j = 0; j < nums.length; j++) {
      for(int i = 0; i < nums.length-1; i++) {
        if(nums[i+1] < nums[i]) {
          int temp = nums[i];
          nums[i] = nums[i+1];
          nums[i+1] = temp;
        }
      }
    }
    return nums;
  }
}
