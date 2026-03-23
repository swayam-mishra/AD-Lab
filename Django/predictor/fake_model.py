def fake_predict(age, pclass, sex):
    if age < 18 or sex == 'female':
        return "Survived"
    return "Did Not Survive"
