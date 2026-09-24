class Plants{
    void food(){
        System.out.println("food by photosynthesis-parent-Class");
    }
}
class leaf extends Plants{
    void kitchen(){
        System.out.println("The kitchen of a plant-Child-Class");
    }
}
class chloroplast extends leaf{
    void process(){
        System.out.println("The reactor for food-2xChild-Class");
    }
}
class heirarcy{
    public static void main(String args[]){
        
    }
}