# Seed Classification using Random Forest

This project implements a **Random Forest classifier** to predict the class of wheat seeds based on their geometric and physical properties.  
The project demonstrates basic data preprocessing, exploratory visualization, model training, and evaluation.

---

## Objective

To classify seeds into one of three classes using measurable physical features such as area, perimeter, and kernel shape attributes.

---

## Dataset

- **File:** `seeds_dataset.csv`
- **Target Column:** `Class (1, 2, 3)`
- **Dropped Columns:**  
  - `Unnamed: 8`  
  - `Unnamed: 9`  

These columns contained no useful information and were removed during preprocessing.

---

## Features Used

- Area  
- Perimeter  
- Compactness  
- Kernel length  
- Kernel width  
- Asymmetry coefficient  
- Kernel groove length  

---

## Workflow

1. Load and inspect dataset structure
2. Remove unnecessary columns
3. Check feature cardinality
4. Perform basic exploratory visualization
5. Split data into training and testing sets
6. Train a Random Forest classifier
7. Evaluate model performance using accuracy

---

## Model Details

- **Algorithm:** Random Forest Classifier
- **Library:** Scikit-learn
- **Train/Test Split:** Default (random_state = 42)
- **Evaluation Metric:** Accuracy score

---

## Visualization

A bar chart is generated showing the **sum of seed area grouped by class**, providing a high-level view of class distribution in the dataset.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
