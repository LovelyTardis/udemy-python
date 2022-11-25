"""
    This day's project is a combination of csv DataSet reads with plots and Machine Learning.
    Given a csv file, it gets the "Survived" column and creates a prediction. Then it creates
    different plots for that prediction and tries to understand the logic of the csv data.
    Creates a plot_tree for every decision it made and what is predicted values for the survivor
    rate, in this case. It also shows a plot for how every feature impacts the final result,
    in this case the genre has a major impact and having parents or offspring has less impact.
"""
import pandas as pd
import matplotlib as plt
from matplotlib import figure, pyplot
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

df = pd.read_csv("DataSet_Titanic.csv")
X = df.drop("Survived", axis=1)
survived_real = df.Survived
tree_obj = tree.DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)


def main():
    """ Main function """
    print(X.head())
    print(survived_real.head())

    tree_obj.fit(X, survived_real)
    survived_predict = tree_obj.predict(X)
    print("Precision: ", accuracy_score(survived_predict, survived_real))

    matrix = confusion_matrix(survived_real, survived_predict)
    ConfusionMatrixDisplay(matrix)

    # IMPORTANT READ #
    # Execute one for a better plot display.
    # show_figure_1 and show_figure_2 can be called in the same execution.
    # show_figure_3 and show_figure_4 must be called one by execution.

    # show_figure_1(survived_predict)
    # show_figure_2(survived_predict)
    # show_figure_3()
    show_figure_4()


def show_figure_1(survived_predict):
    """ Shows the first figure, a confusion matrix
    :param survived_predict: a prediction of the tree
    """
    ConfusionMatrixDisplay.from_predictions(
        survived_real, survived_predict,
        cmap=plt.cm.Blues, values_format=".0f")


def show_figure_2(survived_predict):
    """ Shows the second figure, a confusion matrix
    :param survived_predict: a prediction of the tree
    """
    ConfusionMatrixDisplay.from_predictions(
        survived_real, survived_predict,
        cmap=plt.cm.Blues, values_format=".2f", normalize="true")


def show_figure_3():
    """ Shows the third figure, a decision tree. """
    figure.Figure(figsize=(10, 8))
    tree.plot_tree(tree_obj, filled=True, feature_names=X.columns)
    pyplot.show()


def show_figure_4():
    """ Shows a plot with the feature importances for every column in the csv file """
    importances = tree_obj.feature_importances_
    columns = X.columns

    sns.barplot(x=columns, y=importances)
    pyplot.title("Importance of every attribute")
    pyplot.show()


if __name__ == '__main__':
    main()
