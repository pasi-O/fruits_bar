# 🍎 Fruit Facts Search App

A simple and friendly Flask web application that displays fun fruit facts using clean, minimal fruit cards. The app includes a search bar that lets users filter fruits by name, making it easy to explore the collection. All fruit data is stored in a Python dictionary, keeping the project lightweight and easy to extend.

---

## ✨ Features

### 🔍 Search Bar  
A simple search bar allows users to filter fruits by name.  
The search is case‑insensitive and updates the displayed results based on the query.

### 🍓 Fruit Cards  
Each fruit is displayed as a card containing:
- The fruit’s name  
- A fun fact 

```python
fruit_facts = {
    "Apple": "Apples float in water because they are 25% air.",
    "Banana": "Bananas are berries, but strawberries are not.",
    ...
}
