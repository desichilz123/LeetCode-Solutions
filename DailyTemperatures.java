class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] dailyTemperatures = new int[temperatures.length];
        for (int i = temperatures.length - 1; i >= 0; i--) {
            int j = i + 1;
            while (j < temperatures.length) {
                if (temperatures[j] > temperatures[i]) {
                    dailyTemperatures[i] = j - i;
                    break;
                } else if (temperatures[j] == temperatures[i]) {
                    if (dailyTemperatures[j] != 0) {
                        dailyTemperatures[i] = dailyTemperatures[j] + j - i;
                    } else {
                        dailyTemperatures[i] = 0;
                    }
                    break;
                }
                j++;
            }
            if (j == temperatures.length) {
                dailyTemperatures[i] = 0;
            }
        }
        return dailyTemperatures;
    }
}