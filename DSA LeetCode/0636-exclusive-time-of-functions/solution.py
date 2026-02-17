class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0] * n
        call_stack = []
        previous_time = 0

        for log in logs:
            function_id_str, event_type, timestamp_str = log.split(":")
            function_id = int(function_id_str)
            current_time = int(timestamp_str)

            if event_type == "start":
                if call_stack:
                    running_function = call_stack[-1]
                    exclusive_time[running_function] += current_time - previous_time

                call_stack.append(function_id)
                previous_time = current_time

            else:  # end
                finished_function = call_stack.pop()
                exclusive_time[finished_function] += current_time - previous_time + 1
                previous_time = current_time + 1

        return exclusive_time
        
