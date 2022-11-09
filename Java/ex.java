/*
 * Developer: Prajwal Nautiyal
 * Date: 8 November 2022
 * Tower of Hanoi using recursion
 */

import java.util.ArrayList;
import java.util.Scanner;

public class ex {
    
    static ArrayList<Character> getInput(){                                                             // This function will take input from the user and return an ArrayList of characters
        ArrayList<Character> arr = new ArrayList<Character>(4);                                         // This ArrayList will store the input
        int num;
        char src, dst, aux;
        try (Scanner sc = new Scanner(System.in)) {                                                     // This try-with-resources block will automatically close the Scanner object after the code inside the block is executed
            System.out.println("Enter the number of disces: ");
            num = sc.nextInt();
            arr.add(0,(char) num); 
            System.out.println("Enter the intial position of disces: ");
            src = sc.next().charAt(0);
            arr.add(1, src);
            System.out.println("Enter the destination of disces: ");
            dst = sc.next().charAt(0);
            arr.add(2, dst);
        }
        aux = (char) ((int)src + 1);                                                                    // This is the auxiliary tower
        arr.add(3, aux);
        return arr;
    }

    static void TowersOfHanoi(int n, char s, char d, char a){                                           // A recursive function to solve the problem
       if ((int) n == 1){
        System.out.println("Move disk 1 from " + s + " to destination " + d );
       }
       else{
        TowersOfHanoi(n-1, s, a, d);
        System.out.println("Move disk " + n + " from " + s + " to destination " + d);
        TowersOfHanoi(n-1, a, d, s);
       }
    }

    public static void main(String[] args) {
        ArrayList<Character> arr = new ArrayList<Character>(4);                                         // Declaring an ArrayList of characters to store the input
        arr = ex.getInput();                                                                            // Calling the getInput() function to take input from the user
        ex.TowersOfHanoi((int)arr.get(0), arr.get(1), arr.get(2), arr.get(3));                          // Calling the TowersOfHanoi() function to solve the problem
    }
}
