How to use can refer to:
D:
cd C:\Users\Administrator.OS-201709041456\Desktop\ACP_Fuse
java -jar run.jar ACP_mixed_test.fasta


note:
1.The input file format requires the fasta format:
>P_1
ARPAKAAATQKKVERKAPDA
>N_1
TVEIVMGLEEEFQISVE
The positive case label defaults to 0, and the negative case label defaults to 1; or the label can be defined by the symbol "|".
>P_1|1
ARPAKAAATQKKVERKAPDA
>N_1|0
TVEIVMGLEEEFQISVE
2.The space character cannot appear in the specified cd path.
3.The input sequence should not be less than 10, and each sequence should be longer than 5.
4.Need to be in the windows operating system, install the java environment  and python2.7  environment.

Then the result is as follows:
1.We display the results of the best features in the Optimal_feature.csv file and provide complete results of the relevant functions obtained by the SFS method in the Result_FT.csv file, allowing the user to select the best features.
(The related feature descriptors obtained using the SFS method are located in its subfolder / New_feature / FT_arff)
2.There are 99 independent feature descriptors in the base feature pool in the arff_out folder.
3.In the New_feature file, there is the mrmR score file FT.mrmrout and the feature extraction first step file FTC.arff.

