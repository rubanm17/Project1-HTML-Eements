import java.util.*;

class grading{
    public static void main(String[] args) {
        int sum=0;
        String result;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your no of subjects: ");
        int noofSubjects = sc.nextInt();
        int marks[] = new int[noofSubjects];
        System.out.println("Enter your marks: ");
        System.out.println("Enter the marks of" + noofSubjects + " subjects.Press Enter to give marks for another subject.");
        for(int i=0;i<noofSubjects;i++){
            marks[i] = sc.nextInt();
        }
        for(int j=0;j<noofSubjects;j++){
            sum = sum + marks[j];
        }
        int percentage = sum/noofSubjects;
        System.out.println("Your percentage is: " + percentage);
        if(percentage>=95){
            result = "A+";
        }
        else if(percentage>=90){
            result = "A";
        }
        else if(percentage>=80){
            result = "B+";
        }
        else if(percentage>=70){
            result = "B";
        }
        else if(percentage>=60){
            result = "C+";
        }
        else if(percentage>=50){
            result = "C";
        }
        else{
            result = "Fail";
        }
        System.out.println("Your grade is: " + result);
    }
}