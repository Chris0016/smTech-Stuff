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
 # Module 5.0.4                    #
 # - - - - - - - - - - - - - - - - #
 
 SUMMERTECH CONFIDENTIAL
 COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
 */


import java.util.ArrayList;

public class War {
  
  public static void main(String[] args) throws InterruptedException {
    
    //Variables
    Deck d = new Deck();
    d.shuffle();
    ArrayList<Card> p1 = new ArrayList<Card>();
    ArrayList<Card> p2 = new ArrayList<Card>();
    ArrayList<Card> playing = new ArrayList<Card>();
    int warCount = 0;
    boolean game = true;
    
    //Split the deck into two
    while(d.getSize() > 0) {
      p1.add(d.draw());
      p2.add(d.draw());
    }
    
    //Game loop
    while(game == true) {
      
      //Announce then Play cards
      System.out.println("Player one flips: " + p1.get(0) + "   Player two flips: " + p2.get(0));
      System.out.println("Player one size: " + p1.size()+"   Player two size: " + p2.size() +
                         "    Playing field size: " + playing.size());
      Thread.sleep(500);
      playing.add(0, p1.get(0));
      p1.remove(0);
      playing.add(1, p2.get(0));
      p2.remove(0);
      
      //Comparing the two most recent cards
      //Player one wins
      if(playing.get(0).getValue() > playing.get(1).getValue()) {
        System.out.println("Player one wins the hand.");
        while(!playing.isEmpty()) {
          p1.add(playing.get(0));
          playing.remove(0);
        }
      }
      //Player two wins
      else if(playing.get(0).getValue() < playing.get(1).getValue()) {
        System.out.println("Player two wins the hand.");
        while(!playing.isEmpty()) {
          p2.add(playing.get(0));
          playing.remove(0);
        }
      }
      //The only remaining case is war
      else {
        System.out.println("A WAR HAS OCCURRED.");
        Thread.sleep(1500);
        //Makes sure that a war in the last few cards won't just crash the game.
        if(p1.size() > 4 && p2.size() > 4) {
          for(int i = 0; i < 3; i++) {
            playing.add(p1.get(0));
            p1.remove(0);
            playing.add(p2.get(0));
            p2.remove(0);
          }
        }
        //Should a player not have the required three bonus cards, it will put in all but one.
        else {
          while(p1.size() != 1 && p2.size() != 1) {
            playing.add(p1.get(0));
            p1.remove(0);
            playing.add(p2.get(0));
            p2.remove(0);
          }
        }
      }
      
      //Win conditions
      if(p1.size() == 52 && playing.isEmpty()) {
        System.out.println("Player one wins!");
        game = false;
      }
      else if(p2.size() == 52 && playing.isEmpty()) {
        System.out.println("Player two wins!");
        game = false;
      }
    }
  }
  
}
