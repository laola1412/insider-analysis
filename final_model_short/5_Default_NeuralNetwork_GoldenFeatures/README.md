# Summary of 5_Default_NeuralNetwork_GoldenFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
average_precision

## Training time

1.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.421589 |  nan        |
| auc       | 0.798388 |  nan        |
| f1        | 0.526316 |    0.220877 |
| accuracy  | 0.874346 |    0.295476 |
| precision | 1        |    0.691414 |
| recall    | 1        |    0        |
| mcc       | 0.443961 |    0.282211 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.421589 |  nan        |
| auc       | 0.798388 |  nan        |
| f1        | 0.5      |    0.295476 |
| accuracy  | 0.874346 |    0.295476 |
| precision | 0.585366 |    0.295476 |
| recall    | 0.436364 |    0.295476 |
| mcc       | 0.435956 |    0.295476 |


## Confusion matrix (at threshold=0.295476)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |              310 |               17 |
| Labeled as 1 |               31 |               24 |

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
