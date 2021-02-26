import uuid

# print(uuid.uuid3(uuid.NAMESPACE_DNS, 'guanguoyintao'))
from werkzeug.security import generate_password_hash

print(generate_password_hash('000000'))