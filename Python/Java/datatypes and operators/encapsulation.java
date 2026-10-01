class zeno {
    private String name;
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
}
class encapsulation{
    public static void main(String args[]){
        zeno z=new zeno();
        z.setName("OmniKing");
        System.out.println(z.getName());
    }
}