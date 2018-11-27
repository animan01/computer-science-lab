import re, requests


# Python code to remove duplicate elements
def RemoveDuplicate(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


url = requests.get('http://www.archer-soft.com/en')
html = url.text
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", html)

print(emails)
print(RemoveDuplicate(emails))
