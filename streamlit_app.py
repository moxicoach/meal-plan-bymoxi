import streamlit as st

# Meal Plan Algorithm Functions
def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    activity_factors = {
        "sedentary": 1.2,
        "lightly_active": 1.375,
        "moderately_active": 1.55,
        "very_active": 1.725
    }
    return bmr * activity_factors.get(activity_level, 1.2)

def adjust_for_goal(tdee, goal):
    if goal == "weight_loss":
        return tdee - 500
    elif goal == "muscle_gain":
        return tdee + 500
    else:
        return tdee

def calculate_macronutrients(calories, protein_ratio, carb_ratio, fat_ratio):
    protein_cals = calories * protein_ratio
    carb_cals = calories * carb_ratio
    fat_cals = calories * fat_ratio
    protein_grams = protein_cals / 4
    carb_grams = carb_cals / 4
    fat_grams = fat_cals / 9
    return protein_grams, carb_grams, fat_grams

def generate_meal_plan(protein_grams, carb_grams, fat_grams):
    food_db = {
        "chicken_breast": {"protein": 31, "carbs": 0, "fats": 3.6},
        "brown_rice": {"protein": 2.6, "carbs": 23, "fats": 0.9},
        "broccoli": {"protein": 2.8, "carbs": 6, "fats": 0.4},
        "almonds": {"protein": 21, "carbs": 22, "fats": 50},
        "eggs": {"protein": 13, "carbs": 1.1, "fats": 11},
        "oatmeal": {"protein": 2.4, "carbs": 12, "fats": 1.6},
    }
    meal_plan = {
        "breakfast": {
            "foods": ["oatmeal", "eggs"],
            "protein": 20,
            "carbs": 30,
            "fats": 10
        },
        "lunch": {
            "foods": ["chicken_breast", "brown_rice", "broccoli"],
            "protein": 40,
            "carbs": 50,
            "fats": 10
        },
        "dinner": {
            "foods": ["chicken_breast", "broccoli"],
            "protein": 30,
            "carbs": 20,
            "fats": 10
        },
        "snacks": {
            "foods": ["almonds"],
            "protein": 10,
            "carbs": 10,
            "fats": 20
        }
    }
    return meal_plan

# Streamlit App
st.title("Personalized Meal Plan Generator")
st.write("Enter your details to generate a personalized meal plan.")

# Input fields
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=175.0)
age = st.number_input("Age", min_value=10, max_value=100, value=30)
gender = st.radio("Gender", ["male", "female"])
activity_level = st.selectbox("Activity Level", ["sedentary", "lightly_active", "moderately_active", "very_active"])
goal = st.selectbox("Fitness Goal", ["weight_loss", "muscle_gain", "maintenance"])

# Calculate and display results
if st.button("Generate Meal Plan"):
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    calories = adjust_for_goal(tdee, goal)
    protein_ratio = 0.3
    carb_ratio = 0.4
    fat_ratio = 0.3
    protein_grams, carb_grams, fat_grams = calculate_macronutrients(calories, protein_ratio, carb_ratio, fat_ratio)
    meal_plan = generate_meal_plan(protein_grams, carb_grams, fat_grams)

    # Display results
    st.subheader("Your Personalized Meal Plan")
    st.write(f"Daily Caloric Target: {calories:.2f} kcal")
    st.write(f"Macronutrient Targets: Protein = {protein_grams:.2f}g, Carbs = {carb_grams:.2f}g, Fats = {fat_grams:.2f}g")
    st.write("\n**Sample Meal Plan:**")
    for meal, details in meal_plan.items():
        st.write(f"{meal.capitalize()}: {', '.join(details['foods'])}")
        st.write(f"  Protein: {details['protein']}g, Carbs: {details['carbs']}g, Fats: {details['fats']}g")
