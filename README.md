# 🧠 Mentor-Aspirant Recommendation System

This project is a simple recommendation system that matches **law entrance exam aspirants** with the most suitable **mentors** based on their preferences and profiles using **cosine similarity**.

---

## 🚀 Features

- Mock data generation for mentors and aspirants.
- One-hot encoding for categorical attributes (subjects, styles).
- Cosine similarity-based matching.
- Top N mentor recommendations for each aspirant.
- Console output for easy testing and verification.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn (for cosine similarity)

---

## 📊 How It Works

### 1. **Generate Mock Data**
- **Mentors:** Include fields like subject specializations, college, teaching style, experience, and success rate.
- **Aspirants:** Include fields like preferred subjects, target college, preparation level, and learning style.

### 2. **Feature Vectorization**
- Convert categorical fields (e.g., subject preferences, learning/teaching style) into binary vectors using **one-hot encoding**.
- Normalize numerical features (e.g., mentor ranks and success rates).
- Use placeholder values for aspirant fields where numeric data is not applicable.

### 3. **Similarity Calculation**
- Compute **cosine similarity** between aspirant feature vectors and mentor feature vectors.
- Higher similarity scores indicate better matches.

### 4. **Recommendation**
- Return the **top 3 mentors** for each aspirant based on similarity scores.
- Display the match percentage along with mentor details.

---

## 🧪 Sample Output

Aspirant A1:
Preferred Subjects: ['English', 'GK']
Target College: NLU Delhi
Preparation Level: Beginner
Learning Style: Interactive

Top 3 Recommended Mentors:

1. Mentor 2 (Match: 87.33%)
   College: NALSAR Hyderabad
   Specialization: English, GK, Legal Reasoning
   Teaching Style: Interactive

2. Mentor 5 (Match: 84.57%)
   College: NLSIU Bangalore
   Specialization: English, Constitutional Law, GK
   Teaching Style: Interactive

3. Mentor 8 (Match: 81.12%)
   College: WBNUJS Kolkata
   Specialization: GK, Current Affairs, English
   Teaching Style: Practice-oriented
