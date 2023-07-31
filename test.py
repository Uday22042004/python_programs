def get_subject_name(verify, value):
    for key, mark in verify.items():
        if mark == value:
            return key
    return None

def get_marks(subject):
    while True:
        mark = input(f"Enter your mark in {subject}: ")
        try:
            mark = int(mark)
            if mark < 5 or mark > 100:
                raise ValueError
            return mark
        except ValueError:
            print("Invalid input. Please enter a valid mark between 5 and 100.")

def run_advisor():
    name = input("Enter your name: ")
    subjects = ("English", "Hindi", "Physics", "Chemistry", "Maths")
    verify = {}

    for subject in subjects:
        mark = get_marks(subject)
        verify[subject] = mark

    mark_list = list(verify.values())
    mark_list.sort()

    weak_subject_index = mark_list[0]
    weak_subject = get_subject_name(verify, weak_subject_index)

    if weak_subject:
        print(f"""Dear {name},

I wanted to talk to you about your recent marks in {weak_subject}. I know you may be disappointed, but I believe in your ability to do better next time.

Remember, one mark doesn't define you or your potential. It's just a chance to learn and improve. Here are some tips to help you score better next time:

1. Reflect on your mistakes: Take a look at where you went wrong and figure out which areas you struggled with the most. Understanding your weaknesses will help you focus your efforts.

2. Talk to your teacher: Don't hesitate to ask your teacher for help. They're there to support you and provide extra guidance. Reach out and ask questions or clarify any doubts you have.

3. Make a study plan: Create a schedule that includes dedicated study time for {weak_subject}. Break it down into smaller, manageable chunks, and stick to your plan.

4. Use available resources: Take advantage of textbooks, online tutorials, and practice exercises. They can provide different explanations and examples to help you understand the concepts better.

5. Study with others: Consider forming study groups with classmates who excel in {weak_subject}. You can learn from each other, discuss challenging topics, and support one another.

6. Practice consistently: Regular practice is key to improving in any subject. Set aside time each day to practice {weak_subject} and work on problem-solving.

Stay positive and don't get discouraged. You have the potential to do great things. Keep working hard, believe in yourself, and you'll see progress.

If you need any further help or have any questions, feel free to reach out to me or your teacher. We're here to support you.

Best of luck, and keep pushing forward!

""")
    else:
        print("Unable to determine the weak subject.")

run_advisor()
