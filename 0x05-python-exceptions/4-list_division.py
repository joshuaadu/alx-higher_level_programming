#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        value = 0
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            result.append(value)

        except ZeroDivisionError:
            print("division by 0")
            result.append(value)

        except IndexError:
            print("out of range")
            result.append(value)

        except Exception:
            result.append(value)

        finally:
            continue
    return result
