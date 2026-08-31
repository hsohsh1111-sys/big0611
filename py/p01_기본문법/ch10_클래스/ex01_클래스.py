# 클래스 정의
class Character:
    # 생성자 (Constructor): 객체가 만들어질 때 처음 자동으로 실행되는 특별한 함수
    def __init__(self, name, hp):
        self.name = name  # 인스턴스 변수 (속성, Attribute)
        self.hp = hp      # 인스턴스 변수

    # 메서드 (Method): 클래스 내부에 정의된 함수 (기능)
    def take_damage(self, damage):
        self.hp -= damage
        print(f"[{self.name}]이(가) {damage}의 피해를 입었습니다! (남은 HP: {self.hp})")

# 객체 생성
# 1. 서로 다른 데이터(이름, 체력)를 가진 객체 2개 생성
warrior = Character("전사", 100)
wizard = Character("마법사", 60)

# 2. 각 객체의 속성(데이터) 접근
# 객체.속성
print(warrior.name)  # 출력: 전사
print(wizard.hp)     # 출력: 60

# 3. 각 객체의 메서드(기능) 실행
# 객체.메서드()
# 문자열.split()
warrior.take_damage(20)  # 출력: [전사]이(가) 20의 피해를 입었습니다! (남은 HP: 80)
wizard.take_damage(15)   # 출력: [마법사]이(가) 15의 피해를 입었습니다! (남은 HP: 45)