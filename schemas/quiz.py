
def quizEntity(item)->dict:
    return {
        "id":            str(item["_id"]),
        "num":           str(item["num"]),
        "profession":    str(item["profession"]),
        "institution":   str(item["institution"]),
        "answer":        str(item["answer"]),
    }

def quizsEntity(entity)->list:
    return  [quizEntity(item) for item in entity]