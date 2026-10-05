import streamlit as st

st.set_page_config(
    page_title="Country Information App",
    page_icon="🌍"
)

countries = {
    "india": {
        "name": "India",
        "population": "1.4 Billion",
        "currency": "Indian Rupee (INR)",
        "food": "Biryani, Dosa, Samosa",
        "capital": "New Delhi",
        "places": "Taj Mahal, Red Fort, Gateway of India"
    },
    "japan": {
        "name": "Japan",
        "population": "123 Million",
        "currency": "Japanese Yen (JPY)",
        "food": "Sushi, Ramen, Tempura",
        "capital": "Tokyo",
        "places": "Mount Fuji, Tokyo Tower, Kyoto"
    },
    "usa": {
        "name": "United States",
        "population": "340 Million",
        "currency": "US Dollar (USD)",
        "food": "Hamburger, Hot Dog, Apple Pie",
        "capital": "Washington, D.C.",
        "places": "Statue of Liberty, Grand Canyon, Times Square"
    },
    "uk": {
        "name": "United Kingdom",
        "population": "69 Million",
        "currency": "Pound Sterling (GBP)",
        "food": "Fish and Chips, Pie, Roast Beef",
        "capital": "London",
        "places": "Big Ben, London Eye, Stonehenge"
    },
    "canada": {
        "name": "Canada",
        "population": "41 Million",
        "currency": "Canadian Dollar (CAD)",
        "food": "Poutine, Maple Syrup, Butter Tarts",
        "capital": "Ottawa",
        "places": "Niagara Falls, Banff National Park, CN Tower"
    },
    "australia": {
        "name": "Australia",
        "population": "27 Million",
        "currency": "Australian Dollar (AUD)",
        "food": "Meat Pie, Pavlova, Vegemite",
        "capital": "Canberra",
        "places": "Sydney Opera House, Great Barrier Reef, Uluru"
    },
    "france": {
        "name": "France",
        "population": "68 Million",
        "currency": "Euro (EUR)",
        "capital": "Washington, D.C.",
        "places": "Statue of Liberty, Grand Canyon, Times Square"
    },

    
    "uk": {
        "name": "United Kingdom",
        "population": "69 Million",
        "currency": "Pound Sterling (GBP)",
        "food": "Fish and Chips, Pie, Roast Beef",
        "capital": "London",
        "places": "Big Ben, London Eye, Stonehenge"
    },

    "canada": {
        "name": "Canada",
        "population": "41 Million",
        "currency": "Canadian Dollar (CAD)",
        "food": "Poutine, Maple Syrup, Butter Tarts",
        "capital": "Ottawa",
        "places": "Niagara Falls, Banff National Park, CN Tower"
    },

    "australia": {
        "name": "Australia",
        "population": "27 Million",
        "currency": "Australian Dollar (AUD)",
        "food": "Meat Pie, Pavlova, Vegemite",
        "capital": "Canberra",
        "places": "Sydney Opera House, Great Barrier Reef, Uluru"
    },

    "france": {
        "name": "France",
        "population": "68 Million",
        "currency": "Euro (EUR)",
        "food": "Croissant, Baguette, Crêpe",
        "capital": "Paris",
        "places": "Eiffel Tower, Louvre Museum, Palace of Versailles"
    },

    "germany": {
        "name": "Germany",
        "population": "84 Million",
        "currency": "Euro (EUR)",
        "food": "Bratwurst, Pretzel, Sauerbraten",
        "capital": "Berlin",
        "places": "Brandenburg Gate, Neuschwanstein Castle, Berlin Wall"
    },

    "italy": {
        "name": "Italy",
        "population": "59 Million",
        "currency": "Euro (EUR)",
        "food": "Pizza, Pasta, Gelato",
        "capital": "Rome",
        "places": "Colosseum, Venice, Leaning Tower of Pisa"
    },

    "china": {
        "name": "China",
        "population": "1.4 Billion",
        "currency": "Chinese Yuan (CNY)",
        "food": "Fried Rice, Dumplings, Peking Duck",
        "capital": "Beijing",
        "places": "Great Wall of China, Forbidden City, Terracotta Army"
    },

    "brazil": {
        "name": "Brazil",
        "population": "216 Million",
        "currency": "Brazilian Real (BRL)",
        "food": "Feijoada, Coxinha, Pão de Queijo",
        "capital": "Brasília",
        "places": "Christ the Redeemer, Amazon Rainforest, Copacabana Beach"
    },

    "south_africa": {
        "name": "South Africa",
        "population": "63 Million",
        "currency": "South African Rand (ZAR)",
        "food": "Bobotie, Biltong, Bunny Chow",
        "capital": "Pretoria",
        "places": "Table Mountain, Kruger National Park, Cape of Good Hope"
    },

    "russia": {
        "name": "Russia",
        "population": "144 Million",
        "currency": "Russian Ruble (RUB)",
        "food": "Borscht, Pelmeni, Blini",
        "capital": "Moscow",
        "places": "Red Square, Kremlin, Lake Baikal"
    },

    "mexico": {
        "name": "Mexico",
        "population": "130 Million",
        "currency": "Mexican Peso (MXN)",
        "food": "Tacos, Enchiladas, Tamales",
        "capital": "Mexico City",
        "places": "Chichen Itza, Cancun, Teotihuacan"
    },

    "uae": {
        "name": "United Arab Emirates",
        "population": "11 Million",
        "currency": "UAE Dirham (AED)",
        "food": "Shawarma, Machboos, Hummus",
        "capital": "Abu Dhabi",
        "places": "Burj Khalifa, Palm Jumeirah, Sheikh Zayed Grand Mosque"
    }
}


st.title("🌍 Country Information App")

country = st.text_input(
    "🌎 Enter Country Name",
    placeholder="Example: India"
)

if st.button("🔍 Search Country"):

    key = country.strip().lower()

    if key in countries:

        data = countries[key]

        st.success(
            f"Information found for {data['name']}"
        )

        st.header(f"🌍 {data['name']}")

        st.write(
            f"👥 **Population:** {data['population']}"
        )

        st.write(
            f"💰 **Currency:** {data['currency']}"
        )

        st.write(
            f"🍛 **Popular Food:** {data['food']}"
        )

        st.write(
            f"🏙️ **Capital:** {data['capital']}"
        )

        st.write(
            f"📍 **Famous Places:** {data['places']}"
        )

    else:

        st.error(
            "❌ Country not available."
        )
