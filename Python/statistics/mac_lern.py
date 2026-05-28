import nltk
from nltk.chat.util import Chat,reflections

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by OpenAI. You can call me ChatGPT.",]
    ],
    [
        r"i am fine|i am doing good|i am well",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"how are you ?",
        ["Its alright."]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"i am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright ?)",]
    ],
    [
        r"age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["My parents created me using machine language.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am based on the cloud, so I do not have a physical location.',]
    ],
    [
        r"how is the weather in (.*)?",
        ["I don't have access to real-time weather data, but you can check a weather website or app for the current conditions in %1.",]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an interesting field! What do you do there?",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past few days in %2", "In %2 there is a 50% chance of rain today",]
    ],
    [
        r"how (.*) health(.*)?",
        ["Health is very important, but I am just a computer program, so I don't have health issues.",]
    ],
    [
        r"(.*) (sports|game|sport)?",
        ["I'm a big fan of soccer.",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Neymar",]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt", "Leonardo DiCaprio", "Scarlett Johansson",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. See you soon!",]
    ],
    [
        r"bye",
        ["Type quit to exit.",]
    ]
    
]

def chat():
    print("Hi! I'm a chatbot created by OpenAI. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()