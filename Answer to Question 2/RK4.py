"""
@Author: Jin Huhao
@Date: 2022-12-25
@Description: fourth-order Runge-Kutta
"""

import numpy as np
import matplotlib.pyplot as plt


# k1=100=5/3 k2=600=10 k3=150=2.5 S=10 E=1 ES=P=0
def func_ES(E, S, ES):
    V_ES = 5 / 3 * E * S - 10 * ES - 2.5 * ES
    return V_ES


def func_E(E, S, ES):
    V_E = 2.5 * ES - 5 / 3 * E * S
    return V_E


def func_S(E, S):
    V_S = - 5 / 3 * E * S
    return V_S


def func_P(ES):
    V_P = 2.5 * ES
    return V_P


def Runge_Kutta():
    STEP = 0.04
    E = 1  # um
    S = 10
    ES = 0
    P = 0
    ES_LIST = [ES]
    E_LIST = [E]
    S_LIST = [S]
    P_LIST = [P]

    for i in range(0, 20):
        # step 1
        f_ES_1 = func_ES(E, S, ES)
        f_E_1 = func_E(E, S, ES)
        f_S_1 = func_S(E, S)
        f_P_1 = func_P(ES)
        ES_1 = ES + f_ES_1 * STEP / 2
        E_1 = E + f_E_1 * STEP / 2
        S_1 = S + f_S_1 * STEP / 2
        P_1 = P + f_P_1 * STEP / 2

        # step 2
        f_ES_2 = func_ES(E_1, S_1, ES_1)
        f_E_2 = func_E(E_1, S_1, ES_1)
        f_S_2 = func_S(E_1, S_1)
        f_P_2 = func_P(ES_1)
        ES_2 = ES + f_ES_2 * STEP / 2
        E_2 = E + f_E_2 * STEP / 2
        S_2 = S + f_S_2 * STEP / 2
        P_2 = P + f_P_2 * STEP / 2

        # step 3
        f_ES_3 = func_ES(E_2, S_2, ES_2)
        f_E_3 = func_E(E_2, S_2, ES_2)
        f_S_3 = func_S(E_2, S_2)
        f_P_3 = func_P(ES_2)
        ES_3 = ES + f_ES_3 * STEP
        E_3 = E + f_E_3 * STEP
        S_3 = S + f_S_3 * STEP
        P_3 = P + f_P_3 * STEP

        # step 4
        f_ES_4 = func_ES(E_3, S_3, ES_3)
        f_E_4 = func_E(E_3, S_3, ES_3)
        f_S_4 = func_S(E_3, S_3)
        f_P_4 = func_P(ES_3)

        ES = ES + (f_ES_1 + 2 * f_ES_2 + 2 * f_ES_3 + f_ES_4) * STEP / 6
        E = E + (f_E_1 + 2 * f_E_2 + 2 * f_E_3 + f_E_4) * STEP / 6
        S = S + (f_S_1 + 2 * f_S_2 + 2 * f_S_3 + f_S_4) * STEP / 6
        P = P + (f_P_1 + 2 * f_P_2 + 2 * f_P_3 + f_P_4) * STEP / 6

        ES_LIST.append(ES)
        E_LIST.append(E)
        S_LIST.append(S)
        P_LIST.append(P)

    return ES_LIST, E_LIST, S_LIST, P_LIST


if __name__ == '__main__':
    ES_LIST, E_LIST, S_LIST, P_LIST = Runge_Kutta()
    # result
    print('------ ES ------')
    for i in range(len(ES_LIST)):
        print(ES_LIST[i])
    print('------ E ------')
    for i in range(len(E_LIST)):
        print(E_LIST[i])
    print('------ S ------')
    for i in range(len(S_LIST)):
        print(S_LIST[i])
    print('------ P ------')
    for i in range(len(P_LIST)):
        print(P_LIST[i])

    plt.plot(P_LIST)
    plt.xlabel('number of times')
    plt.ylabel('v')
    plt.show()