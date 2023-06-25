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
 # Module 5.0.2                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */

import java.util.Random;

public class Deck {
  
  //Vars
  private Card[] stack;
  private int currentSize;
  
  //Constructor
  public Deck(){
    
    int count = 0;
    currentSize = 52;
    stack = new Card[52];
    
    for(int s = 0; s < 4; s++) {
      for(int v = 1; v < 14; v++) {
        if(s == 0) {
          stack[count] = new Card(v, "Hearts");
        }
        else if(s == 1) {
          stack[count] = new Card(v, "Diamonds");
        }
        else if(s == 2) {
          stack[count] = new Card(v, "Spades");
        }
        else if(s == 3) {
          stack[count] = new Card(v, "Clubs");
        }
        count++;
      }
    }
    
  }
  
  //Getters
  public Card draw() {
    currentSize--;
    return stack[currentSize];
  }
  public int getSize() {
    return currentSize;
  }
  
  //Shuffle
  public void shuffle() {
    
    Random rand = new Random();
    currentSize = 52;
    
    for(int i = 0; i < stack.length; i++) {
      int r = rand.nextInt(stack.length - i) + i;
      Card temp = stack[i];
      stack[i] = stack[r];
      stack[r] = temp;
    }
    
  }
  
}
