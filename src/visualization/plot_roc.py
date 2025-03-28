import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve

def plot_roc_auc(model, X_test, y_test, model_name="Model"):
    """
    Plots the ROC curve and prints AUC score for a given model.

    Parameters:
        model: Trained classifier with predict_proba or decision_function
        X_test: Test features
        y_test: True labels for test data
        model_name (str): Custom title for the ROC curve
    """
    # Get prediction scores
    try:
        y_scores = model.predict_proba(X_test)[:, 1]
    except AttributeError:
        y_scores = model.decision_function(X_test)

    # Compute ROC curve and AUC
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    auc_score = roc_auc_score(y_test, y_scores)

    # Plotting
    plt.figure(figsize=(4, 3))
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {auc_score:.2f})', color='darkorange')
    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve - {model_name}')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()