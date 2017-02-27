import java.util.ArrayList;

public class Reverse {
    public static void main(String[] theArgs) {
        System.out.println(reverseString(theArgs[0]));
    }

    public static String reverseString(String theString) {
        ArrayList<Character> chList = new ArrayList<Character>();
        for (int i = 0; i < theString.length(); i++) {
            chList.add(theString.charAt(i));
        }

        String reversed = "";

        for (int i = chList.size() - 1; i >= 0; i--) {
            reversed += chList.get(i);
        }
        return reversed;
    }
}