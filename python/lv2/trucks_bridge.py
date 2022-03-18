from collections import deque


def solution(bridge_length, weight, truck_weights):
    sec = 0
    sum_bridge = 0
    #zerosum = 0
    truck_weights = deque(truck_weights)

    bridge = deque([0]*(bridge_length+1))
    while True:
        sec += 1
        if truck_weights:
            if sum_bridge+truck_weights[0] > weight:  # 수용 불가
                bridge.append(0)
            else:  # 수용 가능
                # if sum_bridge == 0:
                #     zerosum += 1
                truck = truck_weights.popleft()
                bridge.append(truck)
                sum_bridge += truck

        else:
            if sum_bridge == 0:
                break

        bridge.popleft()
        sum_bridge -= bridge[1]
        # print(bridge)

    return sec  # -zerosum


print(solution(2, 10, [7, 4, 5, 6]))
