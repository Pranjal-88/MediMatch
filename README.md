# **MediMatch: AI-Powered Alternative Medicine Finder**

MediMatch is a command-line tool designed to suggest alternative medicines for patients when a specific medicine is unavailable. Leveraging machine learning techniques like clustering and K-Nearest Neighbors (KNN), MediMatch provides effective recommendations tailored to patient needs.

---

## **Features**

- **Smart Clustering**: Groups medicines based on chemical composition, usage, and reviews.  
- **Alternative Finder**: Suggests similar medicines when a preferred one is not available.  
- **Review-Based Suggestions**: Considers excellent, average, and poor reviews to enhance recommendation quality.  
- **Extensible Dataset**: Easily add new data to expand the system’s functionality.  

---

## **Technologies Used**

- **Programming Language**: Python  
- **Libraries**:  
  - Scikit-learn  
  - Pandas  
  - NumPy  

---

## **Dataset Structure**

The dataset (`medicines.csv`) should have the following structure:

| Medicine Name            | Main Element  | Numeric Value | Uses                          | Side Effects          | Image URL                                     | Manufacturer                      | Excellent Review % | Average Review % | Poor Review % |  
|---------------------------|---------------|---------------|-------------------------------|-----------------------|-----------------------------------------------|-----------------------------------|---------------------|-------------------|---------------|  
| Avastin 400mg Injection   | Bevacizumab   | 400mg         | Cancer of colon and rectum...| Rectal bleeding, ...  | https://onemg.gumlet.io/l_watermark_346,w... | Roche Products India Pvt Ltd      | 22                  | 56                | 22            |  
| Augmentin 625 Duo Tablet  | Amoxycillin   | 500mg         | Treatment of Bacterial...    | Vomiting, Nausea,...  | https://onemg.gumlet.io/l_watermark_346,w... | Glaxo SmithKline Pharmaceuticals  | 47                  | 35                | 18            |  


---

## **Installation and Setup**

### Prerequisites
- Python (version 3.8 or later)  
- Pip (Python package manager)

### Steps to Set Up
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Pranjal-88/MediMatch.git
   cd MediMatch
