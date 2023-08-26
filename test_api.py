import json
import requests

host = 'http://localhost:8000/api'

header = {"Content-Type": "application/json"}


def test_create_student_score():
    data = {"first_name": "Chaiyatat",
            "last_name": "Meema",
            "subject_title": "Coding",
            "score": 50
            }

    response = requests.post(url=f'{host}/student_score/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_get_student_score(student_id):
    response = requests.get(url=f"{host}/student_score/{student_id}/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


def test_personnel_details():
    response = requests.get(url=f"{host}/personnel_details/Dorm Palace School", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


def test_school_hierarchy():
    response = requests.get(url=f"{host}/school_hierarchy/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


def test_school_structure():
    response = requests.get(url=f"{host}/school_structure/", headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4, ensure_ascii=False)}\n")


host2='http://localhost:8000/todo'

id = 1

def test_create_todo():
    data = {
        "title": "head",
        "description": "body",
    }

    response = requests.post(url=f'{host2}/', headers=header, data=json.dumps(data))
    global id
    id = response.json()["id"]
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_edit_todo(post_id: int):
    data = {
        "id": post_id,
        "title": "head2",
        "description": "body2",
        "done": True,
    }

    response = requests.patch(url=f'{host2}/', headers=header, data=json.dumps(data))
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_view_all_todo():

    response = requests.get(url=f'{host2}/', headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_view_todo(post_id: int):

    response = requests.get(url=f'{host2}/{post_id}', headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")

def test_del_todo(post_id: int):

    response = requests.delete(url=f'{host2}/{post_id}', headers=header)
    print(f"\nstatus {response.status_code}\nresponse = {json.dumps(response.json(), indent=4)}\n")


if __name__ == '__main__':
    pass

    test_create_student_score()
    test_get_student_score(1)
    test_personnel_details()
    test_school_hierarchy()
    test_school_structure()

    test_create_todo()
    test_edit_todo(id)
    test_view_all_todo()
    test_view_todo(id)
    test_del_todo(id)



