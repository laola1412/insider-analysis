# Summary of 6_Default_RandomForest_KMeansFeatures_RandomFeature

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: average_precision
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
average_precision

## Training time

3.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.357305 | nan         |
| auc       | 0.886036 | nan         |
| f1        | 0.695652 |   0.491777  |
| accuracy  | 0.861257 |   0.55245   |
| precision | 0.933333 |   0.878199  |
| recall    | 1        |   0.0599909 |
| mcc       | 0.607499 |   0.55245   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.357305 |   nan       |
| auc       | 0.886036 |   nan       |
| f1        | 0.682635 |     0.55245 |
| accuracy  | 0.861257 |     0.55245 |
| precision | 0.802817 |     0.55245 |
| recall    | 0.59375  |     0.55245 |
| mcc       | 0.607499 |     0.55245 |


## Confusion matrix (at threshold=0.55245)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              272 |               14 |
| Labeled as 1 |               39 |               57 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
