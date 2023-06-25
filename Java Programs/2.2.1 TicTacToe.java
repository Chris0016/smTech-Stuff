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
# Module 2.2.1                    #
# - - - - - - - - - - - - - - - - #

SUMMERTECH CONFIDENTIAL
COPYRIGHT (C) 2017 SUMMERTECH, INC. ALL RIGHTS RESERVED
*/

import java.util.Scanner;
public class TicTacToe {
  
  public static void main(String[] args) {
    
    //Variable setup
    Scanner scan=new Scanner(System.in);
    char turn='X';
    char[][] board=new char[3][3];
    int count=0;
    
    //Set the board
    for(int i=0;i<3;i++) {
      for(int j=0;j<3;j++) {
        board[i][j]='-';
      }
    }
    
    while(count < 9) {
      //Print the board
      for(int i=0;i<3;i++) {
        for(int j=0;j<3;j++) {
          System.out.print(board[j][i]+" ");
        }
        System.out.println();
      }
      
      //Gameplay
      System.out.println("Player "+ turn +" what x coordinate would you like to play");
      int xcoord = scan.nextInt();
      System.out.println("Player "+ turn +" what y coordinate would you like to play");
      int ycoord = scan.nextInt();
      
      if(xcoord >= 0 && xcoord < 3 && ycoord >= 0 && ycoord < 3) {
        if(board[xcoord][ycoord] == '-') {
          board[xcoord][ycoord] = turn;
          if(turn == 'X')
            turn = 'O';
          else if(turn == 'O')
            turn = 'X';
          count++;
        }
        else {
          System.out.println("Invalid move.");
        }
      }
      else {
        System.out.println("Invalid move.");
      }
    }
    
    //Win conditions
    if(board[0][0] == turn && board[0][1] == turn && board[0][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[1][0] == turn && board[1][1] == turn && board[1][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[2][0] == turn && board[2][1] == turn && board[2][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[0][0] == turn && board[1][0] == turn && board[2][0] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[0][1] == turn && board[1][1] == turn && board[2][1] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[0][2] == turn && board[1][2] == turn && board[2][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[0][0] == turn && board[1][1] == turn && board[2][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    else if(board[2][0] == turn && board[1][1] == turn && board[0][2] == turn) {
      System.out.println(turn + " wins!");
      System.exit(0);
    }
    
    //Nine turns have gone and the game hasn't ended, must be a tie!
    System.out.println("It's a tie!");
  }
  
}
