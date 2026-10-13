import java.util.Scanner;

public class candidatefinder {
    public static candidate getcandidatedetails()throws InvalidInternException{
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the candidate details");
        System.out.println("Name:");
        String name = sc.next();
        System.out.println("gender:");
        String gender = sc.next();
        System.out.println("percentage in attendence:");
        int percentage = sc.nextInt();

     if (percentage<75){
        throw InvalidInternException("Registration Failed.");
        }else{
            candidate Candidate = new candidate();
            Candidate.setName(name);
            Candidate.setGender(gender);
            Candidate.setPercentage(percentage);

            return Candidate;
        }
    }
    public static void main(String args[]){
        System.out.println("Welcome to InternHiring");
        try{
        candidate Candidate = new candidate();
        System.out.println("Registration complete");
        }catch (InvalidInternException e)
        {
            System.out.println(e.getMessage())
        }
    }
}
