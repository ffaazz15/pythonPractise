
from functools import partial


def email(id,domain,extension):
    print(id+domain+extension)

db1 = partial(email,"mohammedfazil196",)
db1("@gamil",".com")