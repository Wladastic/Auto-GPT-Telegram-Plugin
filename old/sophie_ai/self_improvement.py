class SelfImprovement:
    def __init__(self, ml_core, gpt_integration):
        self.ml_core = ml_core
        self.gpt_integration = gpt_integration

    def analyze_performance(self, input_data, output_data, true_output_data):
        correct_predictions = 0
        total_predictions = len(output_data)

        for i in range(total_predictions):
            if output_data[i] == true_output_data[i]:
                correct_predictions += 1

        accuracy = correct_predictions / total_predictions
        return accuracy

    def update_model(self, input_data, true_output_data):
        self.ml_core.train_model(input_data, true_output_data)
        gpt_suggestions = self.gpt_integration.gpt_request(input_data, true_output_data)
        parsed_suggestions = self.gpt_integration.gpt_response_parser(gpt_suggestions)

        for suggestion in parsed_suggestions:
            if suggestion['type'] == 'edit_code':
                self.ml_core.edit_code(suggestion['file'], suggestion['line_number'], suggestion['new_code'])
            elif suggestion['type'] == 'create_file':
                self.ml_core.create_file(suggestion['file'], suggestion['content'])

        self.ml_core.train_model(input_data, true_output_data)