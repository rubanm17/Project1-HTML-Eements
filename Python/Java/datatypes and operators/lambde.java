import java.util.ArrayList;
class lamde{
    public static void main(String[] args) {
        System.out.println("--------lambdas-----------");
        ArrayList<Integer> num = new ArrayList<>();
        num.add(23);
        num.add(68);
        num.add(67);
        num.add(99);
        num.forEach( (x) -> {System.out.println(x) ;} );
        num.forEach(n -> {if (n == 67) System.out.println("dont say 67");});
    }
}