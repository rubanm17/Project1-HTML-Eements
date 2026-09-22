class wo_rd {
    public static void main(String[] args) {
        String first="Cod";
        String last="ingnal";
        String word =first+last;
        String C_T="Welcome"+"To"+"Codingnal";
        String C_C=word.toUpperCase();
        String C_S=word.toLowerCase();

        int L_C = word.length();
        int L_CT=C_T.length();
        int sum=L_CT-L_C;

        System.out.println(word);
        System.out.println(C_T);
        System.out.println(C_C);
        System.out.println(C_S);
        System.out.println(L_C);
        System.out.println(L_CT);
        System.out.println(sum);
    }
}