class Result {

    /*
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */
    public static String timeConversion(String s) {
    // Parse the hour and suffix (AM/PM)
    int hour = Integer.parseInt(s.substring(0, 2));
    String pm_am = s.substring(s.length() - 2);
    String restOfString = s.substring(2, s.length() - 2);

    if (pm_am.equals("PM")) {
        if (hour != 12) { // To handle 12 PM properly, where no addition of 12 is required
            hour += 12;
        }
    } else if (hour == 12) { // Adjusting 12 AM to 00:00
        hour = 0;
    }

    // Format the hour to ensure it is two digits
    String formattedHour = String.format("%02d", hour);
    return formattedHour + restOfString;
}

}