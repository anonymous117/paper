### Info

Notes for the evaluation:

- The evaluation data has n=5% noise in both directions, effectively 10%.
- A model is correct when the divergence between the actual and predicted value at the scaling point P(x,y,z) is smaller than the percentage of noise.
- Additionally we invetigate if the predicted value is within e.g. 2x percent of noise.
- N=1x means we check if the prediction is within the base 5% of noise. N=2x means within 10% noise in both directions.
- The title of the plot also indicates for which axes and the specific point the scaling was checked.
- The parameter values we use for the evaluation are x=[4,8,16,32,64], y=[10,20,30,40,50], z=[2,4,6,8,10].
- For the evaluation of the scaling we go to the next and second next point in the row of an axis or all axis after the maximum point we use for modeling. E.g. p=64 -> p=128, P=256.

