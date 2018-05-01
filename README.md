# CreditCardFraud
predictive modeling on Credit Card Fraud Dataset from [Kaggle Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)
In this reporsitory I plan to utilize the credit card fraud dataset to explore tree algorithms including random forest, GBM, xgboost and lightGBM
I will also explore the use of DNN using keras.

Tree models are very popular and powerful in supervised learning. The family of tree algorithms includes decision tree algorithms, random forest(ensemble), Gradient Boosting and the current most popular and powerful lightGBM and xgboost algorithms.

## From Decistion Tree to Random Forest
Decision Tree algorithm is based on the concept of [information gain](https://en.wikipedia.org/wiki/Information_gain_in_decision_trees). While decision tree algorithm is very powerful, it might produce overfitting result. To improve the robustness of our model, random forest algorithm was introduced using bootstrap sampling and by splitting among a random set of features instead of all features([scikit learn reference](http://scikit-learn.org/stable/modules/ensemble.html)).

## Addictive Training using Gradient Boost
Random Forest algorithm is certainly very powerful, but it does not learn from its own mistakes through all the iterations. Gradient Boosting utilized weak learners to addictively search for optimized solutions([Boosed Tree](https://homes.cs.washington.edu/~tqchen/pdf/BoostedTree.pdf)). The main dropback of GBM is that training could take lots of time and memory. In fact for large datasets with sparse data, GBM will take too long to return meaningful result.

## XGBoost acceleration and better
To solve the problem of GBM requiring large memory and much time, xgboost improved both the algorithm and system design to enable scale solution for gradient boosting trees[1]. 







## Reference

[1] Chen, T., & Guestrin, C. (2016). XGBoost. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining - KDD 16. Retrieved from[Link](http://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf)
