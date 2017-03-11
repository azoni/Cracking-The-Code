/**
 * Reverse a string.
 * @author Garrett
 * @version 1.0
 */
public class ReverseString {

  // Main method.
  // @param theArgs command line arguments
  public static void main(String[] thArgs) {
    String reversed = reverseString("Hello");
    System.out.println(reversed);
  }

  // Returns a reversed version of the given string.
  // @param theString a valid string
  // @return a reversed version of the given string
  public static String reverseString(String theString) {
    StringBuilder reversed = new StringBuilder();

    if (theString.length() == 0 || theString.length() == 1) {
      return theString;
    } else {
      for (int i = theString.length() - 1; i >= 0; i--) {
        reversed.append(theString.charAt(i));
      }
    }

    return reversed.toString();
  }
}
