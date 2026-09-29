package xolbor;

import java.util.Scanner;

class add {
    void a(int num1 , int num2){
        int sum = num1 + num2;
        System.out.println("The Addition of" + num1 + "and" + num2 + "is" + sum );
    }
}
class sub {
    void b(int num1 ,int num2){
        int sb = num2 - num1 ;
        System.out.println("The Subtraction of" + num2 + "and" + num1 +"is" + sb );
    }
}
class mul{
    void c(int num1 , int num2){
        int ml = num1 * num2;
        System.out.println("The Multiplication of" + num2 + "and" + num1 +"is" + ml );
    }
}
class div{
    void d(int num1, int num2){
        int dv = num2 / num1;
        System.out.println("The Divsion of" + num2 + "and" + num1 +"is" + dv );
    }
}
class calc {
    public static void HW(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the first number");
        int num1 = sc.nextInt();
        System.out.println("enterv the second number");
        int num2 = sc.nextInt();
        System.out.println("What method do you want to use");
    }
}