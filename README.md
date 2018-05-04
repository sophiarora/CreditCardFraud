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
To solve the problem of GBM requiring large memory and much time, xgboost improved both the algorithm and system design to enable scale solution for gradient boosting trees[1]. At the algorithm level, instead of using exact greedy method, xgboost uses approximation algorithms. Exact greedy methods tried every split to find the one that maximize information gain. Approximation consider the distribution of the data and instead trying buckets of split points. Xgboost also utilize weighted quantile sketch to make ranking the datas much easier. Because ranking and soring the data is an important step to propose ideal split point. Finally, at algorithm level, sparity-aware split was implemented to tackle problems encounter when there are many missing values/categorical dataset with lots of levels.

At system level, column blocks were enabled for parallel learning. Instead of sortting the entire dataset, xgboost divided data into blocks and then sort them. Xgboost also implemented cache-aware access and blocks for out-of-core Computation to reduce memory and processing burdens.

## LightGBM

XGBoost provides speedy fitting and prediction for large and complex dataset. LightGBM further improve the algorithm to try and enhance model performance[2].

LightGBM utilized a new method called one-side sampling. One-side sampling keeps all the the instances with large gradient and randomly samples from instances with small gradient. LightGBMG also utilize feature bundling to combine features that mutually exclusive in sparsity(never take zeros together) and thus reduce data dimensions.

## Reference

[1] Chen, T., & Guestrin, C. (2016). XGBoost. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining - KDD 16. Retrieved from [Link](http://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf)

[2]Guolin Ke, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. [LightGBM: A Highly Efficient Gradient Boosting Decision Tree](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf). In Advances in Neural Information Processing Systems (NIPS), pp. 3149-3157. 2017.
