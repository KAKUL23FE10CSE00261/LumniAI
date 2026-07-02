def get_recommendation(skin_issue, skin_type):

    recommendations = {

        ("inflammatory acne", "oily"): {
            "cleanser": "2% Salicylic Acid Face Wash",
            "serum": "10% Niacinamide Serum",
            "moisturizer": "Oil-Free Gel Moisturizer",
            "sunscreen": "SPF 50 Oil-Free Sunscreen",
            "ingredients_to_avoid": [
                "Coconut Oil",
                "Heavy Creams",
                "Alcohol-based Products"
            ],
            "foods": [
                "Fresh Fruits",
                "Vegetables",
                "Green Tea",
                "Drink 2-3L Water"
            ]
        },

        ("inflammatory acne", "dry"): {
            "cleanser": "Gentle Hydrating Cleanser",
            "serum": "5% Niacinamide Serum",
            "moisturizer": "Ceramide Moisturizer",
            "sunscreen": "Hydrating SPF 50 Sunscreen",
            "ingredients_to_avoid": [
                "Harsh Scrubs",
                "Strong Alcohol"
            ],
            "foods": [
                "Nuts",
                "Seeds",
                "Milk",
                "Fresh Fruits"
            ]
        },

        ("pigmentation", "dry"): {
            "cleanser": "Hydrating Cleanser",
            "serum": "Vitamin C Serum",
            "moisturizer": "Ceramide Moisturizer",
            "sunscreen": "SPF 50 PA++++",
            "ingredients_to_avoid": [
                "Lemon on Face",
                "Harsh Exfoliation"
            ],
            "foods": [
                "Vitamin C Fruits",
                "Tomatoes",
                "Leafy Greens"
            ]
        },

        ("pigmentation", "oily"): {
            "cleanser": "Foaming Cleanser",
            "serum": "Vitamin C + Niacinamide",
            "moisturizer": "Oil-Free Moisturizer",
            "sunscreen": "Gel SPF 50",
            "ingredients_to_avoid": [
                "Heavy Oils"
            ],
            "foods": [
                "Orange",
                "Kiwi",
                "Watermelon"
            ]
        },

        ("wrinkles", "dry"): {
            "cleanser": "Cream Cleanser",
            "serum": "Retinol Serum",
            "moisturizer": "Peptide Moisturizer",
            "sunscreen": "SPF 50",
            "ingredients_to_avoid": [
                "Over-exfoliation"
            ],
            "foods": [
                "Avocado",
                "Walnuts",
                "Fish"
            ]
        }

    }

    default = {

        "cleanser": "Gentle Face Wash",

        "serum": "Niacinamide Serum",

        "moisturizer": "Lightweight Moisturizer",

        "sunscreen": "SPF 50 Sunscreen",

        "ingredients_to_avoid": [
            "Excess Sugar",
            "Harsh Chemicals"
        ],

        "foods": [
            "Fresh Fruits",
            "Vegetables",
            "Drink Plenty of Water"
        ]

    }

    return recommendations.get((skin_issue.lower(), skin_type.lower()), default)