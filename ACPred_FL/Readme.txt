How to use can refer to:

C:
cd C:\Users\Administrator\Desktop\ACPred_FL
java -jar ACPFL_Seq.jar ACP_mixed_test.fasta
java -jar ACPFL_Result.jar ACP_mixed_test.fasta


The positive case label defaults to 0, and the negative case label defaults to 1; or the label can be defined by the symbol "|".
>P_1|1
ARPAKAAATQKKVERKAPDA
>N_1|0
TVEIVMGLEEEFQISVE
2.The space character cannot appear in the specified cd path.
3.The input sequence should not be less than 10, and each sequence should be longer than 5.
4.Need to be in the windows operating system, and install the java environment.


references:
