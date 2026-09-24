class Animal {
    void eat(){
        System.out.println("eating..parent-Class..eat method");
    }
}
class lion extends Animal{
    void roar(){
        System.out.println("Roar..class-lion..roar method");
    }
}
class babylion extends lion{
    void observe(){
        System.out.println("observe..babylion-class..observe method");
    }
}
class multicls{
    public static void main(String args[]){
        babylion obj= new babylion();
        obj.observe();
        obj.roar();
        obj.eat();
    }
}