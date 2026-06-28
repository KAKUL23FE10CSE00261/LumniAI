"""
routine_generator.py
Generates personalised skincare routines & product lists
based on skin_type, concerns, and lifestyle data.
"""

ROUTINES = {
    "Oily": {
        "morning": (
            "Start with a gentle foaming cleanser to remove overnight sebum. "
            "Apply a niacinamide serum (10%) to regulate oil production and minimise pores. "
            "Finish with an oil-free, lightweight moisturiser and a broad-spectrum SPF 50 sunscreen."
        ),
        "night": (
            "Double-cleanse: micellar water first, then a salicylic acid cleanser (2%) to unclog pores. "
            "Use a retinol serum (0.025-0.05%) 3x per week to control sebum and refine texture. "
            "Seal with a water-gel or gel moisturiser—skip heavy creams."
        ),
    },
    "Dry": {
        "morning": (
            "Cleanse with a cream or oil-based cleanser that preserves the skin barrier. "
            "Layer a hydrating hyaluronic acid serum on damp skin to lock in moisture. "
            "Apply a rich ceramide moisturiser, then SPF 30+ sunscreen to protect."
        ),
        "night": (
            "Oil cleanse to dissolve impurities without stripping. "
            "Use a peptide or glycerin-rich serum to rebuild the moisture barrier overnight. "
            "Finish with a thick ceramide or shea butter night cream, and consider a sleeping mask 2x per week."
        ),
    },
    "Combination": {
        "morning": (
            "Use a balanced gel-cream cleanser on the whole face. "
            "Apply a lightweight niacinamide serum to the T-zone; apply a hydrating serum on dry zones. "
            "Use a light moisturiser with SPF 30+ across the entire face."
        ),
        "night": (
            "Cleanse thoroughly to remove makeup and pollution. "
            "Spot-treat the T-zone with a BHA (salicylic acid) toner pad; "
            "apply a gentle hydrating serum to cheeks and dry patches. "
            "Use a medium-weight moisturiser—avoid heavy occlusive creams on oily areas."
        ),
    },
    "Sensitive": {
        "morning": (
            "Use a fragrance-free, sulphate-free cream cleanser to avoid triggering reactions. "
            "Apply centella asiatica or aloe vera serum to soothe and strengthen the barrier. "
            "Use a mineral (zinc oxide / titanium dioxide) SPF 30+ sunscreen to minimise irritation."
        ),
        "night": (
            "Rinse only with lukewarm water in the evening, or use a micellar water on cotton. "
            "Apply a barrier-repair serum with ceramides and panthenol. "
            "Finish with a gentle, fragrance-free night cream—patch-test any new actives before use."
        ),
    },
    "Normal": {
        "morning": (
            "Use a mild gel or foam cleanser. "
            "Apply a vitamin C serum (10-15%) to brighten and protect against oxidative stress. "
            "Moisturise with a medium-weight lotion and SPF 30+ to maintain your healthy baseline."
        ),
        "night": (
            "Cleanse to remove the day's impurities. "
            "Use a retinol or peptide serum 3-4 nights a week to maintain skin quality. "
            "Apply a lightweight overnight moisturiser—your skin is balanced, so keep it simple."
        ),
    },
}

PRODUCTS = {
    "Oily":       ["Foaming Salicylic Acid Cleanser", "Niacinamide 10% Serum",
                   "Oil-Free Lightweight Moisturiser", "SPF 50 Sunscreen (matte finish)",
                   "Retinol 0.05% Night Serum", "BHA Toner Pads"],
    "Dry":        ["Cream / Oil Cleanser", "Hyaluronic Acid Serum",
                   "Ceramide Moisturiser", "SPF 30 Mineral Sunscreen",
                   "Glycerin Night Serum", "Sleeping Mask"],
    "Combination":["Balanced Gel-Cream Cleanser", "Niacinamide Serum (T-zone)",
                   "Hydrating Serum (cheeks)", "Light Moisturiser SPF 30",
                   "BHA Toner (T-zone only)", "Medium-Weight Night Cream"],
    "Sensitive":  ["Fragrance-Free Cream Cleanser", "Centella Asiatica Serum",
                   "Aloe Vera Gel", "Mineral SPF 30 Sunscreen",
                   "Ceramide + Panthenol Barrier Serum", "Gentle Night Cream"],
    "Normal":     ["Mild Gel Cleanser", "Vitamin C 15% Serum",
                   "Lightweight Lotion Moisturiser", "SPF 30 Sunscreen",
                   "Retinol 0.025% Serum (3x/week)", "Peptide Night Cream"],
}

CONCERN_EXTRAS = {
    "Dark Spots":            ["Alpha Arbutin 2% Serum", "Azelaic Acid 10% Cream"],
    "Redness / Irritation":  ["Centella Asiatica Extract", "Azulene Calming Toner"],
    "Uneven Texture":        ["AHA (Glycolic Acid 5%) Toner", "Enzyme Exfoliant Mask"],
    "Excess Oil / Shine":    ["Pore-Minimising Primer", "Oil-Blotting Papers"],
    "Dryness / Flakiness":   ["Urea 5% Cream", "Overnight Hydrating Mask"],
}

DIETS = {
    "Oily":       ["Green leafy vegetables", "Pumpkin seeds (zinc)", "Berries",
                   "Cucumber", "Whole grains", "Green tea"],
    "Dry":        ["Avocado (healthy fats)", "Fatty fish (omega-3)", "Walnuts",
                   "Sweet potato", "Olive oil", "Coconut water"],
    "Combination":["Blueberries", "Tomatoes", "Eggs",
                   "Lentils", "Banana", "Walnuts"],
    "Sensitive":  ["Oatmeal", "Chamomile tea", "Turmeric",
                   "Ginger", "Leafy greens", "Probiotic yogurt"],
    "Normal":     ["Colourful vegetables", "Berries", "Nuts & seeds",
                   "Lean protein", "Green tea", "Whole grains"],
}


def generate_routine(skin_type: str, concerns: list, lifestyle: dict) -> dict:
    r = ROUTINES.get(skin_type, ROUTINES["Normal"])
    p = list(PRODUCTS.get(skin_type, PRODUCTS["Normal"]))

    for concern in concerns:
        extras = CONCERN_EXTRAS.get(concern, [])
        for e in extras:
            if e not in p:
                p.append(e)

    d = DIETS.get(skin_type, DIETS["Normal"])

    # Lifestyle impact messages
    lifestyle_msgs = []
    sleep = lifestyle.get("sleep_hours", 7)
    water = lifestyle.get("water_intake", 6)
    if isinstance(sleep, (int, float)):
        if sleep < 6:
            lifestyle_msgs.append({
                "text": "You are sleeping less than recommended hours. "
                        "This negatively affects skin repair and glow.",
                "type": "warning"
            })
        else:
            lifestyle_msgs.append({
                "text": "Good sleep hours are supporting overnight skin regeneration.",
                "type": "success"
            })
    if isinstance(water, (int, float)):
        if water >= 8:
            lifestyle_msgs.append({
                "text": "Your water intake is supporting healthy skin hydration.",
                "type": "success"
            })
        elif water < 5:
            lifestyle_msgs.append({
                "text": "Low water intake can cause dryness and dull complexion. "
                        "Aim for 8 glasses/day.",
                "type": "warning"
            })

    return {
        "morning":        r["morning"],
        "night":          r["night"],
        "products":       p,
        "diet":           d,
        "lifestyle_msgs": lifestyle_msgs,
    }


def compute_skin_score(profile: dict, cv_scores: dict | None = None) -> dict:
    """Compute numeric skin scores from profile + optional CV data."""
    base = 70.0
    issues = profile.get("skin_issues", [])
    base -= len(issues) * 8

    water = profile.get("lifestyle", {}).get("water_intake", 6) or 6
    sleep = profile.get("lifestyle", {}).get("sleep_hours", 7) or 7
    base += min(water - 6, 4) * 2
    base += min(sleep - 6, 3) * 2
    skin_score = max(20.0, min(base, 95.0))

    product_score = max(10.0, 100.0 - len(issues) * 12 - (8 - water) * 3)
    routine_eff   = max(10.0, skin_score * 0.85)
    env_sens      = 20.0 + (len(issues) * 5)

    if cv_scores:
        skin_score   = skin_score * 0.5 + cv_scores.get("oiliness", 0) * -0.1 \
                       + cv_scores.get("dark_spots", 0) * -0.1 + 10
        skin_score   = max(20.0, min(skin_score, 95.0))

    return {
        "skin_score":    round(skin_score, 2),
        "product_score": round(product_score, 2),
        "routine_eff":   round(routine_eff, 2),
        "env_sens":      round(env_sens, 2),
    }
