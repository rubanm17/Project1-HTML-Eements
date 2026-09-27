package xolbor;


import java.util.Scanner;

class report_card {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Roll Number: ");
        int roll = sc.nextInt();

        System.out.print("Enter Semester: ");
        int semester = sc.nextInt();

        System.out.print("Enter marks in English: ");
        int english = sc.nextInt();

        System.out.print("Enter marks in Maths: ");
        int maths = sc.nextInt();

        System.out.print("Enter marks in Science: ");
        int science = sc.nextInt();

        System.out.print("Enter marks in Computer: ");
        int computer = sc.nextInt();

        int total = english + maths + science + computer;
        double percentage = total / 4.0;

        System.out.println("\n===== REPORT CARD =====");
        System.out.println("Student Name: " + name);
        System.out.println("Roll Number: " + roll);
        System.out.println("Semester: " + semester);
        System.out.println("-----------------------");
        System.out.println("English: " + english);
        System.out.println("Maths: " + maths);
        System.out.println("Science: " + science);
        System.out.println("Computer: " + computer);
        System.out.println("-----------------------");
        System.out.println("Total Marks: " + total + "/400");
        System.out.println("Percentage: " + percentage + "%");

        
        sc.close();
    }
}