
vendors = [
    {"name": "RetroDecor Co.", "theme": "Retro", "rating": 9, "cost": 20000},
    {"name": "ModernEvents Ltd.", "theme": "Modern", "rating": 8, "cost": 18000},
    {"name": "BeachVibes Ltd.", "theme": "Beach", "rating": 7, "cost": 15000},
    {"name": "BirthdayBash Co.", "theme": "Birthday", "rating": 9, "cost": 10000},
    {"name": "WeddingPros", "theme": "Wedding", "rating": 10, "cost": 50000},
]

restaurants = [
    {"name": "RetroBites", "theme": "Retro", "rating": 9, "menu": ["Mini Burgers", "Neon Mocktails"], "avg_cost_per_guest": 400},
    {"name": "ModernEats", "theme": "Modern", "rating": 8, "menu": ["Sushi Platter", "Fusion Dessert"], "avg_cost_per_guest": 500},
    {"name": "BeachCafe", "theme": "Beach", "rating": 7, "menu": ["Tropical Juice", "Grilled Seafood"], "avg_cost_per_guest": 450},
    {"name": "BdayTreats", "theme": "Birthday", "rating": 9, "menu": ["Cupcakes", "Chocolate Fountain"], "avg_cost_per_guest": 300},
    {"name": "WeddingFeast", "theme": "Wedding", "rating": 10, "menu": ["Royal Thali", "Premium Drinks"], "avg_cost_per_guest": 800},
]

surprises = [
    {"theme": "Retro", "idea": "Classic vinyl record photobooth & neon lights"},
    {"theme": "Modern", "idea": "Laser light show & modern art gallery corner"},
    {"theme": "Beach", "idea": "Sand art station & live acoustic music"},
    {"theme": "Birthday", "idea": "Balloon wall & magician performance"},
    {"theme": "Wedding", "idea": "Live string quartet & flower shower surprise"},
]

def main():
    print("Welcome to the Event Management AI")

    # Gather event details
    theme = input("Enter your event theme (e.g. Retro, Modern, Beach): ")
    guest_count = int(input("How many guests? "))
    budget = float(input("What is your estimated budget? "))
    reason = input("What is the reason for the event (e.g. Birthday, Wedding)? ")

    print("\nYou entered:")
    print(f"Theme: {theme}")
    print(f"Guests: {guest_count}")
    print(f"Budget: ₹{budget}")
    print(f"Reason: {reason}")

    # Recommend vendors
    matching_vendors = [v for v in vendors if v["theme"].lower() == theme.lower()]
    if matching_vendors:
        print("\nHere are some vendors that fit your theme:")
        for v in matching_vendors:
            print(f"→ {v['name']} (Rating: {v['rating']}), Estimated cost: ₹{v['cost']}")
    else:
        print("\nHmm, couldn't find vendors for that exact theme. Here are some top-rated options:")
        for v in sorted(vendors, key=lambda x: x['rating'], reverse=True)[:3]:
            print(f"→ {v['name']} (Rating: {v['rating']}), Estimated cost: ₹{v['cost']}")

    # Recommend restaurants
    matching_restaurants = [r for r in restaurants if r["theme"].lower() == theme.lower()]
    if matching_restaurants:
        print("\nYou might like these restaurants for your theme:")
        for r in matching_restaurants:
            print(f"→ {r['name']} | Menu: {', '.join(r['menu'])} | Avg cost per guest: ₹{r['avg_cost_per_guest']} | Rating: {r['rating']}")
    else:
        print("\nNo themed restaurants found. Here are some favorites:")
        for r in sorted(restaurants, key=lambda x: x['rating'], reverse=True)[:2]:
            print(f"→ {r['name']} | Menu: {', '.join(r['menu'])} | Avg cost per guest: ₹{r['avg_cost_per_guest']} | Rating: {r['rating']}")

    # Surprise idea
    surprise = next((s['idea'] for s in surprises if s['theme'].lower() == theme.lower()), None)
    print(f"\n A surprise idea for your guests: {surprise if surprise else 'Maybe add a small welcome drink or fun photo booth?'}")

    # Estimate total food cost
    avg_cost = matching_restaurants[0]['avg_cost_per_guest'] if matching_restaurants else sorted(restaurants, key=lambda x: x['rating'], reverse=True)[0]['avg_cost_per_guest']
    total_food_cost = avg_cost * guest_count
    print(f"\nYour estimated food cost is about ₹{total_food_cost}")

    total_est_cost = total_food_cost + (matching_vendors[0]['cost'] if matching_vendors else 0)
    print(f"That brings the total estimate to ₹{total_est_cost}")

    # Check against the budget
    if total_est_cost <= budget:
        print(f"Looks good! You'd still have ₹{budget - total_est_cost} left in your budget. 🎉")
    else:
        print(f"It looks like you're over your budget by ₹{total_est_cost - budget}. Maybe look for more affordable vendors or restaurants?")

    # Prepare summary content
    summary = f"""
Event Summary
==========================
Theme: {theme}
Guests: {guest_count}
Budget: ₹{budget}
Reason: {reason}

Recommended Vendor:
{matching_vendors[0]['name']} (Cost: ₹{matching_vendors[0]['cost']}) if matching_vendors else "N/A"

Recommended Restaurant:
{matching_restaurants[0]['name']} (Avg per guest: ₹{avg_cost}) if matching_restaurants else "N/A"

Surprise Idea:
{surprise if surprise else "Welcome drink or photo booth"}

Total Estimated Cost: ₹{total_est_cost}
==========================
""".strip()

    # Save summary to file
    with open("event_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n Summary saved to event_summary.txt. You can open this file anytime!")

if __name__ == "__main__":
    main()
