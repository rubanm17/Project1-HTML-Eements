import java.util.*;

class user_input {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter your name: ");
        String n = sc.nextLine();
        System.out.println("Enter your lucky number: ");
        int luckyNumber = sc.nextInt();
        System.out.println("The name you entered is: " + n);
        System.out.println("The lucky number you entered is: " + luckyNumber);

    }
}