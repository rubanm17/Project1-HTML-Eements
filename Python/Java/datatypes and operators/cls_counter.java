class cls {
    int number = 10;
    void increment(){
        number = number+1;
    }
public static void main(String[] args) {
    cls obj1 = new cls();    
    cls obj2 = new cls();
    cls obj3 = new cls();
    
    obj1.increment();
    obj2.increment();
    obj3.increment();

    System.out.println(obj1.number);
    System.out.println(obj2.number);
    System.out.println(obj3.number);
}
}