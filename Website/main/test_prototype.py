import re
import pandas as pd
import numpy as np
import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
import random
from flask import Flask, jsonify, json
import datetime
import pytz
import dateutil.parser


restauraunt_profiles = pd.read_csv(
    '../derived_files/combined_restaurant_order_profile.csv')
id_df = pd.read_csv('../from_skip_files/All_Restaurants.csv')
print(id_df)

id_df['short_name'] = id_df['short_name'].str.lower()
restauraunt_profiles = restauraunt_profiles[restauraunt_profiles['short_name'].isin(
    id_df['short_name'])]


cuisine_map = {
    "Chicken": ["chicken"],
    "Fries": ["fries"],
    "Beef": ["beef"],
    "Pork": ["pork", "bacon", "pepperoni"],
    "Rice": ["rice"],
    "Lamb": ["lamb"],
    "Vegetarian": ["vegan", "vegetarian", "veggie", "beyond meat"],
    "Sandwiches & Subs": ["sandwich", "sub", "wrap", "blt"],
    "Desserts": ["blizzard", "ice cream", "frozen", "dessert", "chocolate", "drizzle", "desserts", "milkshake", "candy",
                 "candies", "sundae", "oreo", "skor", "brownie", "shake", "tiramisu", "timbits", "ben and jerry",
                 "cheesecake", "cookie"],
    "Canadian": ["canadian", "canadien", "alberta", "poutine"],
    "Fast Food": ["fast food", "combo", "meal"],
    "Burgers": ["burger", "patty", "mcdouble", "big mac", "quarter pounder"],
    "Seafood": ["fish", "seafood", "shrimp", "crab", "lobster", "prawn", "seaweed",
                "salmon", "tuna", "poke", "calamari", "squid", "fish and chips"],
    "Healthy": ["organic", "health", "protein", "salad", "fresh", "tofu",  "fruit", "water", "vegetable", "smoothie", "parfait"],
    "Pizza": ["pizza"],
    "Breakfast & Brunch": ["egg", "toast", "benedict", "breakfast", "brunch", "cereal", "pancake", "waffle", "hash brown"],
    "Coffee/Tea": ["coffee", " tea ", "americano", "cappuccino", "latte", "cafe", "chai", "london fog"],
    "Alcohol": ["beer", "wine", "liquor", "budweiser", "bud light", "spirits", "corona", "stella artois",
                "michelob ultra", "mike's hard", "labatt", "sauvignon", "smirnoff", "vodka", "whisky", "cognac",
                "white claw", "pinot noir"],
    "Noodles": ["noodle", "vermicelli"],
    "Pub Food": ["wing", "onion ring", "wedge", "mac & cheese", "mac and cheese", "gravy", "mashed potato", "breadsticks"],
    "Indian": ["indian", "naan", "nan", "samosa", "masala", "aloo", "paneer", "biryani", "tandoori", "roti", "tikka"],
    "Italian": ["italian", "pasta", "spaghetti", "penne", "fettuccini", "lasagna", "lasagne", "linguini", "ravioli", "tortellini", "meatball", "canoli"],
    "Bakery": ["danish", "cake", "bun", "donut", "muffin", "bagel", "doughnut", "pie", "scone", "rolls", "loaf"],
    "Barbecue": ["barbecue", "bbq", "grill", "buffalo"],
    "Chinese": ["chinese", "china", "hot pot", "wonton", "cantonese", "mein", "gyoza"],
    "Vietnamese": ["vietnamese", "pho", "viet", "bun cha", "ca kho to"],
    "Japanese": ["japanese", "japan", "ramen", "sashimi", "teriyaki", "katsu", "tempura", "edamame", "bento", "takoyaki"],
    "Tacos": ["taco"],
    "Sushi": ["sushi"],
    "Mediterranean": ["mediterranean", "pita", "damascus", "greek", "greece", "briam", "taramasalata", "opa"],
    "Hot Dogs & Sausages": ["hot dogs", "sausage", "weiner"],
    "Middle Eastern": ["middle eastern", "falafel", "hummus", "shawarma", "baklava", "donair", "tzatziki"],
    "Convenience": ["convenience", "pre-made", "grocery", "slurpee"],
    "Mexican": ["mexican", "chilaquiles", "burrito", "nacho", "quesadilla", "queso", "taquito", "salsa"],
    "Steakhouse": ["steakhouse", "steak"],
    "Halal": ["halal", "zabiha"],
    "Korean": ["korean", "kimchi", "bulgogi", "bibimbap", "tteokbokki", "jjambbong", "doenjang"],
    "Thai": ["thai", "tom yum goong", "green curry"],
    "Soup": ["soup"],
    "Gluten Free": ["gluten free", "no gluten"],
    "Popcorn": ["popcorn"],
    "Pet Food": ["pet", "dog", "cat"],
    "Bubble Tea": ["bubble tea", "boba", "milk tea", "taro milk"],
    "French": ["french", "francais", "crepe", "foie gras", "coq au vin", "cassoulet", "baguette", "croissant", "gougeres", "cajun & creole", "creole"],
    "African": ["african", "pap en vleis", "shisa nyama", "bunny chow", "koshari"],
    "Latin American": ["latin", "asado", "saltena", "feijoada", "empanada", "bandeja paisa",
                       "gallo pinto", "ropa vieja", "mangu", "encebollado", "pupusas", "pepian", "peruvian"],
    "Haute Cuisine": ["haute", "high class", "expensive", "champagne"],
    "Ethiopian": ["ethiopian", "tibs", "kitfo", "beyainatu", "fuul"],
    "Caribbean": ["caribbean", "jamaica", "barbados", "bahamas"],
    "Filipino": ["filipino", "adobo", "lechon", "sisig", "bulalo"],
    "Spanish": ["spanish", "paella valenciana", "patatas bravas", "gazpacho", "pimientos de padron", "jamon", "tapas", "churro"],
    "Butcher": ["raw", "butcher", "delicatessen"],
    "Kosher": ["kosher", 'kashrut', 'jewish'],
    "German": ["german", "schnitzel", "rouladen", "eintopf", "sauerbraten"]
}

ethnic_or_cultural_items = [
    "Convenience",
    "Indian",
    "Italian",
    "Chinese",
    "Vietnamese",
    "Japanese",
    "Mediterranean",
    "Middle Eastern",
    "Mexican",
    "Korean",
    "Thai",
    "French",
    "African",
    "Latin American",
    "Ethiopian",
    "Caribbean",
    "Filipino",
    "Spanish",
    "German",
]


def get_order_weight(order_date_str):
    order_date = dateutil.parser.parse(order_date_str)
    delta = datetime.datetime.now(pytz.utc) - order_date
    days_since_order = delta.days
    weight_0to3months = 1
    weight_3to6months = 0.7
    weight_6to12months = 0.3
    weight_12to24months = 0.2
    if days_since_order < 90:
        return weight_0to3months
    elif days_since_order < 180:
        slope = (weight_3to6months - weight_0to3months) / (180 - 90)
        return 1.0 + slope * (days_since_order - 90)
    elif days_since_order < 365:
        slope = (weight_6to12months - weight_3to6months) / (365 - 180)
        return 0.7 + slope * (days_since_order - 180)
    elif days_since_order < 730:
        slope = (weight_12to24months - weight_6to12months) / (730 - 365)
        return 0.3 + slope * (days_since_order - 365)
    else:
        return 0.1


def create_customer_profile(group):
    # data = [[group['items'], group['date']]]
    # my_df = pd.DataFrame(data, columns=['items', 'date'])
    my_df = pd.DataFrame(group, columns=['items', 'date'])
    my_df['items'] = my_df['items'].apply(lambda x: ', '.join(x))
    print(my_df)

    customer_profile = dict(zip(cuisine_map.keys(), [0] * 80))
    total_filtered = 0
    total_filtered = 0

    for index, row in my_df.iterrows():
        items = row['items'].split(", ")
        order_date = row['date']
        weight = get_order_weight(order_date)
        any_items_found = False
        for item in items:
            lower_item = item.lower()
            cuisine_identified_item = False
            for key in cuisine_map:
                for cuisine in cuisine_map[key]:
                    if cuisine in lower_item:
                        if key in ethnic_or_cultural_items:
                            cuisine_identified_item = True
                        customer_profile[key] += weight
                        total_filtered += weight
                        any_items_found = True
                        break

    map_total_filtered = 0
    for value in customer_profile.values():
        map_total_filtered += value
    if math.isclose(total_filtered, map_total_filtered, abs_tol=0.003) and total_filtered != 0:
        for key in customer_profile:
            customer_profile[key] = customer_profile[key]/total_filtered
        customer_profile['customer_id'] = "Dummy"

    # Create customer Profile dataframe
    customer_profile_df = pd.DataFrame(customer_profile, index=[0])

    customer_profile_df = customer_profile_df.reindex(
        columns=['customer_id'] + list(customer_profile_df.columns.drop('customer_id')))

    cols = customer_profile_df.columns.tolist()
    cols = cols[:-54] + sorted(cols[-54:])

    customer_profile_df = customer_profile_df.reindex(columns=cols)
    print("This is customer profile")
    print(customer_profile_df)

    return customer_profile_df


# Cosine Similarity Calculation
def cosine_similarity(customer_profile, restaurant_profile_list):
    cos_sims = []
    norm_a = np.linalg.norm(customer_profile)
    for vec in restaurant_profile_list:
        dot_product = np.dot(customer_profile, vec)
        norm_b = np.linalg.norm(vec)
        cos_sim = dot_product / (norm_a * norm_b)
        cos_sims.append(cos_sim)
    return np.array(cos_sims)


# Reccomendating filtering functions
def recommend_cosine_sim(customer_vector, restaurant_profiles, num_recommendations):
    # Calculate cosine similarity between customer and restaurants, and stores the indicies of the highest similarity
    # restaurants in variable value.
    customer_vector_temp = customer_vector.squeeze()
    customer_cuisines = customer_vector_temp.iloc[1:].to_numpy()
    customer_cuisines = customer_cuisines.reshape(1, -1)
    restaurant_cuisines = restaurant_profiles.iloc[:, 1:].to_numpy()
    similarity = cosine_similarity(customer_cuisines, restaurant_cuisines)
    value = np.argsort(similarity.flatten())[::-1]
    top_X_restaurants_id = []
    top_X_short_names = []
    ratings = []
    # Ensures unique restaurant names in recommendation
    for i in value:
        curr_name = restaurant_profiles.iloc[i]['short_name']
        rating_same_name = id_df[id_df['short_name'] == curr_name]
        max_rating_row = rating_same_name.loc[rating_same_name['restaurant_rating'].idxmax()]
        top_X_restaurants_id.append(max_rating_row['restaurant_id'])
        ratings.append(max_rating_row['restaurant_rating'])
        if len(top_X_restaurants_id) == num_recommendations:
            break
    top_X_restaurants = restaurant_profiles.iloc[value[:num_recommendations]]
    top_cos_scores = np.sort(similarity.flatten())[::-1][:num_recommendations]
    top_X_restaurants.insert(55, 'cosine similarity score', top_cos_scores)
    top_X_restaurants.insert(56, 'restaurant rating', ratings)
    top_X_restaurants.insert(1, 'restaurant_id', top_X_restaurants_id)
    return top_X_restaurants


def recommend_liked_cuisine_restaurants(customer_vector, restaurant_profiles, num_recommendations, num_replacements):
    customer_vector_id = customer_vector.iloc[0]
    customer_cuisines = customer_vector.iloc[-54:, 1:]
    customer_cuisines = customer_cuisines.squeeze()
    top = pd.to_numeric(customer_cuisines, errors='raise').nlargest(
        num_replacements)
    top = top[top > 0]
    total = top.sum()
    top_index = top.index[0]
    top_value = top.iloc[0]
    num_restaurants = []
    restaurants = []
    for index, value in top.iloc[0:].items():
        copy_customer_cuisines = customer_cuisines.copy()
        copy_customer_cuisines[top_index] = value
        copy_customer_cuisines[index] = top_value
        t_top5 = pd.to_numeric(copy_customer_cuisines,
                               errors='raise').nlargest(5)
        num_restaurants.append(round((value/total)*num_recommendations))
        customer_id_series = pd.Series({"customer_id": customer_vector_id})
        copy_customer_vector = pd.concat(
            [customer_id_series, copy_customer_cuisines])
        restaurants.append(recommend_cosine_sim(
            copy_customer_vector, restaurant_profiles, num_recommendations))
    print(num_restaurants)
    while (sum(num_restaurants) < num_recommendations):
        random_index = random.randint(0, len(num_restaurants) - 1)
        num_restaurants[random_index] += 1
    while (sum(num_restaurants) > num_recommendations):
        random_index = random.randint(0, len(num_restaurants) - 1)
        num_restaurants[random_index] -= 1
    final_restaurants = []
    avoid = []
    for i in range(0, len(num_restaurants)):
        final_restaurants.append(restaurants[i][~restaurants[i].isin(
            avoid)].dropna().sample(n=num_restaurants[i]))
        avoid.extend(final_restaurants[-1]['short_name'].to_list())
    final_df = pd.concat(final_restaurants, axis=0)
    return final_df


def update_3_top_cuisines(customer_vector, similarity_matrix):
    # Picks two highest customer cuisine preferences and swaps them with similar cuisines found
    # in a similarity matrix. E.g customer likes Chicken 0.25 and Rice 0.2, will swap them out so they
    # could become Fast Food and Lamb.
    customer_vector_id = customer_vector.iloc[0, 0]
    customer_cuisines = customer_vector.iloc[-54:, 1:]
    org_sum = str(customer_cuisines.sum())

    customer_cuisines_numeric = customer_cuisines.apply(
        pd.to_numeric, errors='raise')
    top3 = customer_cuisines_numeric.sum().nlargest(3)
    print("This is customer's top 3 cuisines")
    print(top3)

    do_not_repeat = top3.index.to_list()
    print(do_not_repeat)
    for cuisine in top3.index.to_list():
        similar_cuisines_dict = similarity_matrix[cuisine].to_dict()
        print(similar_cuisines_dict)
        old_cuisine = cuisine
        old_cuisine_preference = top3[old_cuisine]
        print(old_cuisine, old_cuisine_preference)
        similar_cuisine = ""
        while similar_cuisine == "" or similar_cuisine in do_not_repeat:
            similar_cuisine = random.choice(list(similar_cuisines_dict.keys()))
        similarity_of_new_cuisine = similar_cuisines_dict[similar_cuisine]
        print(similar_cuisine, similarity_of_new_cuisine)
        updated_old_cuisine_value = customer_cuisines[similar_cuisine]
        updated_similar_cuisine_value = old_cuisine_preference
        customer_cuisines[old_cuisine] = updated_old_cuisine_value
        customer_cuisines[similar_cuisine] = updated_similar_cuisine_value
    print("Sums", org_sum, " ", customer_cuisines.sum())

    customer_cuisines_numeric = customer_cuisines.apply(
        pd.to_numeric, errors='raise')
    top5 = customer_cuisines_numeric.sum().nlargest(5)

    print(top5)
    customer_id_series = pd.Series({"customer_id": customer_vector_id})

    print("This is updated customer Cuisine")
    customer_cuisines.insert(0, "customer_id", customer_vector_id)
    print(customer_cuisines)

    return customer_cuisines


def adjust_recommendations_using_rating(top_restaraunts, weight):
    if weight < 0 or weight > 1:
        return
    adjusted_scores = []
    for i in range(0, top_restaraunts.shape[0]):
        r_row = top_restaraunts.iloc[i]
        restaurant_rating = id_df[id_df['restaurant_id'] == r_row['restaurant_id']]['restaurant_rating']
        adjusted_scores.append(
            weight*restaurant_rating.iloc[0]/5+(1-weight) * r_row['cosine similarity score'])
    top_restaraunts.insert(56, 'adjusted score', adjusted_scores)
    new_top_restaraunts = top_restaraunts.sort_values(
        by='adjusted score', ascending=False)
    return new_top_restaraunts


def clean_similar_cuisine():
    rf = pd.read_csv("../derived_files/similarity_matrix.csv")
    similar_cuisines = {}
    similarity_upper_limit = 0.75
    for index, row in rf.iterrows():
        similarities = row.drop("Unnamed: 0")
        similarities = pd.to_numeric(similarities, errors='raise')
        filtered = similarities[similarities <= similarity_upper_limit]
        columns = filtered.nlargest(5)
        similar_cuisines[row.iloc[0]] = columns
    return similar_cuisines


def convert_to_json(customer_vector, restaurant_vector, adjusted_restaurant_vector):
    customer_id = customer_vector.iloc[0, 0]
    customer_cuisines = customer_vector.iloc[-54:, 1:]

    top5_customer = customer_vector.iloc[-54:, 1:].apply(
        lambda row: row.nlargest(5).index.tolist(), axis=1)
    print("reached just before json")

    json_data = {
        index: {
            "customer_id": customer_vector.loc[index, "customer_id"],
            "top_5": {
                column: customer_vector.loc[index, column] for column in sorted(values, key=lambda x: customer_vector.loc[index, x], reverse=True)[:5]
            }
        } for index, values in top5_customer.items()
    }

    print("This is customer top 5 cuisine")

    customer_json = json.dumps(json_data)

    # Top 5 cuisine for restaurant
    print("This is restaurant profile")
    print(restaurant_vector)
    no_scores = restaurant_vector.drop(
        columns=['adjusted score', "cosine similarity score"])
    top5 = no_scores.iloc[:, 2:-
                          2].apply(lambda row: row.nlargest(5).index.tolist(), axis=1)
    print(top5)

    print("This is restaurant rating")
    for index, values in top5.items():
        print(id_df.loc[index, "restaurant_rating"])

    json_data = {
        index: {
            "short_name": restaurant_vector.loc[index, "short_name"],
            "adjusted_score": restaurant_vector.loc[index, "adjusted score"],
            "cosine_similarity_score": restaurant_vector.loc[index, "cosine similarity score"],
            "restaurant_rating": float(id_df.loc[index, "restaurant_rating"]),
            "top_5": {
                column: restaurant_vector.loc[index, column] for column in values
            }
        } for index, values in top5.items()
    }
    print("Top 5 cuisines for each restaurant")
    restaurant_json = json.dumps(json_data)

    # Top 5 cuisine for varied restaurant

    no_scores_adj = adjusted_restaurant_vector.drop(
        columns=['adjusted score', "cosine similarity score"])
    top5 = no_scores_adj.iloc[:, 2:-
                              2].apply(lambda row: row.nlargest(5).index.tolist(), axis=1)
    json_data = {
        index: {
            "short_name": adjusted_restaurant_vector.loc[index, "short_name"],
            "adjusted_score": adjusted_restaurant_vector.loc[index, "adjusted score"],
            "cosine_similarity_score": adjusted_restaurant_vector.loc[index, "cosine similarity score"],
            "restaurant_rating": float(id_df.loc[index, "restaurant_rating"]),
            "top_5": {
                column: adjusted_restaurant_vector.loc[index, column] for column in values
            }
        } for index, values in top5.items()
    }
    print("Top 5 cuisines for each Varied restaurant")
    varied_restaurant_json = json.dumps(json_data)

    customer_dict = json.loads(customer_json)
    restaurant_dict = json.loads(restaurant_json)
    varied_restaurant_dict = json.loads(varied_restaurant_json)

    # Merge the two dictionaries
    merged_dict = {"Customers": customer_dict, "Restaurants": restaurant_dict,
                   "Varied_Restuarnts": varied_restaurant_dict}

    # Convert the merged dictionary to JSON
    merged_json = json.dumps(merged_dict)
    return merged_json


def recommend_pipeline(item_list):
    print(item_list)
    avoid_restaraunts = []
    similar_cuisines = clean_similar_cuisine()
    customer_profile = create_customer_profile(item_list)

    top_restaraunts = recommend_liked_cuisine_restaurants(
        customer_profile, restauraunt_profiles, 5, 5)

    new_customer_vector = update_3_top_cuisines(
        customer_profile, similar_cuisines)

    top_restaraunts_varied = recommend_liked_cuisine_restaurants(
        new_customer_vector, restauraunt_profiles, 5, 3)

    top_restaraunts_adjusted = adjust_recommendations_using_rating(
        top_restaraunts, 0.1)

    top_restaraunts_varied_adjusted = adjust_recommendations_using_rating(
        top_restaraunts_varied, 0.1)

    print(top_restaraunts_adjusted[[
          'cosine similarity score', 'adjusted score']])
    print(top_restaraunts_varied_adjusted[[
          'cosine similarity score', 'adjusted score']])

    # Extracting top 5 cuisines from customer_profile

    intermediate_top_5 = top_restaraunts_adjusted.head(5)
    intermediate_varied_top_5 = top_restaraunts_varied_adjusted.head(5)

    print("Reached just before convert to json")
    json_data = convert_to_json(
        customer_profile, intermediate_top_5, intermediate_varied_top_5)

    return json_data
