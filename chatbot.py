import time

def school_bot():
    print("🤖 SchoolBot: Hello! I am your AI School Assistant. What is your name?")
    user_name = input("✍️ You: ")
    print(f"🤖 SchoolBot: Nice to meet you, {user_name}! How can I help you today?")
    print("(Type 'exit' or 'bye' to close the chat)\n")

    while True:
        user_input = input(f"✍️ {user_name}: ").lower()

        if 'exit' in user_input or 'bye' in user_input:
            print(f"🤖 SchoolBot: Goodbye, {user_name}! Have a great day ahead! 👋")
            break
        elif 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            print("🤖 SchoolBot: Hello there! Hope your studies are going well. What can I check for you?")
        elif 'exam' in user_input or 'timetable' in user_input or 'date sheet' in user_input:
            print("🤖 SchoolBot: 📅 The Class 10 Pre-Board exams start next Monday. Ensure your syllabus is revised!")
        elif 'syllabus' in user_input or 'ai code' in user_input:
            print("🤖 SchoolBot: 📚 The AI curriculum (Subject Code 417) includes Introduction to AI, AI Project Cycle, CV, NLP, and Data Science.")
        elif 'timing' in user_input or 'time' in user_input or 'hours' in user_input:
            print("🤖 SchoolBot: 🕒 The regular school timings are from 8:00 AM to 2:00 PM. Remedial classes run till 3:00 PM.")
        elif 'boring' in user_input or 'joke' in user_input:
            print("🤖 SchoolBot: Here is a quick one: Why did the computer squeak? Because someone stepped on its mouse! 🐭")
        else:
            print("🤖 SchoolBot: 🤔 I am sorry, I didn't quite catch that. Could you ask about 'exams', 'syllabus', or 'school timings'?")
        
        print("-" * 40)
        time.sleep(0.5)

if __name__ == "__main__":
    school_bot()
