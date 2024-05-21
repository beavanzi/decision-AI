__ibm_groups = {
            "Class 1": (0.0, 18.5),
            "Class 2": (18.5, 25),
            "Class 3": (25, 1000),
        }

__glucose_groups = {
            "Class 1": (0.0, 100),
            "Class 2": (100, 125),
            "Class 3": (125, 100000),
        }

__insulin_groups = {
            "Class 1": (0.0, 140),
            "Class 2": (140, 199),
            "Class 3": (199, 10000),
        }

__pedigree_groups = {
            "Class 1": (0, 0.3),
            "Class 2": (0.3, 10),
        }

_helthy_util={
            "output":"Não precisa se preucupar",
            "BMI 1":25,
            "BMI 2":60,
            "BMI 3":25,
            "Glucose 1":50,
            "Glucose 2":30,
            "Glucose 3":15,
            "Insulin 1":80,
            "Insulin 2":15,
            "Insulin 3":0,
            "DiabetesPedigreeFunction 1":45,
            "DiabetesPedigreeFunction 2":25
        }
        
_should_go_on_diet_util={
            "output":"Deve melhorar a alimentação",
            "BMI 1":55,
            "BMI 2":25,
            "BMI 3":65,
            "Glucose 1":30,
            "Glucose 2":70,
            "Glucose 3":25,
            "Insulin 1":20,
            "Insulin 2":70,
            "Insulin 3":0,
            "DiabetesPedigreeFunction 1":30,
            "DiabetesPedigreeFunction 2":50
        }
_need_to_go_on_doctor_util={
            "output":"Deve ir ao médico",
            "BMI 1":75,
            "BMI 2":15,
            "BMI 3":75,
            "Glucose 1":25,
            "Glucose 2":60,
            "Glucose 3":90,
            "Insulin 1":30,
            "Insulin 2":50,
            "Insulin 3":100,
            "DiabetesPedigreeFunction 1":15,
            "DiabetesPedigreeFunction 2":70
        }

references = {
    "BMI": __ibm_groups,
    "Glucose": __glucose_groups,
    "Insulin": __insulin_groups,
    "DiabetesPedigreeFunction": __pedigree_groups,
    
}

decision_references = {
    "helthy": _helthy_util,
    "should_go_on_diet": _should_go_on_diet_util,
    "need_to_go_on_doctor": _need_to_go_on_doctor_util,
}

