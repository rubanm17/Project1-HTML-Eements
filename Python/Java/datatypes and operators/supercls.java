class scls{
    int num=56;
}
class cls extends scls{
    int num=96;
    void printNumber(){
        System.out.print(num);
    }
}
class supercls{
    public static void main(String[] args) {
        cls s = new cls();
        s.printNumber();
    }
}