# **MediMatch: AI-Powered Alternative Medicine Finder**

MediMatch is a command-line tool designed to suggest alternative medicines for patients when a specific medicine is unavailable. Leveraging machine learning techniques like clustering and K-Nearest Neighbors (KNN), MediMatch provides effective recommendations tailored to patient needs.

---

## **Features**

- **Smart Clustering**: Groups medicines based on chemical composition, category, and treatment type.  
- **Alternative Finder**: Suggests similar medicines when a preferred one is not available.  
- **Extensible Dataset**: Add new data easily to expand the system’s functionality.  

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

| Medicine Name | Category      | Chemical Composition | Treatment Type | Side Effects |  
|---------------|---------------|----------------------|----------------|--------------|  
| MedicineA     | Allergy       | CompoundX, CompoundY | Skin Allergy   | Drowsiness   |  
| MedicineB     | Pain Relief   | CompoundZ            | Headache       | Nausea       |  

Place this file in the `data/` folder before running the project.

---

## **Installation and Setup**

### Prerequisites
- Python (version 3.8 or later)  
- Pip (Python package manager)

### Steps to Set Up
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/MediMatch.git
   cd MediMatch
