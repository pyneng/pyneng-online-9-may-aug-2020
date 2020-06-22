from check_ip_function_main import check_ip


def check_ip_list(ip_list):
    correct_ip_list = []
    wrong_ip_list = []
    for ip in ip_list:
        check = check_ip(ip)
        if check:
            correct_ip_list.append(ip)
        else:
            wrong_ip_list.append(ip)
    return correct_ip_list, wrong_ip_list


if __name__ == "__main__":
    print("#" * 30)
    ip_list_to_check = ["10.1.1.1", "1.2", "8.8.8.8", "500.5.5.1"]
    result = check_ip_list(ip_list_to_check)
    print(result)
