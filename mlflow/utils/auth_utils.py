import jwt
from mlflow.utils.constants import *
from mlflow.exceptions import MlflowException, PERMISSION_DENIED


def get_token_from_file(token_file):
    """
    :param token_file: Path of file containing the jwt token
    :return:
    """
    with open(token_file, 'r') as file_handle:
        token = file_handle.read()
    return token


def get_decrypted_jwt_data(token):
    """
    :param token: String - access token containing information about the user
    :return: dict - Decoded token data
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ENCRYPTION_ALGORITHM])
    except Exception as e:
        raise MlflowException('Invalid jwt token', error_code=PERMISSION_DENIED)


def get_authorised_teams_from_token(token):
    try:
        decoded_token_data = get_decrypted_jwt_data(token)
        return [team.get('team_id') for team in decoded_token_data.get('teams', list())]
    except Exception as e:
        raise MlflowException('Invalid jwt token', error_code=PERMISSION_DENIED)


def get_authorised_teams(token_file):
    """
    :param token_file:  String - file containing access token with information about the user
    :return: list - list of teams which the user is a part of.
    """
    try:
        token = get_token_from_file(token_file)
        return get_authorised_teams_from_token(token)
    except Exception as e:
        raise MlflowException('Invalid token path', error_code=PERMISSION_DENIED)


def get_jwt_token_for_user():
    """
    :param email: email of user
    :param team_id: team_id to which the user belongs
    :return: jwt token containing teh user details
    """
    email = input('Enter Email: ')
    team_id = input('Enter Team Id: ')
    user_data = {
        "teams": [{
            "team_id": team_id,
            "roles": ["VIEWER"]
        }],
        "emp_id": "28888",
        "name": "",
        "email": email,
        "created_at": 1672899265,
        "expiry_at": 1672902865
    }
    return jwt.encode(user_data, JWT_SECRET_KEY, JWT_ENCRYPTION_ALGORITHM)
