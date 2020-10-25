
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleague = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name


    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"


    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name


    def __lt__(self, other):
        if self.__actor_full_name is None:
            return False
        elif other.__actor_full_name is None:
            return True
        elif ord(self.__actor_full_name[0]) < ord(other.__actor_full_name[0]):
            return True
        else:
            return False


    def __hash__(self):
        if self.__actor_full_name is None:
            return 0
        else:
            return hash(len(self.__actor_full_name))


    def add_actor_colleague(self, colleague):
        self.__colleague.append(colleague)


    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleague:
            return True
        else:
            return False