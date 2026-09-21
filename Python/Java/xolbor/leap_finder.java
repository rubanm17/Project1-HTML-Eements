package xolbor;

import java.util.Scanner;

class leap_finder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the year: ");
        int year = sc.nextInt();

        String result = (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
                ? "Leap Year"
                : "Not a Leap Year";

        System.out.println(result);
    }
}
