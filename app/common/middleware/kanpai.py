from kanpai import Kanpai

userRegister = Kanpai.Object({
    "name": Kanpai.String().trim().required(),
    "email": Kanpai.Email().required(),
    "password": Kanpai.String().trim().required(),
    "role": Kanpai.String().trim().required()
})


userLogin = Kanpai.Object({
    "email": Kanpai.Email().required(),
    "password": Kanpai.String().trim().required()
})

inputTask = Kanpai.Object({
    "user_id": Kanpai.Number().required(),
    "title": Kanpai.String().required(),
    "description": Kanpai.String().required(),
    "duedate": Kanpai.String().required(),
    "status": Kanpai.String().required()
})
