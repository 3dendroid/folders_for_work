import os

# current_month = datetime.date.today().month
# print(current_month)

path = r'C:\Users\denki\Desktop\SN_bugs\november'

folders = [
    'screenshots',
    'videos',
    'jsons',
    'profiles',
    'tasks',
    'logs',
]


# months = [
#     [1], ['january'],
#     [2], ['february'],
#     [3], ['march'],
#     [4], ['april'],
#     [5], ['may'],
#     [6], ['june'],
#     [7], ['july'],
#     [8], ['august'],
#     [9], ['september'],
#     [10], ['october'],
#     [11], ['november'],
#     [12], ['december'],
# ]

def empty_folder(path, folders):
    for f in folders:
        os.mkdir('' + f)


if __name__ == "__main__":
    empty_folder(path, folders)
