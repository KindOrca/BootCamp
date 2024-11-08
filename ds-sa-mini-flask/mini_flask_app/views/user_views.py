from collections import UserList
import os
import csv
import json

from flask import Blueprint, request
from mini_flask_app import CSV_FILEPATH, TMP_FILEPATH

user_bp = Blueprint('user', __name__)

# CSV 파일 경로와 임시 파일 경로입니다.
CSV_FILEPATH = os.path.join(os.getcwd(), 'mini_flask_app', 'users.csv')

@user_bp.route('/user')
def get_user():
    """
    get_user 함수는 `username` 을 키로 한 값을 쿼리 파라미터 값으로 넘겨주면 
    해당 값을 가진 유저를 리턴해야 합니다.

    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `/api/user`

    상황별 요구사항:
      - `username` 값이 주어지지 않은 경우:
        - 리턴 값: "No username given"
        - HTTP 상태 코드: `400`
      - `username` 이 주어졌지만 해당되는 유저가 없는 경우:
        - 리턴 값: "User '{ username }' doesn't exist"
        - HTTP 상태 코드: `404`
      - 주어진 `username` 값으로 유저를 정상적으로 조회한 경우:
        - 리턴 값: 'users.csv' 파일에 저장된 유저의 `id` 를 문자열로 변경한 값
        - HTTP 상태 코드: `200`
    """
    username = request.args.get('username',default=None)

    users = make_dic()

    if username == None:
      return "No username given", 400
    if username not in users.values():
      return f"User '{ username }' doesn't exist", 404
    else:
      id = [i for i in users.keys() if users[i] == username][0]
      return str(id), 200


@user_bp.route('/user', methods=['PATCH'])
def update_user():
    """
    쿼리 파라미터로 전달되는 `username` 과 `new_username` 데이터로
    'users.csv' 파일에 있는 기존 유저의 'username' 을 변경해 주어야 합니다.

    요구사항:
      - HTTP Method: `PATCH`
      - Endpoint: `api/user`

    상황별 요구사항:
      - 쿼리 파라미터에 `username` 혹은 `new_username` 가 없는 경우:
        - 리턴 값: "No username/new_username given"
        - HTTP 상태 코드: `400`
      - 쿼리 파라미터에서 주어진 `username` 에 해당하는 유저가 'users.csv'
        파일에 존재하지 않은 경우:
        - 리턴 값: "User '{ username }' doesn't exist"
        - HTTP 상태 코드: `400`
      - 쿼리 파라미터에서 주어진 `new_username` 이 이미 사용 중인 경우:
        - 리턴 값: "Username '{ new_username }' is in use"
        - HTTP 상태 코드: `400`
      - 정상적으로 주어진 `username` 을 `new_username` 변경한 뒤 'users.csv' 파일에 기록한 경우:
        - 리턴 값: "OK"
        - HTTP 상태 코드: `200`
    """
    username = request.args.get('username',default=None)
    new_username = request.args.get('new_username',default=None)

    users = make_dic()

    if username == None or new_username == None:
      return "No username/new_username given", 400
    if username not in users.values():
      return f"User '{ username }' doesn't exist", 400
    if new_username in users.values():
      return f"Username '{ new_username }' is in use", 400
    
    idx = [i for i in users.keys() if users[i] == username][0]
    users[idx] = new_username

    with open(CSV_FILEPATH, 'w') as file:
      fieldnames = ['username', 'id']
      wtr = csv.DictWriter(file, fieldnames=fieldnames)
      wtr.writeheader()
      for id, name in users.items():
        wtr.writerow({'id':id, 'username':name})

    return 'OK', 200



    

@user_bp.route('/user', methods=['POST'])
def create_user():
    """
    create_user 함수에서는 JSON 으로 전달되는 데이터로 
    새로운 유저를 'users.csv' 파일에 추가해야 합니다. 이때 추가되는 유저의 아이디
    값은 파일에 존재하는 가장 높은 아이디 값에 1을 추가한 값입니다.

    요구사항:
      - HTTP Method: `POST`
      - Endpoint: `api/user`
      - 받는 JSON 데이터 형식 예시:
            ```json
            {
                "username":"유저 이름"
            }
            ```

    상황별 요구사항:
      - 주어진 JSON 데이터에 `username` 키가 없는 경우:
        - 리턴 값: "No username given"
        - HTTP 상태 코드: `400`
      - 주어진 JSON 데이터의 `username` 을 사용하는 유저가 이미 'users.csv' 파일에 존재하는 경우:
        - 리턴 값: "User '{ username }' already exists"
        - HTTP 상태 코드: `400`
      - 주어진 JSON 데이터의 `username` 으로 정상적으로 생성한 경우:
        - 리턴 값: "Created user '{ username }'"
        - HTTP 상태 코드: `200`
    """
    # data = request.get_json()
    # users = make_dic()
    # if 'username' not in data:
    #   return "No username given", 400
    try:
      data = request.get_json()
      username = data.get('username')
    except:
      return "No username given", 400
    
    users = make_dic()

    if username in users.values():
      return f"User '{ username }' already exists", 400

    with open(CSV_FILEPATH, 'a') as file:
      fieldnames = ['id','username']
      wtr = csv.DictWriter(file, fieldnames=fieldnames)
      wtr.writerow({'id':len(users) + 1, 'username':username})

    return f"Created user '{ username }'", 200

@user_bp.route('/user', methods=['DELETE'])
def delete_user():
    """
    delete_user 함수는 `username` 을 키로 한 값을 
    쿼리 파라미터 값으로 넘겨주면 해당 값을 가진 
    유저를 'users.csv' 파일에서 제거해야 합니다.

    요구사항:
      - HTTP Method: `DELETE`
      - Endpoint: `api/user`

    상황별 요구사항:
      - `username` 값이 주어지지 않은 경우:
        - 리턴 값: "No username given"
        - HTTP 상태 코드: `400`
      - `username` 이 주어졌지만 해당되는 유저가 없는 경우:
        - 리턴 값: "User '{ username }' doesn't exist"
        - HTTP 상태 코드: `404`
      - 주어진 `username` 값을 가진 유저를 정상적으로 삭제한 경우:
        - 리턴 값: "OK"
        - HTTP 상태 코드: `200`
    """
    username = request.args.get('username', default=None)
    users = make_dic()

    if username == None:
      return "No username given", 400
    if username not in users.values():
      return f"User '{ username }' doesn't exist", 404
    
    id = [i for i in users.keys() if users[i] == username][0]
    del users[id]
    
    with open(CSV_FILEPATH,'w') as file:
      fieldnames = ['id','username']
      wtr = csv.DictWriter(file, fieldnames=fieldnames)
      wtr.writeheader()
      for id, username in users.items():
        wtr.writerow({'id':id, 'username':username})

    return 'OK', 200

def make_dic():
  users = dict()
  with open(CSV_FILEPATH, 'r') as file:
    rdr = csv.DictReader(file)
    for i in rdr:
      users[i['id']] = i['username']
  return users