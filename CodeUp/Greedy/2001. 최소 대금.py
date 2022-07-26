pasta_a = int(input())
pasta_b = int(input())
pasta_c = int(input())
juice_a = int(input())
juice_b = int(input())

min_pasta = min_juice = 0

# (모든 파스타와 생과일 쥬스의 가격은 100원 이상 2000원 이하이다.)
if 100 <= min(pasta_a, pasta_b, pasta_c, juice_a, juice_b) and max(pasta_a, pasta_b, pasta_c, juice_a, juice_b) <= 2000:
    # 파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
    total_price = (min(pasta_a, pasta_b, pasta_c) + min(juice_a, juice_b)) * 1.1

    # 그날 세트 메뉴의 최소 대금을 소수 첫째자리까지 출력하시오.
    print("{:.1f}".format((min(pasta_a, pasta_b, pasta_c) + min(juice_a, juice_b)) * 1.1))
else:
    print("모든 파스타와 생과일 쥬스의 가격은 100원 이상 2000원 이하입니다.")
