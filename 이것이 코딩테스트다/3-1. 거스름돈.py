N = int(input())

if N % 10 != 0:
    print("최소 단위는 10원입니다.")
else:
    won_list = [500, 100, 50, 10]
    won_dict = {'500원': 0, '100원': 0, '50원': 0, '10원': 0}

    for won in won_list:
        won_dict['{}원'.format(won)] = N // won
        N %= won

    print("거스름돈")
    print("500원: {}개".format(str(won_dict['500원'])))
    print("100원: {}개".format(str(won_dict['100원'])))
    print("50원: {}개".format(str(won_dict['50원'])))
    print("10원: {}개".format(str(won_dict['10원'])))
