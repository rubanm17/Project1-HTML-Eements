abstract class  Object{
    abstract void showShape();
    public void show(){
        System.out.println("I'm form abstract");
    }
}
class sphere extends Object{
    void showShape(){
        System.out.println("Sphere");
    }
}
class cube extends Object{
    void showShape(){
        System.out.println("cube");
    }
}
class pyramid extends Object{
    void showShape(){
        System.out.println("pyramid");
    }
}
class abstraction{
    public static void main(String[] args) {
        Object A = new sphere();
        A.showShape();
        A = new cube();
        A.showShape();
        A = new pyramid();
        A.showShape();
        A.show();
    }
}