class Main {
    public static void main(String[] args){
        int a=10;
        int b=5;
        System.out.println("Unary Operators" + (++a));
        System.out.println("Unary Operators" + (--b));
        System.out.println("Binary Operators");
        System.out.println("1+2 " + (1 + 2));
        int increment = ++a * b++;
        System.out.println(increment);
        System.out.println("Ternary Operator");
        int largestNumber=(a>b)?a:b; 
        System.out.println("Largest of 2 Numbers: " + largestNumber);
    }
}
