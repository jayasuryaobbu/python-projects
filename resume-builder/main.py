import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from textblob import TextBlob
import collections
from tkinter import messagebox


root = tk.Tk()
root.title("Resume Builder")
each_word = []
skills_lines = []
only_skills = []
only_skill_categories = []
need_skill_categories = []
matched_skills = []
need_skills = []

window_frame = tk.Canvas(root, width=600, height=800)
window_frame.pack()


def compare_keywords(each_word):

    '''read lines from skills text file'''
    skills_file = open("skills.txt", "r")
    text_lines = skills_file.readlines()
    for x in range(len(text_lines)):
        new_word = text_lines[x].split('\n')
        skills_lines.append(new_word[0])
    '''separate skills from their categories and store them in different lists '''
    for y in range(len(skills_lines)):
        only_skill_word = skills_lines[y].split(' - ')
        only_skill_categories.append(only_skill_word[-1].casefold())
        only_skills.append(only_skill_word[0].casefold())

    '''Check for matching skills and get the skills candidate posses'''
    compare_skills_lists = [string for string in only_skills if string in each_word]
    for a in range(len(compare_skills_lists)):
        for b in range(len(only_skills)):
            if compare_skills_lists[a] == only_skills[b]:
                need_skill_categories.append(only_skill_categories[b].casefold())
                need_skills.append(only_skills[b].casefold())

    '''get the most frequent skill category'''
    matching_category = collections.Counter(need_skill_categories)
    matched_category = matching_category.most_common(1)
    first_tuple_elements = [a_tuple[0] for a_tuple in matched_category]

    '''now get the skills matched with the most frequent skill category'''
    for c in range(len(need_skill_categories)):
        if first_tuple_elements[0] == need_skill_categories[c]:
            matched_skills.append(need_skills[c].casefold())

    '''remove any repeated skills and add remaining to a list'''
    nonrepeated = collections.Counter(matched_skills)
    non_rep = list(nonrepeated.keys())

    '''we now got which category application it is and also the skills candidate posses for that'''
    print("This Job is related to " + first_tuple_elements[0] + "\n")
    print("And you have the following skills from that job: ")
    for d in range(len(non_rep)):
        print(str(non_rep[d]))


def build_keywords(title_info, description_info):

    '''get all words in the texts'''
    all_words_in_title = title_info.split()
    all_words_in_description = description_info.split()
    '''get noun phrases from texts'''
    nouns_in_title = TextBlob(title_info)
    title_keywords = nouns_in_title.noun_phrases
    nouns_in_description = TextBlob(description_info)
    description_keywords = nouns_in_description.noun_phrases
    '''get verbs from texts'''
    is_verb = lambda pos: pos[:2] == 'VB'
    tokenized_title = nltk.word_tokenize(title_info)
    verbs_in_title = [word for (word, pos) in nltk.pos_tag(tokenized_title) if is_verb(pos)]
    tokenized_description = nltk.word_tokenize(description_info)
    verbs_in_description = [word for (word, pos) in nltk.pos_tag(tokenized_description) if is_verb(pos)]

    '''keywords_file_search = open("keywords.txt", "r")
    text_lines = keywords_file_search.readlines()
    for x in range(len(text_lines)):
        new_word = text_lines[x].split('\n')
        each_word.append(new_word[0].casefold())
    filtered_title_list = [string for string in title_keywords if string not in each_word]
    filtered_description_list = [string for string in description_keywords if string not in each_word]
    fil_ver_title = [string for string in verbs_in_title if string not in each_word]
    fil_ver_description = [string for string in verbs_in_description if string not in each_word]

    for y in range(len(filtered_title_list)):
        each_word.append(filtered_title_list[y].casefold())
    for x in range(len(filtered_description_list)):
        each_word.append(filtered_description_list[x].casefold())
    for a in range(len(fil_ver_title)):
        each_word.append(fil_ver_title[a].casefold())
    for b in range(len(fil_ver_description)):
        each_word.append(fil_ver_description[b].casefold())

    keywords_file_search.close()
    keywords_file = open("keywords.txt", "r+")
    keywords_file.truncate(0)
    keywords_file.close()'''

    '''add all words, noun phrases, verbs to each_word list'''
    for y in range(len(title_keywords)):
        each_word.append(title_keywords[y].casefold())
    for x in range(len(description_keywords)):
        each_word.append(description_keywords[x].casefold())
    for a in range(len(verbs_in_title)):
        each_word.append(verbs_in_title[a].casefold())
    for b in range(len(verbs_in_description)):
        each_word.append(verbs_in_description[b].casefold())
    for c in range(len(all_words_in_title)):
        each_word.append((all_words_in_title[c].casefold()))
    for d in range(len(all_words_in_description)):
        each_word.append(all_words_in_description[d].casefold())

    '''now execute compare_keywords function'''
    compare_keywords(each_word)


def generate_resume():

    """get text written in text and description fields"""
    title_text = position_title_text.get(1.0, tk.END)
    description_text = job_description_text.get(1.0, tk.END)

    '''check for filled fields otherwise throw an error
        if fields are filled execute build_keywords function'''
    if len(title_text) == 1:
        messagebox.showinfo("Error!!", "Text Field is empty!!")
    elif len(description_text) == 1:
        messagebox.showinfo("Error!!", "Description Box is Empty!!")
    else:
        build_keywords(title_text, description_text)


position_title_label = tk.Label(root, text="Enter the Job Title")
window_frame.create_window(60, 40, window=position_title_label)

position_title_text = tk.Text(root, width=60, height=3)
window_frame.create_window(255, 80, window=position_title_text)

job_description_label = tk.Label(root, text="Enter the Job Description")
window_frame.create_window(78, 120, window=job_description_label)

job_description_text = ScrolledText(root, width=60, height=9)
window_frame.create_window(262, 210, window=job_description_text)

'''With click execute generate_resume function'''
submit_button = tk.Button(root, text="Submit", command=generate_resume)
window_frame.create_window(262, 310, window=submit_button)


root.mainloop()
