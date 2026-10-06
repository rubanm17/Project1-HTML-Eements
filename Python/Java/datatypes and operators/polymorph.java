class Hiilstation{
    void location(){
        System.out.println("Location is:");
    }
    void famousefor()
    {
        System.out.println("Famous for:");
    }
}
class manali extends Hiilstation{
    void location(){
        System.out.println("mussorie is in Utharkhand");
    }
    void famousefor(){
        System.out.println("It is famouse for education institutions");
    }
}
class gulmarg extends Hiilstation{
    void location(){
        System.out.println("gulmarg is in JMk");
    }
    void famousefor(){
        System.out.println("It is famouse for skeeing");
    }
}
class polymorph{
    public static void main(String args[]){
        Hiilstation A = new Hiilstation();
        Hiilstation B = new manali();
        Hiilstation C = new gulmarg();
        A.location();
        A.famousefor();
        B.location();
        B.famousefor();
        C.location();
        C.famousefor();
    }
}