from .base import BaseCgi


class StatusJsonCgi(BaseCgi):
    def __init__(self, rest_client) -> None:
        super().__init__(rest_client)
        self.path = "statusjson.cgi"

    def host_count(self) -> None:
        pass

    def host_list(self) -> None:
        pass

    def host(self) -> None:
        pass

    def service_count(self) -> None:
        pass

    def service_list(
        self,
        **params
    ) -> None:
        params = { "query": "servicelist", **params}
        response = self.rest_client.get(path=self.path, params=params)

        return self._result_handler(response)

    def service(self) -> None:
        pass

    def comment_count(self) -> None:
        pass

    def comment_list(self) -> None:
        pass

    def comment(self) -> None:
        pass

    def downtime_count(self) -> None:
        pass

    def downtime_list(self) -> None:
        pass

    def downtime(self) -> None:
        pass

    def program_status(self) -> None:
        pass

    def performance_data(self) -> None:
        pass

    def help(self) -> None:
        pass
