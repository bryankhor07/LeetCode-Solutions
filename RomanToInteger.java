class Solution {
    public int romanToInt(String s) {
        int sum = 0;
		
		    for (int i = s.length() - 1; i >= 0; i--) {
			    if (s.charAt(i) == 'I') {
				    sum += 1;
			    } 
			    if (s.charAt(i) == 'V') {
				    sum += 5;
				    if (i != 0) {
					    if (s.charAt(i - 1) == 'I') {
						    sum -= 1;
						    i--;
					    }
				    }	
			    }
			    if (s.charAt(i) == 'X') {
				    sum += 10;
				    if (i != 0) {
					    if (s.charAt(i - 1) == 'I') {
						    sum -= 1;
						    i--;
					    }
				    }
			    }
			    if (s.charAt(i) == 'L') {
				    sum += 50;
				    if(i != 0) {
					    if (s.charAt(i - 1) == 'X') {
						    sum -= 10;
						    i--;
					    }
				    }
			    }
			    if (s.charAt(i) == 'C') {
				    sum += 100;
				    if (i != 0) {
					    if (s.charAt(i - 1) == 'X') {
						    sum -= 10;
						    i--;
					    }
				    }
			    }
			    if (s.charAt(i) == 'D') {
				    sum += 500;
				    if (i != 0) {
					    if (s.charAt(i - 1) == 'C') {
						    sum -= 100;
						    i--;
					    }
				    }
			    }
			    if (s.charAt(i) == 'M') {
				    sum += 1000;
				    if (i != 0) {
					    if (s.charAt(i - 1) == 'C') {
						    sum -= 100;
						    i--;
					    }
				    }
			    }
		    }
		    return sum;
    }
}
