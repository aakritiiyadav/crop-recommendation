# Detailed crop library containing information on seasonal growth, NPK requirements,
# and actionable agricultural advisory rules for the 22 supported crops.

CROP_DETAILS = {
    "rice": {
        "name": "Rice",
        "description": "A staple food crop grown in flooded fields (paddies). It requires abundant water, high humidity, and warm weather.",
        "season": "Kharif (Monsoon - June to November)",
        "duration": "3 to 6 months",
        "water_requirement": "Very High (Requires standing water or 100-200 cm rainfall)",
        "optimal_npk": {"N": 80, "P": 40, "K": 40},
        "optimal_ph": "6.0 to 7.0",
        "market_value": "High",
    },
    "maize": {
        "name": "Maize (Corn)",
        "description": "A versatile cereal grain grown widely. It prefers well-drained loamy soils and warm, sunny climates.",
        "season": "Kharif & Rabi (Round the year in some parts)",
        "duration": "3 to 4 months",
        "water_requirement": "Moderate (50-80 cm rainfall)",
        "optimal_npk": {"N": 80, "P": 45, "K": 20},
        "optimal_ph": "5.5 to 7.0",
        "market_value": "Medium to High",
    },
    "chickpea": {
        "name": "Chickpea (Garbanzo Bean)",
        "description": "A pulse crop that thrives in cool climates and clayey soils. It fixes nitrogen in the soil naturally.",
        "season": "Rabi (Winter - October to April)",
        "duration": "3 to 4 months",
        "water_requirement": "Low (Requires minimal watering or 60-90 cm rainfall)",
        "optimal_npk": {"N": 40, "P": 67, "K": 80},
        "optimal_ph": "6.0 to 8.0",
        "market_value": "High",
    },
    "kidneybeans": {
        "name": "Kidney Beans (Rajma)",
        "description": "A popular legume requiring mild climates and moderate rainfall. It is sensitive to waterlogging.",
        "season": "Rabi / Kharif (depending on region)",
        "duration": "3 to 4 months",
        "water_requirement": "Moderate (60-100 cm rainfall)",
        "optimal_npk": {"N": 20, "P": 60, "K": 20},
        "optimal_ph": "6.0 to 6.5",
        "market_value": "High",
    },
    "pigeonpeas": {
        "name": "Pigeon Peas (Arhar/Tur)",
        "description": "A drought-tolerant legume widely grown in semi-arid regions. Ideal for intercropping.",
        "season": "Kharif (June to December)",
        "duration": "6 to 8 months",
        "water_requirement": "Low to Moderate (60-80 cm rainfall)",
        "optimal_npk": {"N": 20, "P": 67, "K": 20},
        "optimal_ph": "6.5 to 7.5",
        "market_value": "High",
    },
    "mothbeans": {
        "name": "Moth Beans",
        "description": "An exceptionally drought-resistant legume grown in arid zones. Prevents soil erosion.",
        "season": "Kharif (June to October)",
        "duration": "3 months",
        "water_requirement": "Very Low (30-50 cm rainfall)",
        "optimal_npk": {"N": 20, "P": 50, "K": 20},
        "optimal_ph": "6.5 to 8.0",
        "market_value": "Medium",
    },
    "mungbean": {
        "name": "Mung Bean (Green Gram)",
        "description": "A short-duration warm-season legume. Rich source of protein and excellent soil nutrient replenisher.",
        "season": "Summer / Kharif (March to June or June to October)",
        "duration": "2 to 3 months",
        "water_requirement": "Low (40-60 cm rainfall)",
        "optimal_npk": {"N": 20, "P": 48, "K": 20},
        "optimal_ph": "6.0 to 7.0",
        "market_value": "High",
    },
    "blackgram": {
        "name": "Black Gram (Urad Dal)",
        "description": "A nutrient-rich legume grown in hot climates. Prefers loamy or clayey soils.",
        "season": "Kharif & Rabi (June to October or November to April)",
        "duration": "3 months",
        "water_requirement": "Moderate (60-75 cm rainfall)",
        "optimal_npk": {"N": 40, "P": 47, "K": 20},
        "optimal_ph": "6.0 to 7.5",
        "market_value": "High",
    },
    "lentil": {
        "name": "Lentil (Masoor)",
        "description": "A cool-season legume grown in well-drained soils. Excellent for rotation and dryland farming.",
        "season": "Rabi (Winter - October to April)",
        "duration": "3 to 4 months",
        "water_requirement": "Low (35-50 cm rainfall)",
        "optimal_npk": {"N": 20, "P": 68, "K": 20},
        "optimal_ph": "6.0 to 7.0",
        "market_value": "High",
    },
    "pomegranate": {
        "name": "Pomegranate",
        "description": "A high-value fruit crop suitable for semi-arid and arid regions. Prefers sandy loam soils.",
        "season": "Perennial (Flowers 2-3 times/year)",
        "duration": "2 to 3 years to first fruit; lives up to 30 years",
        "water_requirement": "Low to Moderate (Drought tolerant once established)",
        "optimal_npk": {"N": 20, "P": 20, "K": 40},
        "optimal_ph": "5.5 to 7.0",
        "market_value": "Very High",
    },
    "banana": {
        "name": "Banana",
        "description": "A tropical fruit crop that requires warm temperatures, rich clay-loam soil, and constant moisture.",
        "season": "Perennial (Planted round the year)",
        "duration": "10 to 12 months for first harvest",
        "water_requirement": "Very High (Needs frequent irrigation or 150-220 cm rainfall)",
        "optimal_npk": {"N": 100, "P": 80, "K": 50},
        "optimal_ph": "6.0 to 7.5",
        "market_value": "High",
    },
    "mango": {
        "name": "Mango",
        "description": "The king of fruits. Requires deep, well-drained loamy soils and a clear dry season for flowering.",
        "season": "Summer (Flowers in winter, fruits in summer)",
        "duration": "4 to 5 years to bear fruit; long perennial",
        "water_requirement": "Moderate (Needs dry spell before flowering, then regular watering)",
        "optimal_npk": {"N": 20, "P": 25, "K": 30},
        "optimal_ph": "5.5 to 7.5",
        "market_value": "Very High",
    },
    "grapes": {
        "name": "Grapes",
        "description": "Grown on vines. Requires dry, warm summers and cool winters with well-drained sandy loam soil.",
        "season": "Perennial (Harvested in Spring/Summer)",
        "duration": "3 years to commercial yield",
        "water_requirement": "Moderate (Prefers drip irrigation)",
        "optimal_npk": {"N": 25, "P": 130, "K": 200},
        "optimal_ph": "5.5 to 6.5",
        "market_value": "Very High",
    },
    "watermelon": {
        "name": "Watermelon",
        "description": "A warm-season crop that thrives in sandy soils and hot, dry conditions with ample sunshine.",
        "season": "Summer (Zaid - January to May)",
        "duration": "3 to 4 months",
        "water_requirement": "Moderate (Needs consistent moisture until fruiting)",
        "optimal_npk": {"N": 100, "P": 15, "K": 50},
        "optimal_ph": "6.0 to 7.0",
        "market_value": "Medium",
    },
    "muskmelon": {
        "name": "Muskmelon (Cantaloupe)",
        "description": "Thrives in warm, dry weather and sandy loam soils. Sweetness depends heavily on sun and optimal watering.",
        "season": "Summer (Zaid - January to May)",
        "duration": "3 months",
        "water_requirement": "Low to Moderate (Well-drained soil prevents root rot)",
        "optimal_npk": {"N": 100, "P": 15, "K": 50},
        "optimal_ph": "6.0 to 7.0",
        "market_value": "Medium to High",
    },
    "apple": {
        "name": "Apple",
        "description": "A temperate fruit crop requiring chilly winters and cool summers. Grown in hilly regions.",
        "season": "Perennial (Harvested in Autumn)",
        "duration": "3 to 5 years for dwarf varieties; long perennial",
        "water_requirement": "Moderate (100-125 cm rainfall/irrigation)",
        "optimal_npk": {"N": 20, "P": 135, "K": 200},
        "optimal_ph": "6.0 to 6.5",
        "market_value": "Very High",
    },
    "orange": {
        "name": "Orange / Citrus",
        "description": "Requires subtropical climate with dry winters and humid summers. Grown in slightly acidic sandy loams.",
        "season": "Perennial (Harvested in Winter/Spring)",
        "duration": "3 to 4 years to bear fruit",
        "water_requirement": "Moderate to High (Needs systematic irrigation)",
        "optimal_npk": {"N": 20, "P": 15, "K": 10},
        "optimal_ph": "5.5 to 6.5",
        "market_value": "High",
    },
    "papaya": {
        "name": "Papaya",
        "description": "A fast-growing tropical fruit. Extremely sensitive to frost and waterlogging; requires rich loam soils.",
        "season": "Perennial (Planted in spring/monsoon)",
        "duration": "9 to 10 months to first harvest",
        "water_requirement": "Moderate to High (Needs frequent, light waterings)",
        "optimal_npk": {"N": 50, "P": 50, "K": 50},
        "optimal_ph": "6.0 to 6.5",
        "market_value": "Medium to High",
    },
    "coconut": {
        "name": "Coconut",
        "description": "A coastal crop thriving in saline soils, high humidity, warm climates, and high rainfall.",
        "season": "Perennial (Yields round the year)",
        "duration": "5 to 7 years to first yield; lives over 80 years",
        "water_requirement": "High (Requires regular coastal rain or irrigation)",
        "optimal_npk": {"N": 20, "P": 20, "K": 30},
        "optimal_ph": "5.2 to 8.0",
        "market_value": "High",
    },
    "cotton": {
        "name": "Cotton",
        "description": "A major cash crop. Requires high temperature, moderate rainfall, and black/alluvial soils with lots of sunshine.",
        "season": "Kharif (May to November)",
        "duration": "5 to 6 months",
        "water_requirement": "Moderate (50-100 cm rainfall)",
        "optimal_npk": {"N": 120, "P": 40, "K": 20},
        "optimal_ph": "5.8 to 8.0",
        "market_value": "Very High",
    },
    "jute": {
        "name": "Jute (Golden Fiber)",
        "description": "A natural fiber crop requiring standing water, high humidity, alluvial soil, and heavy rain.",
        "season": "Kharif (April to August)",
        "duration": "4 months",
        "water_requirement": "Very High (Needs moist soil and 150+ cm rain)",
        "optimal_npk": {"N": 80, "P": 40, "K": 40},
        "optimal_ph": "6.0 to 7.5",
        "market_value": "High",
    },
    "coffee": {
        "name": "Coffee",
        "description": "Grown under shade in high-altitude zones. Prefers well-drained loamy volcanic soils and humid climates.",
        "season": "Perennial (Harvested in Winter)",
        "duration": "3 to 4 years to start bearing; lives 30+ years",
        "water_requirement": "High (150-250 cm rainfall with dry winter spell)",
        "optimal_npk": {"N": 100, "P": 30, "K": 30},
        "optimal_ph": "5.0 to 6.0 (slightly acidic)",
        "market_value": "Very High",
    }
}

def analyze_soil_nutrients(crop_label, n, p, k):
    """
    Compare current soil NPK with the target crop's optimal requirements.
    Provides advice on which nutrients are high, low, or optimal, and suggests amendments.
    """
    crop_info = CROP_DETAILS.get(crop_label.lower())
    if not crop_info:
        return None
        
    optimal = crop_info["optimal_npk"]
    advice = []
    comparison = {}
    
    # Analyze Nitrogen (N)
    diff_n = n - optimal["N"]
    if abs(diff_n) <= 15:
        comparison["N"] = {"status": "Optimal", "color": "green", "value": n, "target": optimal["N"]}
    elif diff_n > 15:
        comparison["N"] = {"status": "High", "color": "red", "value": n, "target": optimal["N"]}
        advice.append({
            "nutrient": "Nitrogen (N)",
            "status": "High",
            "impact": "Excessive nitrogen causes rapid vegetative growth but delays flowering/fruiting and weakens plant resistance.",
            "remedy": "Add dry leaves, sawdust, or mulch (high-carbon materials) to tie up excess nitrogen, and avoid nitrogen-rich fertilizers."
        })
    else:
        comparison["N"] = {"status": "Low", "color": "blue", "value": n, "target": optimal["N"]}
        advice.append({
            "nutrient": "Nitrogen (N)",
            "status": "Low",
            "impact": "Nitrogen deficiency leads to stunted growth, thin stems, and yellowing of older leaves (chlorosis).",
            "remedy": "Apply Nitrogen fertilizers like Urea (46-0-0), Ammonium Nitrate, or organic blood meal and well-rotted manure."
        })
        
    # Analyze Phosphorus (P)
    diff_p = p - optimal["P"]
    if abs(diff_p) <= 15:
        comparison["P"] = {"status": "Optimal", "color": "green", "value": p, "target": optimal["P"]}
    elif diff_p > 15:
        comparison["P"] = {"status": "High", "color": "red", "value": p, "target": optimal["P"]}
        advice.append({
            "nutrient": "Phosphorus (P)",
            "status": "High",
            "impact": "Excessive phosphorus restricts the plant's ability to absorb vital micronutrients like Iron and Zinc.",
            "remedy": "Flush the soil with clean water (if in controlled beds) and avoid phosphate fertilizers. Iron and Zinc foliar sprays may help."
        })
    else:
        comparison["P"] = {"status": "Low", "color": "blue", "value": p, "target": optimal["P"]}
        advice.append({
            "nutrient": "Phosphorus (P)",
            "status": "Low",
            "impact": "Phosphorus deficiency leads to poor root development, delayed maturity, and dark green or purplish leaves.",
            "remedy": "Apply Single Superphosphate (SSP), Diammonium Phosphate (DAP), or organic bone meal and rock phosphate."
        })
        
    # Analyze Potassium (K)
    diff_k = k - optimal["K"]
    if abs(diff_k) <= 15:
        comparison["K"] = {"status": "Optimal", "color": "green", "value": k, "target": optimal["K"]}
    elif diff_k > 15:
        comparison["K"] = {"status": "High", "color": "red", "value": k, "target": optimal["K"]}
        advice.append({
            "nutrient": "Potassium (K)",
            "status": "High",
            "impact": "Excessive potassium interferes with the uptake of Magnesium and Calcium, leading to nutrient deficiencies.",
            "remedy": "Reduce potassium additions, flush soil if possible, and apply Magnesium sulfate (Epsom salt) if deficiency signs appear in leaves."
        })
    else:
        comparison["K"] = {"status": "Low", "color": "blue", "value": k, "target": optimal["K"]}
        advice.append({
            "nutrient": "Potassium (K)",
            "status": "Low",
            "impact": "Potassium deficiency causes leaf margins to turn yellow/brown and burn (scorch), weakens crop stems, and lowers disease resistance.",
            "remedy": "Apply Muriate of Potash (MOP), Potassium Sulfate (SOP), or organic wood ash and kelp meal."
        })
        
    return {
        "comparison": comparison,
        "advisory": advice
    }

def analyze_soil_ph(ph):
    """
    Analyze soil pH level and recommend treatment.
    """
    if ph < 5.5:
        return {
            "status": "Strongly Acidic",
            "color": "red",
            "advice": "Most plants struggle to absorb phosphorus and calcium in strongly acidic soils. Recommend applying agricultural lime (calcium carbonate) or dolomite lime to raise pH, or wood ash in small quantities."
        }
    elif 5.5 <= ph < 6.0:
        return {
            "status": "Moderately Acidic",
            "color": "orange",
            "advice": "Slightly acidic soil. Good for acid-loving crops (like coffee or potatoes) but could be raised slightly for general cropping using light lime applications."
        }
    elif 6.0 <= ph <= 7.0:
        return {
            "status": "Optimal (Neutral)",
            "color": "green",
            "advice": "Soil pH is in the optimal range. Soil nutrients are highly bioavailable. Maintain this status with balanced organic matter addition."
        }
    elif 7.0 < ph <= 8.0:
        return {
            "status": "Moderately Alkaline",
            "color": "orange",
            "advice": "Slightly alkaline soil. Suitable for crops like cabbage, chickpea, or cotton. To lower pH slightly, add compost, manure, or peat moss."
        }
    else:
        return {
            "status": "Strongly Alkaline",
            "color": "red",
            "advice": "High alkalinity reduces availability of micronutrients (iron, zinc, manganese). Recommend adding elemental sulfur, iron sulfate, or ammonium-based nitrogen fertilizers to lower pH."
        }
