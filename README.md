# **MediMatch: AI-Powered Alternative Medicine Finder**

MediMatch is a command-line tool designed to suggest alternative medicines for patients when a specific medicine is unavailable. Leveraging machine learning techniques like clustering and K-Nearest Neighbors (KNN), MediMatch provides effective recommendations tailored to patient needs.

## **Features**

- **Smart Clustering**: Groups medicines based on chemical composition, usage, and reviews
- **Alternative Finder**: Suggests similar medicines when a preferred one is not available
- **Review-Based Suggestions**: Considers excellent, average, and poor reviews to enhance recommendation quality
- **Extensible Dataset**: Easily add new data to expand the system's functionality

## **Technologies Used**

- **Programming Language**: Python
- **Libraries**:
  - Scikit-learn
  - Pandas
  - NumPy

## **Dataset Structure**

The dataset (`medicines.csv`) should have the following structure:

| Medicine Name | Main Element | Numeric Value | Uses | Side Effects | Image URL | Manufacturer | Excellent Review % | Average Review % | Poor Review % |
|--------------|--------------|---------------|------|--------------|-----------|--------------|-------------------|-----------------|---------------|
| Avastin 400mg Injection | Bevacizumab | 400mg | Cancer of colon and rectum... | Rectal bleeding, ... | https://onemg.gumlet.io/l_watermark_346,w... | Roche Products India Pvt Ltd | 22 | 56 | 22 |
| Augmentin 625 Duo Tablet | Amoxycillin | 500mg | Treatment of Bacterial... | Vomiting, Nausea,... | https://onemg.gumlet.io/l_watermark_346,w... | Glaxo SmithKline Pharmaceuticals | 47 | 35 | 18 |

## **Installation and Setup**

### Prerequisites
- Python (version 3.8 or later)
- Pip (Python package manager)

### Steps to Set Up

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Pranjal-88/MediMatch.git
   cd MediMatch
   ```

2. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Dataset**
   - Ensure your `medicines.csv` file is placed in the project root directory
   - Verify the CSV file follows the structure shown above

## **How to Run**

1. **Open the runner.py file**

2. **Modify the Query Medicine**
   - Locate the `query_medicine` variable in `runner.py`
   - Replace its value with the medicine name you want alternatives for
   ```python
   query_medicine = "Your Medicine Name Here"
   ```

3. **Run the Program**
   ```bash
   python runner.py
   ```

4. **View Results**
   - The program will display the closest alternative medicine on the terminal.


## **Example Usage**

```python
# In runner.py
query_medicine = "Zincold Tablet"

# Output will be shown like:
```
![image](https://github.com/user-attachments/assets/14e773a3-96f0-4048-9139-d075db3f2c13)

