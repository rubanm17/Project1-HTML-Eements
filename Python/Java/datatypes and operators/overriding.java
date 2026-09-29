class small{
    public void sayHello(){
        System.out.println("I'm hacking guys!");
    } 
}
class large extends small {
    @Override 
    public void sayHello(){
        System.out.println("I'm hacking broooo!");
    }
}                                                                   
class overriding{
    public static void main(String[] args) {
        small s= new large();
        s.sayHello();
    }
}