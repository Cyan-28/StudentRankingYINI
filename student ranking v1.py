class Score: 

    def __init__(self, maths, mmaths, english, menglish, science, mscience):

        self.english = english
        self.menglish = menglish
        self.maths = maths
        self.mmaths = mmaths
        self.science = science
        self.mscience = mscience


    def Average(self):
        print((self.science + self.english + self.maths)/3)
		

    def ProgressScore(self):

        print("Maths: ",(self.maths-self.mmaths)/10)
        print("English: ",(self.english-self.menglish)/10)
        print("Science: ",(self.science-self.mscience)/10)



test = Score(88, 99, 96, 92, 54, 79)

test.ProgressScore()