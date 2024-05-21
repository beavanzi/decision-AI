class InputView:
    def __init__(self):
        self.BMI = float(input("Valor de IMC: "))
        self.Glucose = float(input("Valor de Glicose: "))
        self.Insulin = float(input("Valor de Insulina: "))
        self.DiabetesPedigreeFunction = float(input("Valor de DiabetesPedigreeFunction: "))
        self.classes = []

    def calc_classes(self, references):
        classes = []
        

        for k, v in references.items():

            attrib = getattr(self, k)

            for key, value in v.items():
                condition_to_equal = value[0] == 0
                if condition_to_equal:
                    condition = (attrib >= value[0]) & (attrib <= value[1])
                else:
                    condition = (attrib > value[0]) & (attrib <= value[1])

                if condition:
                    classNumber = key.split(" ")[1]
                    classes.append(k +" " +classNumber)
                    break
        self.classes = classes

class OutputView:
    
    def __init__(self, classes,references):
        self.classes = classes
        self.helthy=references.get("helthy")
        self.should_go_on_diet=references.get("should_go_on_diet")
        self.need_to_go_on_doctor=references.get("need_to_go_on_doctor")  
        self.decisions_dict = {
            "helthy":0,
            "should_go_on_diet":0,
            "need_to_go_on_doctor":0
        }
       
    
    def calc_utility(self,prob_has_diabetes):
        print("Calculando Melhor decisão...")
        for classe in self.classes:
            class_name,class_number = classe.split(" ")[0],classe.split(" ")[1]
            probability_event = prob_has_diabetes[class_name][int(class_number)-1]
            for key in self.decisions_dict.keys():
                decision = getattr(self,key)
                utility = decision[classe]
                self.decisions_dict[key] += utility*probability_event

        max_value = max(self.decisions_dict.values())
        max_key = [k for k, v in self.decisions_dict.items() if v == max_value][0]
   
        print("{}".format(2*"\n"))
        print(getattr(self,max_key)["output"]+"\n")  
        print("UTILIDADE DA DECISÃO: ", max_value)