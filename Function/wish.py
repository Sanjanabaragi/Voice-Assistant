from datetime import datetime, date
from Head.Mouth import speak
import random

def wish():
    today = date.today()
    formatted_date = today.strftime("%A, %d %B %Y")
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    hour = now.hour

    if 5 <= hour < 12:
        greeting = random.choice([
            "Good morning", "Rise and shine", "Top of the morning", "A beautiful morning to you"
        ])
        quote = random.choice([
            "Every morning is a new opportunity to chase your dreams.",
            "Wake up with determination, go to bed with satisfaction.",
            "The sun is up, the sky is blue, it's beautiful—and so are you.",
            "Success comes to those who hustle early."
        ])
    elif 12 <= hour < 17:
        greeting = random.choice([
            "Good afternoon", "Hope your day is going well", "A wonderful afternoon to you"
        ])
        quote = random.choice([
            "Keep pushing, the best is yet to come.",
            "Stay positive, work hard, and make it happen.",
            "Your energy introduces you even before you speak.",
            "Midday is the perfect time to refocus and re-energize."
        ])
    elif 17 <= hour < 21:
        greeting = random.choice([
            "Good evening", "Hope your day was productive", "Wishing you a peaceful evening"
        ])
        quote = random.choice([
            "Take time to do what makes your soul happy.",
            "Evenings are life's way of saying: You survived the day. Good job!",
            "Relax. Recharge. Reflect.",
            "Let the evening calm your soul."
        ])
    else:
        greeting = random.choice([
            "Good night", "Time to rest now", "Sweet dreams", "Wishing you a restful night"
        ])
        quote = random.choice([
            "Tomorrow is a new chance to do great things.",
            "Sleep well. Your dreams are waiting.",
            "Let today’s worries drift away. Rest well.",
            "Recharge your body and mind tonight."
        ])

    message = f"{greeting}! It's {formatted_date}, and the time is {current_time}. {quote}"
    speak(message)
wish()