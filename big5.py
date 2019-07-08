'''
    alter last week's big5 program so that it does everything it did last week, and in addition:
    1. reads in the questions from the five question files, and stores them in five different lists
    2. reads in and stores the scoring information from the same files
        (e.g., what questions are positive, and what questions are negative
    3. use the stored scoring information to calculate the updated score after each question is asked
    4. uses a while loop to ensure that numbers between 1-5 are the only valid responses
    5. prints the scores out in two rows and five columns, with at least 5 spaces between each columns,
        and with the score centered under the label, like this:
        openness     conscientiousness     extroversion     agreeableness     neuroticism
           20               20                  8                 5                11
'''
e = open('e.txt')
a = open('a.txt')
c = open('c.txt')
n = open('n.txt')
o = open('o.txt')
question_list = []
points_list = []
e_question_list = []
e_points_list = []
a_question_list = []
a_points_list = []
c_question_list = []
c_points_list = []
n_question_list = []
n_points_list = []
o_question_list = []
o_points_list = []
for line in e:
    data = line.strip('\n')
    data = data.split(',')
    e_question_list.append(data[0])
    e_points_list.append(data[1])
for line in a:
    data = line.strip('\n')
    data = data.split(',')
    a_question_list.append(data[0])
    a_points_list.append(data[1])
for line in c:
    data = line.strip('\n')
    data = data.split(',')
    c_question_list.append(data[0])
    c_points_list.append(data[1])
for line in n:
    data = line.strip('\n')
    data = data.split(',')
    n_question_list.append(data[0])
    n_points_list.append(data[1])
for line in o:
    data = line.strip('\n')
    data = data.split(',')
    o_question_list.append(data[0])
    o_points_list.append(data[1])
question_list = [e_question_list, a_question_list, c_question_list, n_question_list, o_question_list]
points_list = [e_points_list, a_points_list, c_points_list, n_points_list, o_points_list]
score = [20, 14, 14, 38, 8]
i = 0
j = 0
for j in range(0,10):
    for i in range(0,5):
        print(question_list[i][j])
        ori = input()
        try:
            ori = int(ori)
        except:
            print("Your input must be an integer")
        x = int(ori)
        while x < 1 or x > 5:
            print("invalid input, please enter a number within 1-5")
            x = int(ori)
        score[i] += x * int(points_list[i][j])
        i += 1
    j += 1

print("openness"+     +"conscientiousness"+     +"extroversion"+     "agreeableness"+     +"neuroticism")
print("{0}     {1}     {2}     {3}     {4}" .format(score[4],score[2],score[0],score[1],score[3]))



