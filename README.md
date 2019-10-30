# CT-ErrorCorrectingCodes-Assignment-Year1
Durham University Computational Thinking Error Correcting Codes year 1 assignment.
This readme file briefly describes what each python file does.
A more in-depth specification can be found in the coursework specification pdf.
All functions written for the coursework are provided in the assignment.py file.
The test_format.py provides some tests to the functions defined in the assignment.py file.
Any functions not described here are given as part of the assignment.
1) message(a) where a is a vector of any positive lenght, converts the vector to a message for
   a Hamming code (a vector of lenght (2^r)-r-1 where r>=2).
2) hammingEncoder(m) where m is a message for a Hamming code, encodes m into a Hamming code.
3) hammingDecoder(v) where v is a Hamming code, decoder for Hamming codes.
4) messageFromCodeword(c) where v is a vector of lenght (2^r)-1 where r>=2, recovers the message from the codeword of a Hamming code.
5) dataFromMessage(m) where m is a message for a Hamming code, recovers the raw data from the message.
6) repetitionEncoder(m,n) where m is a vector of lenght 1 and n is a positive integer, encoder for repetition codes.
7) repetitionDecoder(v) where v is a vector of any positive lenght, decoder for repetition codes.
