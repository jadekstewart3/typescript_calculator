 import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    String[] weekDays = {"monday", "teusday", "wednesday", "thursday", "friday", "saturday", "sunday"};
    float[] temps = new float[7];
    boolean running = true;
    String userInput;
    float total = 0.0;
    float average = 0.0;
    int index;

    Scanner scnr = new Scanner(System.in);

    while(running){
      System.out.println("Enter a day of the week, 'week' for the weekly report, or 'quit' to exit: ");
      userInput = scnr.nextLine().trim();
      if (userInput.equalsIgnoreCase("quit")){
        running = false;
        System.out.println("Goodbye!");
        break;
      } else if(userInput.equalsIgnoreCase("week")){
        for(index = 0; index < weekDays.length; index++){
          for(index = 0; index < temps.length; index++){
            System.out.println(weekDays[index] + ": " + temps[index] + "F");
          }
        }
      }
    }

    private static int weeklyTempAverage(array temps){
      
    }
  }
}