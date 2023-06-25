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
 # Module 5.0.1                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */


public class Card {
  
  //Vars
  private int value;
  private String suit;
  
  //Constructor
  public Card(int v, String s) {
    
    this.value = v;
    this.suit = s;
    
  }
  
  //Getters
  public String getSuit() {
    return suit;
  }
  public int getValue() {
    return value;
  }
  
  //Setters
  public void setSuit(String s) {
    this.suit = s;
  }
  public void setValue(int v) {
    this.value = v;
  }
  
  //Helpful
  public String toString(){
    
    String cardType = "";
    
    if(value > 10){
      if(value == 11)
        cardType = "Jack";
      else if(value == 12)
        cardType = "Queen";
      else if(value == 13)
        cardType = "King";
      return cardType + " of " + suit;
    }
    else if(value == 1) {
      cardType = "Ace";
      return cardType + " of " + suit;
    }
    return value + " of " + suit;
    
  }
  
}
