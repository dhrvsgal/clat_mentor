import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import random


def generate_mentor_data(n_mentors=10):
    subjects = ['Constitutional Law', 'Legal Reasoning', 'Current Affairs', 'English', 'GK']
    teaching_styles = ['Interactive', 'Structured', 'Practice-oriented', 'Theory-focused']
    colleges = ['NLSIU Bangalore', 'NALSAR Hyderabad', 'NLU Delhi', 'WBNUJS Kolkata', 'NLIU Bhopal']
    
    mentors = []
    for i in range(n_mentors):
        mentor = {
            'mentor_id': f'M{i+1}',
            'name': f'Mentor {i+1}',
            'rank': random.randint(1, 100),
            'college': random.choice(colleges),
            'specialization': random.sample(subjects, k=random.randint(2, 4)),
            'teaching_style': random.choice(teaching_styles),
            'years_experience': random.randint(1, 5),
            'success_rate': round(random.uniform(0.7, 0.95), 2)
        }
        mentors.append(mentor)
    return pd.DataFrame(mentors)

# Generate mock data for aspirants
def generate_aspirant_data(n_aspirants=5):
    subjects = ['Constitutional Law', 'Legal Reasoning', 'Current Affairs', 'English', 'GK']
    learning_styles = ['Interactive', 'Structured', 'Practice-oriented', 'Theory-focused']
    target_colleges = ['NLSIU Bangalore', 'NALSAR Hyderabad', 'NLU Delhi', 'WBNUJS Kolkata', 'NLIU Bhopal']
    
    aspirants = []
    for i in range(n_aspirants):
        aspirant = {
            'aspirant_id': f'A{i+1}',
            'preferred_subjects': random.sample(subjects, k=random.randint(2, 4)),
            'target_college': random.choice(target_colleges),
            'preparation_level': random.choice(['Beginner', 'Intermediate', 'Advanced']),
            'learning_style': random.choice(learning_styles)
        }
        aspirants.append(aspirant)
    return pd.DataFrame(aspirants)

# Process features and create feature vectors
def process_features(mentors_df, aspirants_df):
    # Process mentor features
    mentor_features = []
    for _, mentor in mentors_df.iterrows():
        
        subjects = ['Constitutional Law', 'Legal Reasoning', 'Current Affairs', 'English', 'GK']
        subject_features = [1 if subject in mentor['specialization'] else 0 for subject in subjects]
        
        
        teaching_styles = ['Interactive', 'Structured', 'Practice-oriented', 'Theory-focused']
        style_features = [1 if style == mentor['teaching_style'] else 0 for style in teaching_styles]
        
        
        rank_normalized = 1 - (mentor['rank'] / 100)  # Higher rank (lower number) = higher value
        success_rate = mentor['success_rate']
        
       
        mentor_features.append(subject_features + style_features + [rank_normalized, success_rate])
    
    # Process aspirant features
    aspirant_features = []
    for _, aspirant in aspirants_df.iterrows():
      
        subjects = ['Constitutional Law', 'Legal Reasoning', 'Current Affairs', 'English', 'GK']
        subject_features = [1 if subject in aspirant['preferred_subjects'] else 0 for subject in subjects]
        
       
        learning_styles = ['Interactive', 'Structured', 'Practice-oriented', 'Theory-focused']
        style_features = [1 if style == aspirant['learning_style'] else 0 for style in learning_styles]
        
        
        aspirant_features.append(subject_features + style_features + [0.5, 0.5])
    
    return np.array(mentor_features), np.array(aspirant_features)

# Get recommendations for an aspirant
def get_recommendations(mentors_df, aspirant_features, mentor_features, aspirant_idx, top_n=3):
    # Calculate cosine similarity between the aspirant and all mentors
    similarities = cosine_similarity([aspirant_features[aspirant_idx]], mentor_features)[0]
    
    
    top_mentor_indices = similarities.argsort()[-top_n:][::-1]
    
   
    recommendations = []
    for idx in top_mentor_indices:
        mentor = mentors_df.iloc[idx]
        similarity_score = similarities[idx]
        recommendations.append({
            'mentor_id': mentor['mentor_id'],
            'name': mentor['name'],
            'college': mentor['college'],
            'specialization': mentor['specialization'],
            'teaching_style': mentor['teaching_style'],
            'similarity_score': round(similarity_score * 100, 2)
        })
    
    return recommendations

def main():
    # Generate mock data
    mentors_df = generate_mentor_data(10)
    aspirants_df = generate_aspirant_data(5)
    
    # Process features
    mentor_features, aspirant_features = process_features(mentors_df, aspirants_df)
    
    # Print sample recommendations for each aspirant
    print("\nMentor Recommendations:")
    print("-" * 80)
    
    for idx, aspirant in aspirants_df.iterrows():
        print(f"\nAspirant {aspirant['aspirant_id']}:")
        print(f"Preferred Subjects: {aspirant['preferred_subjects']}")
        print(f"Target College: {aspirant['target_college']}")
        print(f"Preparation Level: {aspirant['preparation_level']}")
        print(f"Learning Style: {aspirant['learning_style']}")
        print("\nTop 3 Recommended Mentors:")
        
        recommendations = get_recommendations(mentors_df, aspirant_features, mentor_features, idx)
        
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['name']} (Match: {rec['similarity_score']}%)")
            print(f"   College: {rec['college']}")
            print(f"   Specialization: {', '.join(rec['specialization'])}")
            print(f"   Teaching Style: {rec['teaching_style']}")

if __name__ == "__main__":
    main() 