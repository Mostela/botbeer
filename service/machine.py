#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from statemachine import StateMachine, State


class StateInfos(StateMachine):
    start_talk = State('Start Talk', initial=True)
    info_name = State('Info Name')
    # starting from option_list begin
    option_list = State('Option List')

    list_all = State('List Products')
    choice_one = State('Choice Product')
    # Start checkout state machine
    cart_checkout = State('Checkout')
    # Start payment state machine
    payment_products = State('Payment Products')
    exit = State('End')

    start = start_talk.to(info_name)
    what_name = info_name.to(option_list)
    products_list = option_list.to(list_all)
    choice_product = list_all.to(choice_one)
    more_one = choice_one.to(list_all)
    not_more_one = choice_one.to(cart_checkout)
    choice_checkout = cart_checkout.to(payment_products)
    choice_payment = payment_products.to(exit)

