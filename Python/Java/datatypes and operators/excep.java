import java.util.Scanner ;
public class excep{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        try{
            System.out.println("enter 2 numbers");
            int a= sc.nextInt();
            int b= sc.nextInt();
            int z=a/b;
            System.out.println(a + "divided by " + b + "gives:" + z);
        } catch(ArithmeticException ex){
            System.out.println(ex.toString());
        }finally{
            System.out.println("Application Designed & Developed by");
            System.out.println("team_yt");
            sc.close();
        }
        System.out.println("done");
    }
}