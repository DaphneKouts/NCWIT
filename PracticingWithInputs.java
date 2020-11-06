
/**
 * 
 *
 * Daphne Koutsoukos and Sofia DiMaruo
 * 
 */
import java.io.*;
import java.util.*;
import java.lang.Math. *;
import java.awt.Rectangle;
public class PracticingWithInputs
{
public static void main(String args[])
{
    Scanner kb = new Scanner(System.in);
    System.out.println("Give me a number: ");
    String first = (kb.nextLine());
    int numFirst = Integer.parseInt(first);
    System.out.println("Give me another number: ");
    String second = (kb.nextLine());
    int numSecond = Integer.parseInt(second);
    System.out.println(numFirst * numSecond);
}
public static void goingInCircles()
{
    Scanner kb = new Scanner(System.in);
    System.out.println("Give me an area: ");
    String area = (kb.nextLine());
    double numArea = Double.parseDouble(area);
    System.out.println(Math.sqrt((numArea)/Math.PI));
}
public static void whatsMyName()
{
    Scanner kb = new Scanner(System.in);
    System.out.println("Give me your first name: ");
    String first = (kb.nextLine());
    System.out.println("Give me your last name: ");
    String last = (kb.nextLine());
    System.out.println("This is your full name: " + first + " " + last);
}
public static void rectangles()
{
  Rectangle rect1 = new Rectangle(4,5);
  rect1.grow(3,1); //We couldn't figure out how to grow the rectangle by by a double, or .5
  System.out.println("Height: " + rect1.getHeight() + " Width: " + rect1.getWidth());
 
}
}

