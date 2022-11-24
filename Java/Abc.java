/*
* Dev: Prajwal Nautiyal
* Last Update: 8 November 2022
* A Basic Calculator
*/

// Importing the java.util package to use the Scanner class
import java.util.Scanner;

class Abc {                                                         // Declaring a class named Abc
    static Scanner sc = new Scanner(System.in);                     // Creating a Scanner object
    public static void main(String args[]) {
        do {                                                        // Infinite loop to keep the program running until the user presses Ctrl+C
            try {
                double out[] = new double[3];
                out = Abc.calc();                                   // Calling the calc function and storing the returned value in the variable 'out'
                Abc.output(out[0], out[1], (int) out[2], out[3]);   // Calling the output function
                System.out.println("Press Ctrl+C to exit");         // Printing a message to the user to press Ctrl+C to exit the program
            } 
            catch (Exception e) {
                if (e instanceof java.util.InputMismatchException) { // Checking if the exception is of type InputMismatchException
                    System.out.println("Invalid Input");            // Printing a message to the user that the input is invalid
                } 
                else if (e instanceof java.lang.ArithmeticException) { // Checking if the exception is of type ArithmeticException
                    System.out.println("Cannot divide by zero");    // Printing a message to the user that the input is invalid
                } 
                else if (e instanceof java.util.NoSuchElementException){
                    System.out.println("Program Terminated");       // Printing an exit message
                }
            }
        }while (true);                                              // Infinite loop 
    }

    static int[] input() {                                          // This function will take input from the user and return an array of integers
        int arr[] = new int[2];                                     // Declaring an array of integers with size 3 to store the input
        System.out.println("Enter first value:");
        arr[0] = sc.nextInt();                                      // Taking input from the user for the first element
        System.out.println("Enter second value:");
        arr[1] = sc.nextInt();                                      // Taking input from the user for the second element
        return arr;                                                 // Returning the array
    }

    static double[] calc() {                                        // This function will perform the calculation and return the result; 'a' is the first value, 'b' is the second value and 'c' is the operator choice
        System.out.println("Choose,\n1 for Addition (+)\n2 for Substraction (-)\n3 for Multiplication (*)\n4 for Division (/)\n5 for Modulus (%)\n6 for Power (^)\n7 to Exit");
        int c = sc.nextInt();                                       // Taking input from the user for the operator choice
        int arr[] = new int[2];                                     // Declaring an array of integers with size 2 to store the input
        double out[] = new double[4];                               // Declaring an array of integers with size 4 to store the output
        double val;                                                 // Declaring a variable to store the result
        switch (c) {                                                // Switch case to perform the calculation as per the user's choice of operator from the menu
            case 1:                                                 // Addition
                arr = input();                                        
                val = arr[0] + arr[1];
                break;
            case 2:                                                 // Substraction
                arr = input();                                        
                val = arr[0] - arr[1];
                break;
            case 3:                                                 // Multiplication
                arr = input();
                val = arr[0] * arr[1];
                break;
            case 4:                                                 // Division
                arr = input();
                val = arr[0] / arr[1];
                break;
            case 5:                                                 // Modulus
                arr = input();
                val = arr[0] % arr[1];
                break;
            case 6:                                                 // Power
                arr = input();
                val = (Double) Math.pow(arr[0], arr[1]);
                break;
            case 7:                                                 // Exit
                System.out.println("Program Terminated");            // Printing an exit message
                System.exit(0);                                     // Exiting the program
            default:                                                // If the user enters a choice other than 1, 2, 3 or 4
                val = 0;
                break;
        }
        out[0] = arr[0];
        out[1] = arr[1];
        out[2] = c;
        out[3] = val;
        return out;                                                 // Returning the result
    }

    static void output(double a, double b, int op, double res) {    // This function will print the approppriate result depending on the operator 'op',  'a' and 'b' are the user inputted values and 'res' is the result
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
            case 5:                                                 // Output for modulus
                System.out.println("The remainder when " + a + " is divided by " + b + " is " + res);
                break;
            case 6:                                                 // Output for power
                System.out.println(a + " raised to the power " + b + " is " + res);
                break;
            default:                                                // If the user enters a choice other than 1, 2, 3 or 4
                System.out.println("Invalid choice");
                break;
        }
    }
}