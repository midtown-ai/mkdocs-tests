import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=5, n_classes=4, n_informative=3, random_state=42)

# Encode labels (XGBoost requires labels to be in range 0 to num_classes-1)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define XGBoost model
xgb_model = xgb.XGBClassifier(objective="multi:softmax", num_class=4, n_estimators=10, max_depth=3, eval_metric="mlogloss", use_label_encoder=False)

# Train the model
xgb_model.fit(X_train, y_train)

# Extract one of the trees (from the first boosting round, class 0)
xgb.plot_tree(xgb_model, num_trees=0)  # Tree for class 0 in first boosting round

# Show the tree plot
plt.show()

