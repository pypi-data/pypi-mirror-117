from typing import Optional, Union
import pwn
import json


class NCRequester:

    def __init__(self, port: int, hostname: str = "socket.cryptohack.org", actions: Optional[dict] = None) -> None:
        self._hostname: str = hostname
        self._port: int = port
        self._actions: dict = {} if not actions else actions
        self._conn: Optional[pwn.tubes.remote] = None

    @property
    def hostname(self) -> str:
        return self._hostname
    
    @hostname.setter
    def hostname(self, url: str) -> None:
        self._hostname = url

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

    def open(self) -> None:
        try:
            self._conn = pwn.remote(self._hostname, self._port)
        except pwn.PwnlibException as pe:
            print(f"Remote connection failed: {pe}")

    def close(self) -> None:
        if self._conn and self._conn.connected():
            self._conn.close()

    def _connected(self) -> None:
        if not self._conn or not self._conn.connected():
            raise Exception("Connection need to be established before action.")

    def flush_line(self, print_line: bool = False):
        self._connected()
        line: bytes = self._conn.recvline()
        if print_line:
            print(line)

    def recv_only(self, *specific_output) -> Union[str, dict]:
        self._connected()

        raw_result: bytes = self._conn.recvline()

        result: dict = json.loads(raw_result)

        if 'error' in result.keys() and 'error' not in specific_output:
            raise Exception(f"Error message: {result['error']}")

        if len(specific_output) == 1:
            return result[specific_output[0]]
        
        elif len(specific_output) > 0:
            return {k: v for k, v in result.items() if k in specific_output}

        return result

    def recv_send_raw_payload(self, payload: dict, *specific_output, show_payload: bool = False) -> Union[str, dict]:
        self._connected()

        if show_payload:
            print(f"Payload: {payload}")
        
        raw_result: bytes = self._conn.recvline()
        self._conn.sendline(json.dumps(payload))

        result: dict = json.loads(raw_result)

        if 'error' in result.keys() and 'error' not in specific_output:
            raise Exception(f"Error message: {result['error']}")

        if len(specific_output) == 1:
            return result[specific_output[0]]
        
        elif len(specific_output) > 0:
            return {k: v for k, v in result.items() if k in specific_output}

        return result

    def send_recv_raw_payload(self, payload: dict, *specific_output, show_payload: bool = False) -> Union[str, dict]:
        self._connected()

        if show_payload:
            print(f"Payload: {payload}")
        
        self._conn.sendline(json.dumps(payload))
        raw_result: bytes = self._conn.recvline()

        result: dict = json.loads(raw_result)

        if 'error' in result.keys() and 'error' not in specific_output:
            raise Exception(f"Error message: {result['error']}")

        if len(specific_output) == 1:
            return result[specific_output[0]]
        
        elif len(specific_output) > 0:
            return {k: v for k, v in result.items() if k in specific_output}

        return result

    def do_action(self, action_name: str, *specific_output, show_payload: bool = False, **input_params) -> Union[str, dict]:
        self._connected()
        
        if action_name not in self._actions.keys():
            raise Exception(f"Action '{action_name}' not authorized.")

        action: dict = self._actions[action_name]

        if not all(so in action['output'] for so in specific_output):
            raise Exception("Not allowed output asked.")
        
        payload: dict = {"option": action_name}
        for input_name in action['input']:
            if input_name not in input_params.keys():
                raise Exception(f"Missing '{input_name}' parameters.")

            if not isinstance(input_params[input_name], str):
                raise Exception(f"'{input_name}' parameters should be a string instance.")
            
            payload[input_name] = input_params[input_name]
        
        return self.send_recv_raw_payload(payload, *specific_output, show_payload=show_payload)

