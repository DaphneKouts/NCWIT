/**
 * Practice with iteration assignment
 *
 * Daphne Koutsoukos
 */
import java.io.*;
import java.util.*;
public class ChristmasTree
{
public static void main(String [] args)
{
Scanner input = new Scanner(System.in);
System.out.println("Give me an integer greater than 1: ");
String userStr = input.nextLine();
int userint = Integer.parseInt(userStr);
if (userint%2 == 0)
{
  for (int rows = 1; rows <= userint; rows ++)
    {
        for (int col = 0; col < userint; col ++)
                System.out.print(col < userint - rows ? " " : "*");
        System.out.println();
    }  
}
else
{
 for (int rows = 1; rows <= userint; rows ++)
    {
        for (int col = 0; col < userint - rows; col ++)
            System.out.print(" ");
        for (int star = 1; star <= (2 * rows - 1); star ++)
            System.out.print("*");
        System.out.println();
    }
}
}
public static void project2(String[] args)
{
       Scanner userValues = new Scanner(System.in);
       System.out.println("Please tell me how many values : ");
       String valueStr = userValues.nextLine();
       int value = Integer.parseInt(valueStr);
       int odd = 0;
       int even = 0;
       int numValue = 0;       
       int max = 0;
       int oddmax = 0;
       for (int print = 0; print < value; print ++)
        {
           System.out.println("Enter your integers: ");
           String number = userValues.nextLine();
           numValue = Integer.parseInt(number);
           if ( numValue % 2 == 0) 
               even = even + 1;
           else
                {
                odd = odd + 1;
                if (print ==0)
                 oddmax = numValue;
                else
                    if (numValue > oddmax)
                       oddmax = numValue;
                }
           if (print ==0)
                max = numValue;
           else
                if (numValue > max)
                max = numValue;
        }
        System.out.println("The number of values is: " + value);
        System.out.println("The max value is " + max );
        if (even < odd)
        {
            System.out.println("There are " + odd + " odd numbers!");
        }
                
        else
            System.out.println("There are " + even + " even numbers!"); 
        if (oddmax == 0)
            System.out.println(" There are no odd integers");
        else
            System.out.println("The max odd number is " + oddmax);
}
public static void project3(String[] args)
{
    Scanner inputSequence = new Scanner(System.in);
    System.out.println("Insert the first and second values of a sequence in addition the number of values in the sequence you want printed seperated by commas: ");
    String full = inputSequence.nextLine();
    int comma1 = full.indexOf(",");
    String stringA1 = full.substring(0,comma1);
    int a1 = Integer.parseInt(stringA1);
    int comma2 = full.indexOf(",",comma1 + 1);
    String stringA2 = full.substring(comma1 + 1,comma2);
    int a2 = Integer.parseInt(stringA2);
    String stringN = full.substring(comma2 + 1);
    int n = Integer.parseInt(stringN);
    int nextN;
    System.out.print(a1 + " ");
    System.out.print(a2 + " ");
    for (int pos = 0; pos < n - 2; pos ++)
         {
          nextN = a1 + a2;
          a1 = a2;
          a2 = nextN;
          System.out.print(nextN + " ");
    }
}
public static void project4(String[] args)
{
Scanner givename = new Scanner(System.in);
System.out.println("Please enter your name: ");
String userName = givename.nextLine();
int nameLen = userName.length();
String backwardsName = "";
for (int index = 1; index <= nameLen; index ++)
    {
        backwardsName += (userName.substring(nameLen - index,nameLen - index + 1));
    }
backwardsName = backwardsName.toLowerCase();
System.out.println(backwardsName);
}
}
