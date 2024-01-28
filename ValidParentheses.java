class Solution {
    Map<Character, Character> map = new HashMap<>() {{
    put(']','[');
    put(')','(');
    put('}','{');
    }}; 
    public boolean isValid(String s) {
        if (s.length() == 0) {
            return true;
        }
        Stack<Character> stack = new Stack();
        for (int i = 0; i < s.length(); i++) {
            System.out.println(stack.size());
            if (stack.size() > 0 && map.containsKey(s.charAt(i)) && map.get(s.charAt(i)).equals(stack.peek())) {
                stack.remove(stack.size() - 1);
            }
            else {
                stack.add(s.charAt(i));
            }
        }
        return stack.size() == 0;
    }
}