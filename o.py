import streamlit as st
import speech_recognition as sr
import pyttsx3
import editdistance

qa_dict ={'what is your name': 'My name is ChatBot.', 'how are you': "I'm just a program, so I don't have feelings, but I'm here to assist you!", 'what can you do': 'I can help answer questions, provide information, and assist with various tasks.', 'where are you from': "I exist in the digital realm, so you could say I'm from the internet.", 'how old are you': "I don't have an age in the human sense. I was created by OpenAI.", 'who created you': 'I was created by a team of developers at OpenAI.', 'what is the meaning of life': "That's a philosophical question with many possible answers. Some say it's to seek happiness or fulfillment.", 'what is the capital of france': 'The capital of France is Paris.', 'who is the president of the united states': "I'm sorry, I don't have access to real-time information. As of my last update, I'm not aware of the current president.", 'how do you spell cat': 'C-A-T.', 'what is the square root of 64': 'The square root of 64 is 8.', 'what is the tallest mountain in the world': 'Mount Everest is the tallest mountain above sea level.', 'how do you say hello in spanish': 'Hola.', 'what is the chemical symbol for water': 'H2O.', 'how many continents are there': 'There are seven continents on Earth.', 'what is the largest ocean': 'The Pacific Ocean is the largest ocean.', 'how do you convert celsius to fahrenheit': 'Multiply Celsius temperature by 9/5 and add 32.', 'what is the population of china': "As of my last update, China's population is over 1.4 billion.", 'who wrote romeo and juliet': 'William Shakespeare wrote Romeo and Juliet.', 'what is the chemical formula for table salt': 'The chemical formula for table salt is NaCl.', 'what is the speed of light': 'The speed of light in a vacuum is approximately 299,792 kilometers per second.', 'what is the capital of japan': 'The capital of Japan is Tokyo.', 'who discovered gravity': 'Sir Isaac Newton is credited with discovering gravity.', 'what is the largest mammal': 'The blue whale is the largest mammal on Earth.', 'how many planets are there in the solar system': 'There are eight planets in our solar system.', 'who painted the mona lisa': 'Leonardo da Vinci painted the Mona Lisa.', 'what causes tides': 'The gravitational pull of the moon and the sun causes tides.', 'what is the capital of brazil': 'The capital of Brazil is Brasília.', 'what is photosynthesis': 'Photosynthesis is the process by which plants convert light energy into chemical energy.', 'how many bones are in the human body': 'The adult human body has 206 bones.', 'what is the currency of japan': 'The currency of Japan is the Japanese yen.', 'who wrote 1984': 'George Orwell wrote 1984.', 'what is the chemical symbol for gold': 'The chemical symbol for gold is Au.', 'what is the largest desert in the world': 'The largest desert in the world is the Antarctic Desert.', 'how many time zones are there in the world': 'There are 24 time zones in the world.', 'who discovered penicillin': 'Alexander Fleming is credited with the discovery of penicillin.', 'what is the national animal of australia': 'The national animal of Australia is the kangaroo.', 'what is the smallest country in the world': 'The smallest country in the world is Vatican City.', 'what is the capital of australia': 'The capital of Australia is Canberra.', 'what is the tallest building in the world': 'The tallest building in the world is the Burj Khalifa in Dubai.', 'how long is the great wall of china': 'The Great Wall of China is approximately 13,170 miles long.', 'what is the boiling point of water in fahrenheit': 'The boiling point of water is 212 degrees Fahrenheit.', 'who is the author of to kill a mockingbird': 'Harper Lee is the author of To Kill a Mockingbird.', 'what is the chemical symbol for oxygen': 'The chemical symbol for oxygen is O.', 'what is the largest bird in the world': 'The ostrich is the largest bird in the world.', 'what is the capital of india': 'The capital of India is New Delhi.', 'what is the chemical formula for methane': 'The chemical formula for methane is CH4.', 'what is the currency of china': 'The currency of China is the Chinese yuan.', 'who wrote pride and prejudice': 'Jane Austen wrote Pride and Prejudice.', 'what is the chemical symbol for carbon': 'The chemical symbol for carbon is C.', 'what is the diameter of earth': 'The diameter of Earth is approximately 12,742 kilometers.', 'what is the capital of russia': 'The capital of Russia is Moscow.', 'what is the chemical formula for glucose': 'The chemical formula for glucose is C6H12O6.', 'what is the national flower of japan': 'The national flower of Japan is the cherry blossom.', 'what is the chemical symbol for sodium': 'The chemical symbol for sodium is Na.', 'who is known as the father of modern physics': 'Albert Einstein is often referred to as the Father of Modern Physics.', 'what is the chemical formula for water': 'The chemical formula for water is H2O.', 'what is the currency of india': 'The currency of India is the Indian rupee.', 'who discovered electricity': "Electricity wasn't discovered by a single person, but Benjamin Franklin's experiments with lightning contributed to our understanding of it.", 'what is the chemical symbol for helium': 'The chemical symbol for helium is He.', 'what is the tallest tree in the world': 'The tallest tree in the world is Hyperion, a coast redwood in California.', 'what is the capital of china': 'The capital of China is Beijing.', 'who wrote hamlet': 'William Shakespeare wrote Hamlet.', 'what is the chemical formula for sulfuric acid': 'The chemical formula for sulfuric acid is H2SO4.', 'what is the national animal of canada': 'The national animal of Canada is the beaver.', 'what is the chemical symbol for silver': 'The chemical symbol for silver is Ag.', 'who discovered america': 'Christopher Columbus is often credited with discovering America, although it was already inhabited by indigenous peoples.', 'what is the chemical formula for carbon dioxide': 'The chemical formula for carbon dioxide is CO2.', 'what is the currency of russia': 'The currency of Russia is the Russian ruble.', 'who wrote the great gatsby': 'F. Scott Fitzgerald wrote The Great Gatsby.', 'what is the chemical symbol for iron': 'The chemical symbol for iron is Fe.', 'what is the national bird of the united states': 'The national bird of the United States is the bald eagle.', 'what is the chemical formula for ammonia': 'The chemical formula for ammonia is NH3.', 'what is the tallest animal in the world': 'The giraffe is the tallest animal in the world.', 'what is the chemical symbol for potassium': 'The chemical symbol for potassium is K.', 'what is the currency of germany': 'The currency of Germany is the euro.', 'who wrote the catcher in the rye': 'J.D. Salinger wrote The Catcher in the Rye.', 'what is the chemical formula for nitric acid': 'The chemical formula for nitric acid is HNO3.', 'what is the national animal of india': 'The national animal of India is the Bengal tiger.', 'what is the chemical symbol for nitrogen': 'The chemical symbol for nitrogen is N.', 'what is the currency of brazil': 'The currency of Brazil is the Brazilian real.', 'who wrote the odyssey': 'Homer is credited with writing The Odyssey.', 'what is the chemical formula for hydrochloric acid': 'The chemical formula for hydrochloric acid is HCl.', 'what is the national animal of china': 'The national animal of China is the giant panda.', 'what is the chemical symbol for phosphorus': 'The chemical symbol for phosphorus is P.', 'what is the currency of the united kingdom': 'The currency of the United Kingdom is the British pound sterling.', 'who wrote war and peace': 'Leo Tolstoy wrote War and Peace.', 'what is the chemical formula for aspirin': 'The chemical formula for aspirin is C9H8O4.', 'what is the national animal of russia': 'The national animal of Russia is the brown bear.', 'what is the chemical symbol for calcium': 'The chemical symbol for calcium is Ca.', 'what is the currency of france': 'The currency of France is the euro.', 'who wrote the lord of the rings': 'J.R.R. Tolkien wrote The Lord of the Rings.', 'what is the chemical formula for table sugar': 'The chemical formula for table sugar is C12H22O11.', 'what is the chemical symbol for neon': 'The chemical symbol for neon is Ne.', 'what is the currency of canada': 'The currency of Canada is the Canadian dollar.', 'who wrote moby dick': 'Herman Melville wrote Moby Dick.', 'what is the chemical formula for carbon monoxide': 'The chemical formula for carbon monoxide is CO.', 'what is the national animal of brazil': 'The national animal of Brazil is the jaguar.', 'what is the chemical symbol for magnesium': 'The chemical symbol for magnesium is Mg.'}

all_keys = list(qa_dict.keys())

def preprocess_input(text):
    intput_text = text
    similarity = []
    for i in all_keys:
        distance = editdistance.eval(intput_text, i)
        similarity_ratio = 1 - distance / max(len(intput_text), len(i))
        similarity.append(str(similarity_ratio) + " " + i)
    max_simil_key = max(similarity)

    text = max_simil_key

    first_space_index = text.find(' ')

    intput_key = text[first_space_index + 1:]
    return intput_key

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)

    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        st.write(f"User said: {query}")
        return preprocess_input(query)
    except Exception as e:
        st.error(e)
        return ""

def assistant():
    speak("Hello! How can I assist you today?")
    query = listen()
    if query in qa_dict:
        speak(qa_dict[query])
        st.write("Assistant: "+qa_dict[query])
    else:
        speak("I'm sorry, I didn't understand that.")

def main():
    st.title("Speech Recognition Chatbot")
    st.write("Speak when Listning... on Screen")
    if st.button("Start Chat"):
        assistant()

if __name__ == "__main__":
    main()
