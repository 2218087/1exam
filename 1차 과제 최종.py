# 산업 안전 보건 관리비 계산기

# 대상액이 5억 원 미만일 경우에 각 공사종류에 따른 적용비율(%)
def calculate_safety_health_fee(construction_type, construction_cost):
    if construction_type == 1:
        application_rate = 0.0293
    elif construction_type == 2:
        application_rate = 0.0343
    elif construction_type == 3:
        application_rate = 0.0245
    elif construction_type == 4:
        application_rate = 0.0185
    else:
        print("잘못된 공사 종류 입력")
        return None

# 산업 안전 보건 관리비 계산방법(대상액*적용비율)
    safety_health_fee = construction_cost * application_rate
    return safety_health_fee

# 결과를 출력하는 함수
def display_result(safety_health_fee):
    if safety_health_fee is not None:
        print(f"산업 안전 보건 관리비는 {safety_health_fee:.2f}원입니다.")

# 메인 프로그램
if __name__ == "__main__":
    while True:
        try:  # 사용자로부터 공사 종류와 공사 대상액 입력받는 함수
            construction_type = int(input("공사 종류를 입력하세요 (1:일반건설공사,2:중건설공사,3:철도신설공사,4:특수및기타건설공사): "))
            construction_cost = float(input("공사 대상액을 입력하세요: "))

            if construction_cost >= 500000000:  # 5억 이상일 경우 종료
                print("5억 이상의 공사비용입니다. 프로그램을 종료합니다.")
                break

            safety_health_fee = calculate_safety_health_fee(construction_type, construction_cost)
            display_result(safety_health_fee)
        except ValueError:
            print("유효한 숫자를 입력하세요.")





