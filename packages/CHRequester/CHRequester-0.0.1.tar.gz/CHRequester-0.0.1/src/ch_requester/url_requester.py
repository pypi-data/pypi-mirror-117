from typing import Optional, Union
import requests


class URLRequester:

    def __init__(self, url: str, actions: Optional[dict] = None) -> None:
        self._url: str = url
        self._actions: dict = {} if not actions else actions

    @property
    def url(self) -> str:
        return self._url
    
    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    @property
    def actions(self) -> dict:
        return self._actions

    @actions.setter
    def actions(self, actions: dict) -> None:
        self._actions = actions

    def add_action(self, action_name: str, inputs: tuple, outputs: tuple) -> None:
        if action_name in self._actions.keys():
            raise Exception(f"Action '{action_name}' already exists.")
    
        self._actions[action_name] = {'input': inputs, 'output': outputs}

    def do_action(self, action_name: str, *specific_output, show_url: bool = False, **input_params) -> Union[str, dict]:
        if action_name not in self._actions.keys():
            raise Exception(f"Action '{action_name}' not authorized.")

        action: dict = self._actions[action_name]

        if not all(so in action['output'] for so in specific_output):
            raise Exception("Not allowed output asked.")
        
        url: str = self._url + action_name + "/"
        for input_name in action['input']:
            if input_name not in input_params.keys():
                raise Exception(f"Missing '{input_name}' parameters.")
            
            url += f"{input_params[input_name].hex()}/"
        
        if show_url:
            print(f"Url: {url}")
        
        r: requests.Response = requests.get(url)

        if r.status_code != 200:
            raise Exception("Status code not 200.")

        result: dict = r.json()

        if 'error' in result.keys() and 'error' not in specific_output:
            raise Exception(f"Error message: {result['error']}")

        if len(specific_output) == 1:
            return result[specific_output[0]]
        
        elif len(specific_output) > 0:
            return {k: v for k, v in result.items() if k in specific_output}

        return result

