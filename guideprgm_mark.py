#To show where you have to work like on which subject and which subject is your strong
def subjectn(verify,value):
    for key in verify:
        
        if verify[key]==value:
            return key 
    return None
            
n=1
name=input("Enter your name ")
verify={}

def advisor():
    # try:
    subjects=("English","Hindi", "Physics", "Chemistry","Maths")
    for subject in subjects:
        print(f"Enter you mark in {subject} : ")
        mark=int(input())
        verify [subject]=mark
       
        if (mark<5 or mark>100):
            raise ValueError("Mark should be between 10 and 100 ")
        mark_list=verify.values()
        print('Confirm you marks. "press Enter" or write "change" ')
        print(verify)


    # except ValueError:
    #     print("You enter wronge number or any non-integer value .")
    

    confirm= input()
    if confirm == "":
    
        only_mark=list(mark_list)
        only_mark.sort()
        for index,marks in enumerate(only_mark):
            
            if index ==0:
                weaksub_index=only_mark[index]
                weaksub=subjectn( verify ,weaksub_index)
                
                print(f"""For Weak subject :
                    Hey {name},

    I wanted to talk to you about your recent marks in {weaksub}. I know you may be disappointed, but I believe in your ability to do better next time.

    Remember, one mark doesn't define you or your potential. It's just a chance to learn and improve. Here are some tips to help you score better next time:

    1. Reflect on your mistakes: Take a look at where you went wrong and figure out which areas you struggled with the most. Understanding your weaknesses will help you focus your efforts.

    2. Talk to your teacher: Don't hesitate to ask your teacher for help. They're there to support you and provide extra guidance. Reach out and ask questions or clarify any doubts you have.

    3. Make a study plan: Create a schedule that includes dedicated study time for [subject]. Break it down into smaller, manageable chunks, and stick to your plan.

    4. Use available resources: Take advantage of textbooks, online tutorials, and practice exercises. They can provide different explanations and examples to help you understand the concepts better.

    5. Study with others: Consider forming study groups with classmates who excel in [subject]. You can learn from each other, discuss challenging topics, and support one another.

    6. Practice consistently: Regular practice is key to improving in any subject. Set aside time each day to practice [subject] and work on problem-solving.

    Stay positive and don't get discouraged. You have the potential to do great things. Keep working hard, believe in yourself, and you'll see progress.

    If you need any further help or have any questions, feel free to reach out to me or your teacher. We're here to support you.

    Best of luck, and keep pushing forward!

    """)
                weaksub=subjectn(verify,weaksub_index)
                if weaksub=="English":
                    print(f"""
                        Dear {name},

    I hope this message finds you well. I recently received your exam results, and I noticed that you scored lower than expected in English. I understand that English might not be your strongest subject, but I believe in your potential to improve and excel in it.

    Firstly, I want you to know that receiving a lower mark in English does not define your abilities or intelligence. It is simply an opportunity for growth and learning. English is a language that can be challenging for many students, but with dedication and practice, you can definitely improve your skills.

    Here are a few suggestions to help you work on your English and enhance your performance in the subject:

    1. Identify your weak areas: Take some time to reflect on which specific aspects of English are more challenging for you. Is it grammar, vocabulary, reading comprehension, or writing? By identifying these areas, you can focus your efforts more effectively.

    2. Seek additional resources: Explore different resources that can supplement your learning. There are numerous online platforms, textbooks, grammar guides, and interactive exercises available. Utilize them to practice and reinforce your understanding of the language.

    3. Practice regularly: Consistency is key when it comes to improving your English skills. Dedicate a specific amount of time each day or week to practice reading, writing, listening, and speaking in English. Engage in conversations, read English books or articles, and try to write short essays or paragraphs regularly.

    4. Ask for help: Don't hesitate to reach out to your English teacher or classmates for assistance. They can provide guidance, clarify concepts, and offer additional study materials. Working together with others who share similar goals can be motivating and beneficial.

    5. Stay motivated: Remember, progress takes time, and setbacks are a natural part of the learning process. Stay motivated and believe in your ability to improve. Celebrate even small achievements, as they will eventually add up to significant progress.

    I have faith in your ability to turn things around and achieve better results in English. Remember, the goal is not just to score well but also to develop a strong foundation in the language that will benefit you throughout your academic and professional journey.

    If you need any further assistance or guidance, please don't hesitate to ask. Keep up the hard work, stay focused, and I'm confident that you will see improvement in no time.

    Best of luck!

    Warm regards,
    {name}""")
                
                elif (weaksub=="Hindi"):
                    print(f"""Dear {name},

    I hope this message finds you well. I recently learned that you received a lower score in the subject of Hindi, and I wanted to offer you some tips and tricks to help you improve in this subject. While Hindi may be challenging for you right now, with the right approach and effort, you can certainly excel in it.

    1. Build your vocabulary: Hindi, like any language, relies heavily on vocabulary. Start by dedicating some time each day to learn new words and their meanings. You can use flashcards or digital apps to make this process more engaging and interactive.

    2. Practice reading Hindi texts: Reading Hindi books, newspapers, or online articles can greatly enhance your understanding of the language. Start with simpler texts and gradually move on to more complex ones as your proficiency increases. This will improve your comprehension skills and help you become familiar with different sentence structures.

    3. Focus on grammar: Hindi grammar might seem intimidating, but mastering its basics is crucial for overall proficiency. Dedicate time to studying grammar rules, verb conjugations, noun declensions, and sentence formations. You can find numerous online resources, textbooks, or even seek guidance from your Hindi teacher.

    4. Engage in conversations: Actively participate in Hindi conversations with your friends, family members, or classmates who are fluent in the language. Regular practice will improve your speaking skills, boost your confidence, and help you become more comfortable with the language.

    5. Watch Hindi movies and TV shows: Immersing yourself in the Hindi language through movies, TV shows, or even YouTube videos can be a fun and effective way to improve your listening skills. Pay attention to the dialogue, pronunciation, and intonation to enhance your comprehension.

    6. Seek extra help: If you're still struggling despite your efforts, don't hesitate to seek extra help. Your Hindi teacher or a tutor can provide personalized guidance, clarify doubts, and offer additional resources to support your learning.

    Remember, improvement takes time and consistent effort. Be patient with yourself and stay determined. Practice regularly, set realistic goals, and celebrate your progress along the way. With dedication and the right approach, I have no doubt that you can achieve better results in Hindi.

    Wishing you the best of luck! Keep up the hard work, and I believe you'll see significant improvements soon.

    Sincerely,

    {name}""")
                elif (weaksub=="Physics"):
                    print(f""" 
    Hey {name},

    I heard about your recent physics exam results, and I understand that you're disappointed with your score. Don't worry, though! I'm here to offer you some advice on how to improve in physics:

    1. Don't be discouraged: Remember that a low score doesn't define your abilities. It's just a starting point for improvement.

    2. Identify your weak areas: Take a close look at the topics or concepts that you struggled with the most. Focus on understanding them better.

    3. Seek help when needed: Don't hesitate to ask your teacher or classmates for explanations or clarifications. There are also plenty of online resources and videos that can help you grasp difficult concepts.

    4. Practice regularly: Physics requires practice to reinforce your understanding. Solve as many problems as you can, starting with easier ones and gradually working your way up to more complex ones.

    5. Visualize and draw diagrams: Physics can be abstract, so visualize concepts and draw diagrams to help you understand and remember them better.

    6. Connect with real-world examples: Relate physics principles to everyday situations. This will make the subject more relatable and easier to understand.

    7. Join study groups: Collaborate with classmates who are also working on improving their physics skills. Share ideas, solve problems together, and learn from one another.

    8. Stay organized: Keep a dedicated notebook for formulas, equations, and important concepts. Review your notes regularly to reinforce your understanding.

    9. Stay positive and motivated: Believe in yourself and your ability to improve. Stay motivated by setting small goals and celebrating your progress along the way.

    10. Don't give up: Remember that progress takes time. Stay committed, keep working hard, and don't let setbacks discourage you.

    I believe in your potential to improve in physics. You have what it takes to succeed! Keep a positive attitude, put in the effort, and you'll see improvements in no time.

    If you need any specific advice or have questions, feel free to ask. Good luck, and keep up the great work!

    Best regards,

    {name}""")
                elif (weaksub=="Chemistry"):
                    print(f"""Dear {name},

    Hey there!

    I am here that you didn't score as well as you hoped in your chemistry exam. Don't worry, it happens to the best of us. The good news is that you have the opportunity to bounce back and improve next time.

    Chemistry can be a challenging subject, but with the right approach and a little extra effort, you can definitely turn things around. Here are some tips and tricks to help you improve:

    1. Understand the fundamentals: Chemistry is built upon a foundation of key concepts and principles. Make sure you have a clear understanding of the basics before diving into more complex topics. Take the time to review your class notes and textbook thoroughly.

    2. Practice regularly: Chemistry is a subject that requires practice. Set aside dedicated study time each day to work on problem-solving and practice questions. The more you practice, the more comfortable you'll become with different types of problems.

    3. Seek additional resources: If you find your textbook or class notes aren't sufficient, don't hesitate to explore other resources. Look for online tutorials, videos, or even join a study group where you can discuss difficult concepts with peers.

    4. Ask for help: Don't be afraid to reach out to your teacher or classmates if you're struggling with a particular topic. They can provide clarification or offer alternative explanations that might help you understand better.

    5. Create a study schedule: Plan your study sessions in advance and create a schedule that allows you to cover all the topics systematically. Breaking down your study material into manageable chunks will make it less overwhelming and more achievable.

    6. Engage in active learning: Instead of passively reading or memorizing information, actively engage with the material. Take notes, create flashcards, or teach the concepts to someone else. Active learning techniques can enhance your understanding and retention of the subject.

    7. Practice problem-solving strategies: Chemistry often involves complex problem-solving. Familiarize yourself with different problem-solving strategies and learn how to apply them effectively. Practice solving a variety of problems to strengthen your skills.

    8. Review and revise regularly: Don't leave all your studying for the last minute. Review your notes and revise the material regularly, even if there's no upcoming exam. This will help reinforce your understanding and ensure you don't forget what you've learned.

    Remember, improvement takes time and effort. Be patient with yourself and stay motivated. Believe in your abilities, and with consistent practice and dedication, you'll see progress in no time.

    Best of luck! You've got this.

    {name}""")
                elif (weaksub=="Maths"):
                    print(f"""

    Dear {name},

    I hope this message finds you well. I wanted to take a moment to acknowledge your recent performance in the subject of Mathematics and offer some guidance to help you improve in this area. Remember, setbacks are an opportunity for growth, and with the right mindset and strategies, you can achieve great results.

    Mathematics can be a challenging subject, but with the right approach, you can overcome any difficulties. Here are some tips and tricks to help you improve your math skills:

    1. Understand the Fundamentals: Ensure you have a solid grasp of the fundamental concepts in mathematics. Review the basic operations, such as addition, subtraction, multiplication, and division, as they form the building blocks for more complex topics.

    2. Practice Regularly: Mathematics requires consistent practice to enhance your problem-solving abilities. Set aside dedicated time each day to work on math problems, both from your textbooks and additional resources. The more you practice, the more comfortable you'll become with different types of questions.

    3. Seek Clarification: Don't hesitate to seek clarification whenever you encounter difficulties. Ask your teacher for help, join study groups, or seek online resources that offer explanations and examples related to the topics you're struggling with. Understanding the underlying principles is crucial for success.

    4. Break It Down: When faced with a challenging problem, break it down into smaller, more manageable steps. Start by identifying what the problem is asking, then work through each step systematically. This approach will help you tackle complex problems with greater ease.

    5. Utilize Visual Aids: Mathematics often involves abstract concepts that can be better understood through visual aids. Use diagrams, charts, graphs, or any visual representation that can help you visualize the problem and its solution. Visualizing the problem can make it easier to comprehend and solve.

    6. Practice Problem-Solving Strategies: Familiarize yourself with different problem-solving strategies, such as working backward, drawing a diagram, or using logical reasoning. Experiment with various approaches to find the ones that work best for you.

    7. Review and Reflect: After completing a math assignment or test, take the time to review your answers and identify any mistakes you made. Reflect on what went wrong and how you can improve. Learning from your mistakes is an essential part of the learning process.

    Remember, improving in mathematics takes time and effort. Stay motivated, remain persistent, and don't be discouraged by temporary setbacks. With consistent practice and the right mindset, you can definitely improve your math skills.

    Believe in yourself and keep pushing forward. I have faith in your ability to excel in mathematics. If you need any further assistance or have specific questions, don't hesitate to reach out to me or your teacher.

    Best of luck with your studies!



    {name}""")

                elif index==4:
                    print(f"""So its strong sunject
                        Dear {name},

    I hope this message finds you well. I wanted to take a moment to congratulate you on your excellent performance in [Subject]. Your dedication and hard work have clearly paid off, and I wanted to commend you on your achievements.

    Having a strong subject is a testament to your passion, effort, and commitment to learning. It's wonderful to see how well you have grasped the concepts and excelled in this particular subject. Your success is a result of your perseverance and the time you've invested in studying and understanding the material.

    I encourage you to continue nurturing your skills in this subject. Here are a few suggestions to help you maintain your excellent performance:

    1. Stay Consistent: Continue dedicating regular time to study and revise the subject. Consistency is key to maintaining a strong foundation and staying on top of any new concepts or updates.

    2. Stay Engaged: Keep yourself engaged and motivated in the subject by exploring related topics beyond the classroom. Look for additional resources, books, articles, or documentaries that delve deeper into the subject matter. This will not only broaden your knowledge but also keep your enthusiasm alive.

    3. Share Your Knowledge: Consider sharing your expertise with your peers or classmates who may be struggling in the subject. Tutoring or explaining concepts to others can solidify your understanding and help you reinforce what you've learned.

    4. Challenge Yourself: Look for opportunities to challenge yourself further in the subject. Participate in advanced-level competitions or seek out specialized courses or workshops that can enhance your skills. Pushing your boundaries will not only deepen your understanding but also provide new perspectives and insights.

    5. Seek Guidance: Even though you excel in this subject, don't hesitate to seek guidance or clarification whenever needed. Reach out to your teacher or mentors for any questions or concerns you may have. Their expertise and insights can help you refine your knowledge and take it to the next level.

    Remember, success is a continuous journey. Celebrate your achievements but never stop growing and learning. Your passion and dedication have brought you this far, and I have no doubt that you will continue to thrive in [Subject].

    Keep up the fantastic work, and I wish you continued success in all your academic endeavors!



    {name}""")
                    
            elif index==3:
                print(f"""Dear {name},
                    

    I hope this message finds you well. I wanted to take a moment to discuss your performance in one of your subjects, which seems to be averaging out. While it's great that you are doing well in some areas, it's important to focus on improving your performance in this particular subject. I believe in your potential to excel, and with the right approach, you can elevate your performance and achieve better results.

    Here are some tips and strategies to help you improve in your average subject:

    1. Self-Reflection: Take some time to reflect on your study habits and approach to this subject. Are you putting in enough effort? Are there any specific areas or concepts that you find challenging? Identifying the areas that need improvement is the first step towards progress.

    2. Seek Guidance: Don't hesitate to seek guidance from your teacher or instructor. They can provide valuable insights, clarify concepts, and offer additional resources that can aid your understanding. Reach out to them and express your interest in improving. They will appreciate your initiative and support your efforts.

    3. Study Routine: Establish a consistent study routine for this subject. Allocate specific time slots in your schedule dedicated to studying and reviewing the material. Be disciplined and stick to your routine, ensuring that you are consistently engaging with the subject matter.

    4. Review and Reinforce: Regularly review the material covered in class. Take thorough notes, create flashcards, or develop summary sheets to help reinforce your understanding. Engage in active learning techniques like summarizing concepts in your own words or teaching the material to someone else. Active engagement promotes better retention and comprehension.

    5. Practice, Practice, Practice: Practice is key to mastering any subject. Complete practice problems, exercises, and past exam papers to familiarize yourself with the type of questions you might encounter. As you work through problems, pay attention to your thought process and identify areas where you make mistakes or struggle. This awareness will help you target those areas for improvement.

    6. Form Study Groups: Collaborate with classmates who excel in the subject or are equally motivated to improve. Working together can foster discussion, promote deeper understanding, and provide peer support. Explaining concepts to others can solidify your own knowledge.

    7. Use Additional Resources: Don't limit yourself to just the material provided in class. Explore additional resources such as textbooks, online tutorials, educational websites, or videos that explain the subject matter in different ways. Sometimes, a different perspective can make all the difference in your understanding.

    8. Stay Positive and Persistent: Remember that improvement takes time and effort. Stay positive and motivated, even if you encounter challenges along the way. Persevere through setbacks, and don't let temporary difficulties discourage you. Believe in your abilities and maintain a growth mindset.

    I have faith in your potential to improve in this subject. With dedication, consistent effort, and a proactive approach, I am confident that you can elevate your performance and achieve better results. Don't hesitate to reach out to me or your teacher if you need further assistance or have any questions.

    Wishing you all the best in your studies!


    {name}""")

                
    elif confirm=="change":
        print("Give mark discretion")
        advisor()
                    
    else:
        print("sorry")

advisor()


print(" “Education is the passport to the future, for tomorrow belongs to those who prepare for it today.”")
                

                
                

    # def subjectn(verify,value):
    #     for key in verify:
            
    #         if verify[key]==value:
    #             return key 
    #     return None
    # for mark in range(1,6):
    #     print(f"Enter you mark in {subject} : ")
    #     mark=int(input())
    # while (n<6):
    #     print("Enter your marks ")
    #     print(int(input()))
    #     n=n+1


