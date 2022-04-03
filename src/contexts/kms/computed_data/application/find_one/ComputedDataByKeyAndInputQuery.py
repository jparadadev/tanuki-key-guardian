from src.contexts.shared.domain.Query import Query


class ComputedDataByKeyAndInputQuery(Query):
    QUERY_TYPE: str = 'kms.computed-data.find-by-key-and-input'

    def __init__(
            self,
            key_id: str,
            input: str,
            type: str,
    ):
        self.key_id = key_id
        self.input = input
        self.type = type

    def get_query_type_name(self) -> str:
        return self.QUERY_TYPE
