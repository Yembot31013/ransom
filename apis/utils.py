import uuid

def get_random_code():
  code = str(uuid.uuid5(uuid.NAMESPACE_DNS, "hack.com"))[:7].replace('-', '').lower()
  return code