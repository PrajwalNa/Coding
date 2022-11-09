/*
* Dev: Prajwal Nautiyal
* Last Update: 8 November 2022
* A Basic Calculator
*/

import java.util.*;                                                 // Importing the java.util package to use the Scanner class

class Abc {                                                         // Declaring a class named Abc

    static int[] input() {                                          // This function will take input from the user and return an array of integers
        int arr[] = new int[3];                                     // Declaring an array of integers with size 3 to store the input
        try (Scanner sc = new Scanner(System.in)) {                 // This try-with-resources block will automatically close the Scanner object after the code inside the block is executed
            System.out.println("Enter first value:");
            arr[0] = sc.nextInt();                                  // Taking input from the user for the first element
            System.out.println("Enter second value:");
            arr[1] = sc.nextInt();                                  // Taking input from the user for the second element
            System.out.println("Choose,\n1 for Addition (+)\n2 for Substraction (-)\n3 for Multiplication (*)\n4 for Division (/)");
            arr[2] = sc.nextInt();                                  // Taking input from the user for the operator
        }
        return arr;                                                 // Returning the array
    }

    static float calc(int a, int b, int c) {                        // This function will perform the calculation and return the result; 'a' is the first value, 'b' is the second value and 'c' is the operator choice
        float val;                                                  // Declaring a variable to store the result
        switch (c) {                                                // Switch case to perform the calculation as per the user's choice of operator from the menu
            case 1:                                                 // Addition
                val = a + b;
                break;
            case 2:                                                 // Substraction
                val = a - b;
                break;
            case 3:                                                 // Multiplication
                val = a * b;
                break;
            case 4:                                                 // Division
                val = a / b;
                break;
            default:                                                // If the user enters a choice other than 1, 2, 3 or 4
                val = 0;
                break;
        }
        return val;
    }

    static void output(int a, int b, int op, float res) {           // This function will print the approppriate result depending on the operator 'op',  'a' and 'b' are the user inputted values and 'res' is the result
        switch (op) {                                               // Switch case to print the result as per the user's choice of operand from the menu
            case 1:                                                 // Output for addition
                System.out.println("The sum of " + a + " and " + b + " is " + res);
                break;
            case 2:                                                 // Output for substraction
                System.out.println("The difference between " + a + " and " + b + " is " + res);
                break;
            case 3:                                                 // Output for multiplication
                System.out.println("The product of " + a + " and " + b + " is " + res);
                break;
            case 4:                                                 // Output for division
                System.out.println("The result of dividing " + a + " and " + b + " is " + res);
                break;
            default:                                                // If the user enters a choice other than 1, 2, 3 or 4
                System.out.println("Invalid choice");
                break;
        }
    }

    public static void main(String args[]) {
        try {                                                       // This try block will execute the code inside it and if the keyboard interrupt exception is thrown, the catch block will execute
            while (true) {                                          // Infinite loop to keep the program running until the user presses Ctrl+C
                int ar[] = new int[3];                              // Declaring an array of integers with size 3 to store the input
                ar = Abc.input();                                   // Calling the input function and storing the returned array in the array 'ar'
                float out = Abc.calc(ar[0], ar[1], ar[2]);          // Calling the calc function and storing the returned value in the variable 'out'
                Abc.output(ar[0], ar[1], ar[2], out);               // Calling the output function
                System.out.println("Exit: Ctrl+C.");             // Printing the message to exit the program
            }
        } 
        catch (Exception keyBoardException) {                       // This catch block will execute if the keyboard interrupt exception is thrown
            System.out.println("Program Closing.");              //Exit message
        }
    }
}