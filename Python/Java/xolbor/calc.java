
package xolbor;

import java.util.Scanner;

class Calculator {
    int a, b;

    void add() {
        System.out.println("Addition = " + (a + b));
    }

    void subtract() {
        System.out.println("Subtraction = " + (a - b));
    }
}

class MyCalculator extends Calculator {
    void multiply() {
        System.out.println("Multiplication = " + (a * b));
    }

    void divide() {
        if (b != 0) {
            System.out.println("Division = " + (a / (double)b));
        } else {
            System.out.println("Cannot divide by zero");
        }
    }
}

public class calc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        MyCalculator c = new MyCalculator();

        System.out.print("Enter two numbers: ");
        c.a = sc.nextInt();
        c.b = sc.nextInt();

        c.add();
        c.subtract();
        c.multiply();
        c.divide();

        sc.close();
    }
}
