import java.util.HashSet;
import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class GenerateLMN {
	
	public static final String file = "C:\\Seshasai\\NEU_MSCS_Course\\Spring2017\\MachineLearning\\repos\\repo1\\kattaseshasai09\\Assignment3\\data\\N10of100of1000.txt";
	

    public static int l = 10;
    public static int m = 100;
    public static int n = 1000;
    
    public static int instances = 50000;
    
    public static double labelNoise = 0.05;	// 0.05 for part 3
    public static double featureNoise = 0.001;	// 0.001 for part 3
    public static double irrelevantActive = 0.5;	// probability of irrelevant feature being active
    public static double labelRatioPos = 0.5;		// ratio of postive to negative labels
    
    public static long rngSeed = 239485235295L;
    //public static long rngSeed = System.currentTimeMillis();
    
    public static void main(String[] args)throws Exception {
	
	Random rng = new Random(rngSeed);
	
	BufferedWriter bw = null;
	FileWriter fw = null;
	
	int positive = (int) Math.ceil((double) instances * labelRatioPos); 
	int negative = instances - positive;
	//System.out.println(positive + "," + negative);
	
	int current_pos = 0;
	int current_neg = 0;
	
	//System.out.println(generatePositions(rng,3,5));
	
	//System.exit(0);
	try{
		fw = new FileWriter(file);
		bw = new BufferedWriter(fw);
	
	while ((current_pos < positive) || (current_neg < negative)) {
	    if ((current_neg < negative) && 
		((current_pos >= positive) ||
		 (rng.nextDouble() >= labelRatioPos))) {
		generateNegative(rng,bw);
		current_neg++;
	    }
	    else {
		generatePositive(rng,bw);
		current_pos++;
	    }
	}
	//System.out.println(current_pos + "," + current_neg);
    }
	catch(Exception e){
		System.out.println(e);
	
	}finally{
		bw.close();
		fw.close();
	}
	}	
    
    public static void generatePositive(Random rng,BufferedWriter bw) throws Exception {
	int num_active = rng.nextInt(m-l+1) + l;
	//System.out.println(num_active);
	if (rng.nextDouble() < labelNoise){
	    System.out.print("-");
		bw.write("-");
	}
	else{
	    System.out.print("+");
		bw.write("+");
	}
	System.out.print("1");
	bw.write("1");
	HashSet<Integer> active = generatePositions(rng, num_active, m);
	for (int i = 1; i <= m; i++) {
	    double fNoise = rng.nextDouble();
	    if ((active.contains(i) && (fNoise >= featureNoise)) ||
		(!active.contains(i) && (fNoise < featureNoise))){
		System.out.print(" " + i + ":1");
		bw.write(" " + i + ":1");
		}
        }
	for (int i = (m + 1); i <= n; i++) {
	    double fNoise = rng.nextDouble();
	    if (((fNoise < irrelevantActive) &&
		 (rng.nextDouble() >= featureNoise)) ||
		((fNoise >= irrelevantActive) &&
		 (rng.nextDouble() < featureNoise))){
		System.out.print(" " + i + ":1");
		bw.write(" " + i + ":1");
		 }
	}
	System.out.println();
	bw.write("\n");
    }
	
    
    public static void generateNegative(Random rng,BufferedWriter bw) throws Exception {
	int num_active = rng.nextInt(l);
	//System.out.println(num_active);
	if (rng.nextDouble() < labelNoise){
	    System.out.print("+");
		bw.write("+");
	}
	else{
	    System.out.print("-");
		bw.write("-");
	}
	System.out.print("1");
	bw.write("1");
	HashSet<Integer> active = generatePositions(rng, num_active, m);
	for (int i = 1; i <= m; i++) {
	    double fNoise = rng.nextDouble();
	    if ((active.contains(i) && (fNoise >= featureNoise)) ||
		(!active.contains(i) && (fNoise < featureNoise))){
		System.out.print(" " + i + ":1");
		bw.write(" " + i + ":1");
		}
	}
	for (int i = (m + 1); i <= n; i++) {
	    double fNoise = rng.nextDouble();
	    if (((fNoise < irrelevantActive) &&
		 (rng.nextDouble() >= featureNoise)) ||
		((fNoise >= irrelevantActive) &&
		 (rng.nextDouble() < featureNoise))){
		System.out.print(" " + i + ":1");
		bw.write(" " + i + ":1");
		 }
	}
	System.out.println();
	bw.write("\n");
    }
    
    public static HashSet<Integer> generatePositions(Random rng, int a, int m) {
	HashSet<Integer> result = new HashSet<Integer>();
	int remainder = a;
	int possible = m;
	for (int i = 1; i <= m; i++) {
	    if (rng.nextDouble() < ((double) remainder / possible)) {
		result.add(i);
		remainder--;
	    }
	    possible--;
	}
	return result;
    }
}
