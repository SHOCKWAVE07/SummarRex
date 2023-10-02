# roles.py

roles = {
    "Programmer": {
        "description": "Programming expert | coding | Advanced DSA",
        "model": "gpt-3.5-turbo",
    },
    "Medical Student": {
        "description": "Medical expert | medicine | treatment",
        "model": "gpt-3.5-turbo",
    },
    "Lawyer": {
        "description": "Lawyer | Indian Penal Code | Indian Constitution",
        "model": "gpt-3.5-turbo",
    },
    "Financial Analyst": {
        "description": "Finance | Personal Finance | Financial Analyst",
        "model": "ft:gpt-3.5-turbo-0613:personal::856a6IE6",
    },
    "Default": {
        "description": "An Average Human Being",
        "model": "gpt-3.5-turbo",
    },
    "Personalized": {
        "description": "An Average Human Being",
        "model": "ft:gpt-3.5-turbo-0613:personal::856xPFIF",
    },
}

# Set the default role and associated model
default_role = "Default"
role_selected = default_role
selected_model = roles[default_role]["model"]