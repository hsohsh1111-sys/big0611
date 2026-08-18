def get_valid_age():
    while True:
        try:
            age_input = input("Enter your age: ") 
            age = int(age_input)
            if age < 0:
                print("나이가 0 이상이어야 합니다.")
                continue
            elif age > 150:       
                print("유효하지 않는 나이입니다.")
                continue
            else:
                return age
        except ValuneError as e:
            print(f'숫자만 입력해 주세요: {e}')

        else:
            break 


try:
     user_age = get_valid_age()
     if user_age :
          print(f"Your age is: {user_age}")
except:
     print("An error occurred while getting the age.")          