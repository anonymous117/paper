### Info
 
To evaluate the accuracy of the single parameter modeler we use two different approaches:
 
First, we analyze the scaling of a model at the next measurement point for x that was not used for modeling. Since we used x={4,8,16,32,64,128} for modeling this point is x=256. Then we check if the predicted value at this point is within noise (+-5%), 2x, 3x, 4x and 5x times the noise. 5x noise equals a divergence of +-25% to the actual measured value. If this is the case then we count the model as correct. Furthermore, we also check the scaling at the next point of x which is x=512. Each plot presentes the number of correct models, considering different noise bands, at a specific point with a different number of repetitions R={1,2,3,4,5,6,7}.
 
Second, we analyze the model correctness by taking a look at the correctly identified function terms. As we have only 1 term for functions with 1 model parameter, the model is either correct or incorrect. The plot shows the number of correct models depending on the number of repetitions when using 6 points for modeling the behaviour of parameter x.